#!/usr/bin/env python3
import csv
import re
import sys
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Set, Tuple
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "specs" / "matrices" / "function_matrix_normalized.csv"
DOCS_DIR = ROOT / "specs" / "functions"
REPORT = ROOT / "specs" / "reports" / "function_doc_validation.csv"

HEADER_RE = re.compile(r"^##\s+([A-Z0-9_.]+)\s*$")
INLINE_RE = re.compile(r"`([A-Z0-9_.]+)`")
REQUIRED_SECTION_PATTERNS = {
    "purpose": r"^##\s+purpose\s*$",
    "syntax": r"^##\s+syntax\s*$",
    "behavior": r"^##\s+behavior\s*$",
    "examples": r"^##\s+examples\s*(?:\(expected outputs\))?\s*$",
    "error cases": r"^##\s+error cases\s*$",
    "notes": r"^##\s+notes\s*$",
    "code location": r"^##\s+code location\s*$",
    "sources": r"^##\s+sources\s*$",
    "microsoft docs": r"^##\s+documentation\s*\(\s*microsoft\s*\)\s*$",
    "google sheets docs": r"^##\s+documentation\s*\(\s*google\s*sheets\s*\)\s*$",
}
GENERIC_MS_ROOT = "https://support.microsoft.com/en-us/office"
GENERIC_MS_SOURCE = "https://support.microsoft.com/en-us/office/"
GENERIC_MS_FUNC_INDEX = "https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188"
GENERIC_GS_FUNC_INDEX = "https://support.google.com/docs/table/25273?hl=en"
SOURCE_PLACEHOLDER_STRINGS = (
    "fetch failure prevented extraction.",
    "no source data available",
    "could not extract from source page",
    "fetch_failed:",
    "source fetch status: failed",
    "failed to fetch source",
    "re-run enrichment",
    "not captured from source",
    "see source link for provider-specific behavior details",
    "not available for this provider.",
)

SOURCE_LINE_RE = re.compile(r"^-\s*(excel|google\s*sheets)\s*:\s*(https?://\S+)\s*$", re.I)

DOC_SECTION_FIELD_PATTERNS = {
    "microsoft": {
        "source url": re.compile(r"^\s*-\s*source\s*url\s*:", re.I | re.M),
        "summary": re.compile(r"^\s*-\s*summary\s*:", re.I | re.M),
        "signatures": re.compile(r"^\s*-\s*signatures?\s*:", re.I | re.M),
        "examples": re.compile(r"^\s*-\s*examples?\s*:", re.I | re.M),
        "notes": re.compile(r"^\s*-\s*notes\s*:", re.I | re.M),
        "error behavior": re.compile(r"^\s*-\s*error\s*behavior\s*:", re.I | re.M),
    },
    "google sheets": {
        "source url": re.compile(r"^\s*-\s*source\s*url\s*:", re.I | re.M),
        "summary": re.compile(r"^\s*-\s*summary\s*:", re.I | re.M),
        "signatures": re.compile(r"^\s*-\s*signatures?\s*:", re.I | re.M),
        "examples": re.compile(r"^\s*-\s*examples?\s*:", re.I | re.M),
        "notes": re.compile(r"^\s*-\s*notes\s*:", re.I | re.M),
        "error behavior": re.compile(r"^\s*-\s*error\s*behavior\s*:", re.I | re.M),
    },
}


def read_matrix(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"Missing matrix: {path}")
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        if "Function" not in reader.fieldnames:
            raise ValueError("Matrix CSV missing 'Function' column")
        return [row["Function"].strip().upper() for row in reader]


def read_matrix_rows(path: Path) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing matrix: {path}")
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    return {
        row["Function"].strip().upper(): {
            "excel": row.get("Excel", "N"),
            "sheets": row.get("GoogleSheets", row.get("Google", "N")),
        }
        for row in rows
    }


def extract_functions_from_md(path: Path) -> Set[str]:
    funcs: Set[str] = set()
    for line in path.read_text().splitlines():
        m = HEADER_RE.match(line.strip())
        if m:
            funcs.add(m.group(1).upper())
        for m in INLINE_RE.finditer(line):
            funcs.add(m.group(1).upper())
    return funcs


def check_required_sections(path: Path) -> List[str]:
    missing = []
    lines = [line.strip().lower() for line in path.read_text().splitlines()]
    for section, pattern in REQUIRED_SECTION_PATTERNS.items():
        rx = re.compile(pattern)
        if not any(rx.match(line) for line in lines):
            missing.append(section)
    return missing


def extract_named_section(lines: List[str], heading: str) -> List[str]:
    target = heading.strip().lower()
    in_section = False
    section: List[str] = []
    for line in lines:
        stripped = line.strip().lower()
        if stripped.startswith("## "):
            if stripped == target:
                in_section = True
                continue
            if in_section:
                break
        if in_section:
            section.append(line)
    return section


def normalize_source_url(url: str) -> str:
    return url.strip().rstrip("/")


def parse_provider_section_fields(lines: List[str]) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    current_key = ""
    for raw_line in lines:
        line = raw_line.strip()
        m = re.match(r"^-+\s*([A-Za-z ]+)\s*:\s*(.*)$", line)
        if m:
            key = m.group(1).strip().lower()
            fields[key] = m.group(2).strip()
            current_key = key
            continue
        if not current_key or not line:
            continue
        if line.startswith("-") and not line.startswith("--"):
            value = line.lstrip("-").strip()
            if value and current_key in fields:
                fields[current_key] = f"{fields[current_key]} {value}".strip()
        elif raw_line.startswith("  - "):
            value = raw_line.strip().lstrip("-").strip()
            if value and current_key in fields:
                fields[current_key] = f"{fields[current_key]} {value}".strip()
    return fields


def function_name_variants(name: str) -> List[str]:
    normalized = name.upper().strip()
    variants = [normalized]
    no_separators = re.sub(r"[._]", "", normalized)
    if no_separators and no_separators not in variants:
        variants.append(no_separators)
    alnum_only = re.sub(r"[^A-Z0-9]", "", normalized)
    if alnum_only and alnum_only not in variants:
        variants.append(alnum_only)
    return [v for v in variants if v]


def has_function_signature(value: str, fn: str) -> bool:
    for variant in function_name_variants(fn):
        fn_esc = re.escape(variant)
        if re.search(rf"\b{fn_esc}\s*\(", value, flags=re.I):
            return True
    return False


def has_formula_like_example(value: str, fn: str) -> bool:
    if not value:
        return False
    for variant in function_name_variants(fn):
        fn_esc = re.escape(variant)
        if re.search(rf"\b{fn_esc}\s*\(", value, flags=re.I):
            return True
    return False


def is_placeholder(value: str) -> bool:
    lowered = value.lower()
    return any(token in lowered for token in SOURCE_PLACEHOLDER_STRINGS)


def validate_provider_docs(
    path: Path,
    fn: str,
    support: Dict[str, str],
    sources: Dict[str, str],
) -> List[str]:
    fn_norm = fn
    issues: List[str] = []
    lines = path.read_text().splitlines()
    ms_section = extract_named_section(lines, "## documentation (microsoft)")
    gs_section = extract_named_section(lines, "## documentation (google sheets)")
    if not ms_section:
        issues.append("missing_microsoft_documentation_section")
        return issues
    if not gs_section:
        issues.append("missing_google_sheets_documentation_section")
        return issues

    section_map = {
        "microsoft": (ms_section, support.get("excel", "N") == "Y", sources.get("excel", "")),
        "google sheets": (gs_section, support.get("sheets", "N") == "Y", sources.get("sheets", "")),
    }
    for provider, (content, supported, source_url) in section_map.items():
        section_text = "\n".join(content)
        required = DOC_SECTION_FIELD_PATTERNS[provider]
        if supported:
            for key, pattern in required.items():
                if not pattern.search(section_text):
                    issues.append(f"{provider.replace(' ', '_')}_{key}")
        fields = parse_provider_section_fields(content)

        if not source_url:
            issues.append(f"{provider.replace(' ', '_')}_missing_source_url_in_sources")
            continue

        if provider == "microsoft" and not source_url.startswith("https://support.microsoft.com/"):
            issues.append(f"{provider.replace(' ', '_')}_bad_source_domain")
        if provider == "google sheets" and not source_url.startswith("https://support.google.com/docs/"):
            issues.append(f"{provider.replace(' ', '_')}_bad_source_domain")

        normalized = normalize_source_url(source_url).lower()
        if supported:
            if provider == "microsoft" and (
                normalized == GENERIC_MS_FUNC_INDEX or
                normalized == GENERIC_MS_SOURCE or
                normalized == GENERIC_MS_ROOT
            ):
                issues.append(f"{provider.replace(' ', '_')}_generic_source_url_for_supported_provider")
            if provider == "google sheets" and normalized == GENERIC_GS_FUNC_INDEX:
                issues.append(f"{provider.replace(' ', '_')}_generic_source_url_for_supported_provider")

        if supported and "not present in the provider's function index for this batch" in section_text.lower():
            issues.append(f"{provider.replace(' ', '_')}_unsupported_marker_for_supported_provider")
        if supported and is_placeholder(fields.get("summary", "")):
            issues.append(f"{provider.replace(' ', '_')}_placeholder_summary")
        if supported and is_placeholder(fields.get("examples", "")):
            issues.append(f"{provider.replace(' ', '_')}_placeholder_examples")
        if supported and is_placeholder(fields.get("signatures", "")):
            issues.append(f"{provider.replace(' ', '_')}_placeholder_signatures")
        if supported and not has_function_signature(fields.get("signatures", ""), fn_norm):
            # Fallback to example expressions when syntax extraction is incomplete.
            if not has_formula_like_example(fields.get("examples", ""), fn_norm):
                issues.append(f"{provider.replace(' ', '_')}_missing_signature_expression")
        if supported and (
            is_placeholder(fields.get("notes", ""))
            or "provider-specific behavior" in fields.get("notes", "").lower()
        ):
            issues.append(f"{provider.replace(' ', '_')}_insufficient_notes")
        if supported and is_placeholder(fields.get("error behavior", "")):
            issues.append(f"{provider.replace(' ', '_')}_placeholder_error_behavior")
        if supported and (
            not has_formula_like_example(fields.get("examples", ""), fn_norm)
            and not has_formula_like_example(fields.get("notes", ""), fn_norm)
        ):
            issues.append(f"{provider.replace(' ', '_')}_insufficient_examples")
        if supported and not fields.get("error behavior"):
            issues.append(f"{provider.replace(' ', '_')}_missing_error_behavior")
    return issues


def extract_sources(path: Path) -> Dict[str, str]:
    text = path.read_text()
    lines = text.splitlines()
    in_sources = False
    sources: Dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith("## sources"):
            in_sources = True
            continue
        if in_sources and stripped.startswith("##"):
            in_sources = False
            continue
        if not in_sources:
            continue
        m = SOURCE_LINE_RE.match(stripped)
        if not m:
            continue
        provider = m.group(1).strip().lower().replace(" ", "_")
        url = m.group(2).strip()
        if provider == "excel":
            sources["excel"] = url
        elif provider == "google_sheets":
            sources["sheets"] = url
    return sources


def source_quality_issues(
    function_name: str,
    sources: Dict[str, str],
    source_stats: Dict[str, int],
    used_urls: Dict[Tuple[str, str], List[str]],
    support: Dict[str, str],
) -> List[str]:
    issues = []
    if "excel" not in sources:
        issues.append(f"missing_excel_source")
    else:
        url = sources["excel"]
        if not url.startswith("https://support.microsoft.com/"):
            issues.append(f"bad_excel_source_domain:{url}")
        normalized = normalize_source_url(url).lower()
        if support.get("excel", "N") == "Y" and (
            normalized == GENERIC_MS_FUNC_INDEX or normalized == GENERIC_MS_SOURCE or normalized == GENERIC_MS_ROOT
        ):
            issues.append("generic_excel_index_source")
        key = (url, "excel")
        if key in used_urls:
            used_urls[key].append(function_name)
        else:
            used_urls[key] = [function_name]
        source_stats["excel"] = source_stats.get("excel", 0) + 1

    if "sheets" not in sources:
        issues.append(f"missing_sheets_source")
    else:
        url = sources["sheets"]
        if not url.startswith("https://support.google.com/docs/"):
            issues.append(f"bad_sheets_source_domain:{url}")
        if support.get("sheets", "N") == "Y" and normalize_source_url(url) == GENERIC_GS_FUNC_INDEX:
            issues.append("generic_sheets_index_source")
        key = (url, "sheets")
        if key in used_urls:
            used_urls[key].append(function_name)
        else:
            used_urls[key] = [function_name]
        source_stats["sheets"] = source_stats.get("sheets", 0) + 1

    return issues


def parse_batch_arg(argv: List[str]) -> str:
    for i, token in enumerate(argv):
        if token == "--batch" and i + 1 < len(argv):
            return argv[i + 1]
    return ""


def parse_verbose_arg(argv: List[str]) -> bool:
    return "--quiet" not in argv


def collect_docs(docs_dir: Path) -> Dict[str, Path]:
    docs: Dict[str, Path] = {}
    for md in sorted(docs_dir.glob("*.md")):
        name = md.stem.upper()
        docs[name] = md
    return docs


def load_batch_filter() -> Tuple[str, Set[str]]:
    batch = parse_batch_arg(sys.argv)
    if not batch:
        return "ALL", set()
    # Primary batching source used for operational rollups.
    primary_batch_file = ROOT / "specs" / "data" / "function_batches.csv"
    fallback_batch_file = ROOT / "specs" / "data" / "function_complexity_map.csv"
    if not primary_batch_file.exists() and not fallback_batch_file.exists():
        raise FileNotFoundError(f"Missing batch files: {primary_batch_file} and {fallback_batch_file}")

    selected = set()
    batch_file = primary_batch_file if primary_batch_file.exists() else fallback_batch_file
    with batch_file.open(newline="") as f:
        for row in csv.DictReader(f):
            if row.get("batch_id") == batch:
                selected.add(row["function_name"].strip().upper())
    if selected:
        return batch, selected

    if batch_file is fallback_batch_file:
        return batch, selected

    fallback_batch = "function_complexity_map.csv"
    with fallback_batch_file.open(newline="") as f:
        for row in csv.DictReader(f):
            if row.get("batch_id") == batch:
                selected.add(row["function_name"].strip().upper())
    return batch, selected


def main() -> int:
    try:
        functions = read_matrix(MATRIX)
        matrix_rows = read_matrix_rows(MATRIX)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    if not DOCS_DIR.exists():
        print(f"Missing docs directory: {DOCS_DIR}", file=sys.stderr)
        return 2

    docs = collect_docs(DOCS_DIR)
    batch_label, batch_filter = load_batch_filter()
    verbose = parse_verbose_arg(sys.argv)
    quiet = not verbose

    rows: List[Tuple[str, str, str]] = []
    missing = 0
    status_counts: Dict[str, int] = {}
    missing_section_counts: DefaultDict[str, int] = defaultdict(int)
    failures: List[str] = []
    source_stats: Dict[str, int] = {}
    used_urls: Dict[str, List[str]] = {}

    # Validate each function in matrix
    for fn in functions:
        if batch_filter and fn not in batch_filter:
            continue
        doc = docs.get(fn)
        expected_doc = DOCS_DIR / f"{fn}.md"
        if not doc:
            status = "MISSING_DOC"
            row = (fn, status, str(expected_doc))
            rows.append(row)
            status_counts[status] = status_counts.get(status, 0) + 1
            msg = f"[batch={batch_label}] [{status}] {fn} no doc found (expected {expected_doc})"
            failures.append(msg)
            if verbose:
                print(msg, file=sys.stderr)
            missing += 1
            continue
        declared = extract_functions_from_md(doc)
        if fn not in declared:
            status = "NAME_MISMATCH"
            mismatch = ",".join(sorted(declared))
            row = (fn, status, str(doc))
            rows.append(row)
            status_counts[status] = status_counts.get(status, 0) + 1
            msg = f"[batch={batch_label}] [{status}] {fn} missing declared function header/code reference in {doc} (found: {mismatch or '<none>'})"
            failures.append(msg)
            if verbose:
                print(msg, file=sys.stderr)
            missing += 1
            continue
        missing_sections = check_required_sections(doc)
        if missing_sections:
            missing_list = "|".join(missing_sections)
            status = "MISSING_SECTIONS"
            row = (fn, f"{status}:{missing_list}", str(doc))
            rows.append(row)
            status_counts[status] = status_counts.get(status, 0) + 1
            for section in missing_sections:
                missing_section_counts[section] += 1
            msg = f"[batch={batch_label}] [{status}] {fn} missing sections [{missing_list}] in {doc}"
            failures.append(msg)
            if verbose:
                print(msg, file=sys.stderr)
            missing += 1
            continue

        sources = extract_sources(doc)
        support = matrix_rows.get(fn, {"excel": "N", "sheets": "N"})
        source_issues = source_quality_issues(fn, sources, source_stats, used_urls, support)
        provider_issues = validate_provider_docs(doc, fn, support, sources)
        all_issues = list(source_issues) + list(provider_issues)
        if all_issues:
            status = "SOURCE_ISSUE"
            row = (fn, f"{status}:{'|'.join(sorted(set(all_issues)))}", str(doc))
            rows.append(row)
            status_counts[status] = status_counts.get(status, 0) + 1
            msg = f"[batch={batch_label}] [{status}] {fn} source/doc validation failed ({'|'.join(sorted(set(all_issues)))}) in {doc}"
            failures.append(msg)
            if verbose:
                print(msg, file=sys.stderr)
            missing += 1
            continue
        status = "OK"
        rows.append((fn, status, str(doc)))
        status_counts[status] = status_counts.get(status, 0) + 1

    # Flag extra docs not in matrix
    matrix_set = set(functions)
    for doc_name, doc_path in docs.items():
        if batch_filter and doc_name not in batch_filter:
            continue
        if doc_name not in matrix_set:
            status = "EXTRA_DOC"
            rows.append((doc_name, status, str(doc_path)))
            status_counts[status] = status_counts.get(status, 0) + 1

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["function_name", "status", "doc_path"])
        writer.writerows(rows)

    if not quiet:
        print(f"[SUMMARY] processed={len(rows)} missing_checks={missing}", file=sys.stderr)
        print(f"[SUMMARY] batch={batch_label} selected={len(batch_filter) if batch_filter else len(set(functions))}", file=sys.stderr)
    for status in sorted(status_counts):
        print(f"[SUMMARY] {status}={status_counts[status]}", file=sys.stderr)
    if used_urls:
        for (url, provider), names in sorted(used_urls.items()):
            if len(names) <= 1:
                continue
            # Flag suspicious URL reuse where the same source is used for more than one function.
            # A few shared pages are allowed, but this helps identify any missed per-function source links.
            normalized = normalize_source_url(url).lower()
            if normalized in {GENERIC_MS_FUNC_INDEX, GENERIC_MS_SOURCE, GENERIC_MS_ROOT, GENERIC_GS_FUNC_INDEX}:
                has_supported = any(
                    matrix_rows.get(fn, {"excel": "N", "sheets": "N"}).get(provider, "N") == "Y"
                    for fn in names
                )
                if has_supported:
                    status_counts["SOURCE_ISSUE"] = status_counts.get("SOURCE_ISSUE", 0) + 1
                    for fn in names:
                        failures.append(f"[batch={batch_label}] [SOURCE_ISSUE] {fn} shares generic source {url}")
                        missing += 1

    if missing_section_counts:
        print("[SUMMARY] missing_sections=", file=sys.stderr)
        for section in sorted(missing_section_counts):
            print(f"  - {section}: {missing_section_counts[section]}", file=sys.stderr)
    if source_stats:
        print("[SUMMARY] sources=", file=sys.stderr)
        for key in sorted(source_stats):
            print(f"  - {key}: {source_stats[key]}", file=sys.stderr)
    if failures:
        print("[DETAIL] failures:", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)

    if missing > 0:
        print(f"Validation failed: {missing} missing/mismatched functions", file=sys.stderr)
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
