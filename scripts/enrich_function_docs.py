#!/usr/bin/env python3
import csv
import html
import re
import sys
import time
import urllib.request
from urllib.error import HTTPError, URLError
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "specs" / "matrices" / "function_matrix_normalized.csv"
BATCH_PATH = ROOT / "specs" / "planning" / "function_batches.csv"
DOCS_DIR = ROOT / "specs" / "functions"
REPORT = ROOT / "specs" / "reports" / "batch_doc_enrichment.csv"
VALIDATION_REPORT = ROOT / "specs" / "reports" / "function_doc_validation.csv"

SOURCE_LINE_RE = re.compile(r"^-\s*(excel|google\s*sheets)\s*:\s*(https?://\S+)\s*$", re.I)
HEADER_RE = re.compile(r"^##\s+Documentation\s*\(\s*(.*?)\s*\)\s*$", re.I)
META_RE = re.compile(r"<meta[^>]+>", re.I)
ATTR_RE = re.compile(r'([a-zA-Z0-9\-:]+)\s*=\s*"([^"]*)"')
HEADING_RE = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.I | re.S)
CODE_RE = re.compile(r"<code>(.*?)</code>", re.I | re.S)
BOLD_TAG_RE = re.compile(r"<(?:b|strong|em|i|code)[^>]*>(.*?)</(?:b|strong|em|i|code)>", re.I | re.S)
IMG_ALT_RE = re.compile(r"<img[^>]+alt=\"([^\"]+)\"[^>]*>", re.I | re.S)
IMG_ALT_SINGLE_RE = re.compile(r"<img[^>]+alt='([^']+)'[^>]*>", re.I | re.S)
TABLE_RE = re.compile(r"<table[^>]*>(.*?)</table>", re.I | re.S)
TABLE_ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.I | re.S)
TABLE_CELL_RE = re.compile(r"<t[hd][^>]*>(.*?)</t[hd]>", re.I | re.S)
SECTION_KEYWORDS = {
    "syntax": ("syntax",),
    "examples": ("example", "examples"),
    "remarks": ("remarks", "notes", "note"),
    "errors": ("error", "errors"),
    "return": ("return",),
    "remarks_compat": ("return", "remarks", "notes", "error"),
    "troubleshoot": ("troubleshoot", "common problems", "compatibility issues"),
}
MAX_FETCH_ATTEMPTS = 4
RETRY_DELAYS_SECONDS = [0.5, 1.0, 2.0]
PLACEHOLDER_SUMMARY_MARKERS = ("not captured from source.", "see source for more details", "source temporarily unavailable")
REQUEST_PROFILES = [
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
    {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
    {
        "User-Agent": "Mozilla/5.0 (compatible; IronCalc-DocEnricher/1.0)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
]


def parse_batch_arg(argv: List[str]) -> str:
    for i, token in enumerate(argv):
        if token == "--batch" and i + 1 < len(argv):
            return argv[i + 1]
    return "1"


def parse_offline_arg(argv: List[str]) -> bool:
    return "--offline" in argv


def parse_report_arg(argv: List[str]) -> bool:
    return "--from-report" in argv


def parse_report_path(argv: List[str]) -> Path | None:
    for i, token in enumerate(argv):
        if token == "--report" and i + 1 < len(argv):
            return Path(argv[i + 1])
    return None


def normalize(name: str) -> str:
    return re.sub(r"\s+", "", name.upper())


def extract_section(lines: List[str], heading: str) -> List[str]:
    target = heading.strip().lower()
    in_section = False
    out: List[str] = []
    for line in lines:
        current = line.strip().lower()
        if current.startswith("## "):
            if current == target:
                in_section = True
                continue
            if in_section:
                break
        if in_section:
            out.append(line)
    return out


def parse_signature_lines(lines: List[str], provider: str, fn: str) -> List[str]:
    provider_key = provider.strip().lower()
    out: List[str] = []
    fn_pat = re.escape(fn.lower())
    for raw in lines:
        text = raw.strip()
        if not text.startswith("-"):
            continue
        m = re.match(r"^-+\s*([^:]+)\s*:\s*(.+)$", text)
        if not m:
            continue
        key = m.group(1).strip().lower()
        if key != provider_key and "syntax" not in key and provider_key not in key:
            continue
        value = m.group(2).strip().strip("`")
        if not value:
            continue
        if re.search(rf"\b{fn_pat}\s*\(", value, flags=re.I):
            if value not in out:
                out.append(value)
        if len(out) >= 4:
            break
    return out


def parse_formula_lines(lines: List[str], fn: str) -> List[str]:
    fn_pat = re.escape(fn.lower())
    out: List[str] = []
    flat_text = " ".join(line.strip().lstrip("-").strip() for line in lines)
    for m in re.finditer(rf"\b{fn_pat}\s*\([^\)]{{0,260}}\)", flat_text, flags=re.I):
        value = m.group(0).strip()
        if value and value not in out:
            out.append(value)
            if len(out) >= 8:
                return out

    for raw in lines:
        text = raw.strip().lstrip("-").strip()
        if not text:
            continue
        m = re.search(rf"\b{fn_pat}\s*\([^\)]{{0,260}}\)", text, flags=re.I)
        if m:
            value = m.group(0).strip()
            if value not in out:
                out.append(value)
                if len(out) >= 8:
                    break
    return out


def _find_formula_examples(lines: List[str], fn: str, include_partial: bool = False) -> List[str]:
    out: List[str] = []
    fn_pat = re.escape(fn)
    for raw in lines:
        text = raw.strip().lstrip("-").strip()
        if not text:
            continue
        normalized = text.strip("`")
        if not normalized:
            continue
        if re.search(rf"\b{fn_pat}\s*\(", normalized, flags=re.I):
            out.append(normalized)
            if len(out) >= 8:
                break
        elif include_partial and re.search(rf"\b{fn_pat}\b", normalized, flags=re.I):
            out.append(normalized)
            if len(out) >= 8:
                break
    return out


def _looks_like_provider_summary(text: str) -> bool:
    lowered = text.lower()
    return (
        "not captured from source" in lowered
        or "no short description extracted" in lowered
        or "could not extract from source page" in lowered
        or "not available for this provider" in lowered
    )


def find_function_calls(text: str, fn: str, require_equals: bool = False, max_items: int = 8) -> List[str]:
    fn_esc = re.escape(fn)
    out: List[str] = []
    pattern = rf"\b{fn_esc}\s*\([^\n\r)]{{0,220}}\)"
    for line in text.splitlines():
        for m in re.finditer(pattern, line, flags=re.I):
            raw = m.group(0).strip("`").strip()
            if not raw:
                continue
            if require_equals and "=" not in line and not line.strip().startswith("="):
                continue
            if raw not in out:
                out.append(raw)
                if len(out) >= max_items:
                    return out
    return out


def parse_first_text(lines: List[str]) -> str:
    for raw in lines:
        text = raw.strip()
        if not text.startswith("-"):
            continue
        text = text.lstrip("-").strip()
        if text:
            return text
    return ""


def parse_first_nonempty(lines: List[str]) -> str:
    for raw in lines:
        text = raw.strip()
        if not text:
            continue
        text = text.lstrip("-").strip()
        if text:
            return text
    return ""


def read_matrix_functions(path: Path) -> Dict[str, Dict[str, str]]:
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


def load_batch_functions(batch_id: str) -> Set[str]:
    if not BATCH_PATH.exists():
        raise FileNotFoundError(f"Missing batch file: {BATCH_PATH}")
    functions: Set[str] = set()
    with BATCH_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            if row.get("batch_id") == batch_id:
                functions.add(normalize(row["function_name"]))
    return functions


def load_report_functions(report_path: Path) -> Set[str]:
    if not report_path.exists():
        raise FileNotFoundError(f"Missing report file: {report_path}")
    functions: Set[str] = set()
    with report_path.open(newline="") as f:
        for row in csv.DictReader(f):
            status = (row.get("status") or "").strip()
            if status.startswith("SOURCE_ISSUE"):
                fn = (row.get("function_name") or "").strip().upper()
                if fn:
                    functions.add(fn)
    return functions


def build_request(url: str, profile: Dict[str, str]) -> urllib.request.Request:
    headers = dict(profile)
    headers.setdefault("Accept-Language", "en-US,en;q=0.9")
    headers.setdefault("Cache-Control", "no-cache")
    headers.setdefault("Pragma", "no-cache")
    headers.setdefault("Referer", "https://www.google.com/")
    return urllib.request.Request(url, headers=headers)


def fetch(url: str, batch: str, fn: str, provider: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, MAX_FETCH_ATTEMPTS + 1):
        profile = REQUEST_PROFILES[min(attempt - 1, len(REQUEST_PROFILES) - 1)]
        req = build_request(url, profile)
        print(
            f"[batch={batch}] [fetch-attempt] provider={provider} fn={fn} attempt={attempt}/{MAX_FETCH_ATTEMPTS} "
            f"url={url}",
            file=sys.stderr,
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                status = getattr(resp, "status", None)
                print(
                    f"[batch={batch}] [fetch-ok] provider={provider} fn={fn} status={status or 'unknown'}",
                    file=sys.stderr,
                )
                return resp.read().decode("utf-8", errors="replace")
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            status = getattr(exc, "code", None)
            if isinstance(exc, HTTPError):
                status_text = f"HTTP {status}"
            elif isinstance(exc, URLError):
                status_text = exc.reason if isinstance(exc.reason, str) else exc.__class__.__name__
            else:
                status_text = exc.__class__.__name__
            print(
                f"[batch={batch}] [fetch-fail] provider={provider} fn={fn} attempt={attempt}/{MAX_FETCH_ATTEMPTS} "
                f"status={status_text} error={exc}",
                file=sys.stderr,
            )
        except Exception as exc:
            last_error = exc
            print(
                f"[batch={batch}] [fetch-fail] provider={provider} fn={fn} attempt={attempt}/{MAX_FETCH_ATTEMPTS} "
                f"error={exc.__class__.__name__}: {exc}",
                file=sys.stderr,
            )

        if attempt < MAX_FETCH_ATTEMPTS:
            delay = RETRY_DELAYS_SECONDS[min(attempt - 1, len(RETRY_DELAYS_SECONDS) - 1)]
            time.sleep(delay)

    raise RuntimeError(f"fetch_failed: {last_error}") if last_error else RuntimeError("fetch_failed")


def extract_sources(path: Path) -> Dict[str, str]:
    sources: Dict[str, str] = {}
    in_sources = False
    for line in path.read_text().splitlines():
        s = line.strip()
        if s.lower().startswith("## sources"):
            in_sources = True
            continue
        if in_sources and s.startswith("## "):
            in_sources = False
            continue
        if not in_sources:
            continue
        m = SOURCE_LINE_RE.match(s)
        if not m:
            continue
        key = m.group(1).lower().replace(" ", "_")
        sources[key] = m.group(2).strip()
    return sources


def parse_meta(html_text: str, key: str) -> str:
    for tag in META_RE.finditer(html_text):
        attrs = {name.lower(): value for name, value in ATTR_RE.findall(tag.group(0))}
        if attrs.get("name", "").lower() != key and attrs.get("property", "").lower() != key:
            continue
        content = attrs.get("content", "").strip()
        if content:
            return html.unescape(content)
    return ""


def decode_html(text: str) -> str:
    text = text.replace("<br/>", "\n").replace("<br>", "\n").replace("<br />", "\n")
    text = re.sub(r"<tr[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"</tr>", "\n", text, flags=re.I)
    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
    text = re.sub(r"</li>", "\n", text, flags=re.I)
    text = re.sub(r"</p>|</div>|</h[1-6]>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def extract_table_rows(table_html: str) -> List[List[str]]:
    rows: List[List[str]] = []
    for row_html in TABLE_ROW_RE.finditer(table_html):
        cells = []
        for cell in TABLE_CELL_RE.findall(row_html.group(1)):
            cell_text = decode_html(cell).strip()
            if cell_text:
                cells.append(cell_text)
            else:
                cells.append("")
        if cells:
            rows.append(cells)
    return rows


def extract_table_pairs(text: str, fn: str) -> List[str]:
    lower_fn = fn.lower()
    examples: List[str] = []
    for table_html in TABLE_RE.finditer(text):
        rows = extract_table_rows(table_html.group(1))
        if len(rows) < 2:
            continue
        headers = [h.strip().lower() for h in rows[0]]
        if not headers:
            continue
        if not any("formula" in h or "argument" in h or "description" in h for h in headers):
            # skip unrelated tables unless they look formula-heavy and include function calls.
            table_text = " ".join(" ".join(r).lower() for r in rows)
            if lower_fn not in table_text:
                continue
        for cells in rows[1:]:
            if not any(cells):
                continue
            if len(cells) >= 2 and any(cells[:2]):
                first = cells[0].strip()
                second = " | ".join(c.strip() for c in cells[1:]).strip(" |")
                if any(h in headers[0] for h in ("argument", "name")) and len(cells) >= 2:
                    item = f"{first}: {second}"
                else:
                    item = f"{first}: {second}"
                if item and item not in examples:
                    examples.append(item)
            elif cells:
                item = cells[0].strip()
                if item and item not in examples:
                    examples.append(item)
    return examples[:12]


def extract_table_formulas(text: str, fn: str) -> List[str]:
    fn_esc = re.escape(fn)
    formulas: List[str] = []
    for table_html in TABLE_RE.finditer(text):
        rows = extract_table_rows(table_html.group(1))
        if not rows:
            continue
        for cells in rows[1:]:
            for cell in cells:
                if not cell:
                    continue
                for match in re.finditer(rf"\b{fn_esc}\s*\([^\n\r)]{{0,220}}\)", cell, flags=re.I):
                    candidate = match.group(0).strip().strip("`").strip()
                    if candidate and candidate not in formulas:
                        formulas.append(candidate)
                        if len(formulas) >= 12:
                            return formulas
    return formulas


def extract_named_section_text(sections: List[Tuple[str, str]], title_terms: Iterable[str]) -> str:
    terms = {t.lower() for t in title_terms}
    for title, body in sections:
        if any(term in title.lower() for term in terms):
            decoded = decode_html(body)
            if decoded:
                return decoded
    return ""


def extract_problematic_error_lines(body_text: str, fn: str) -> List[str]:
    # Keep lines that include an error token or are likely argument/behavioral notes.
    errors: List[str] = []
    fn_esc = re.escape(fn)
    for line in decode_html(body_text).splitlines():
        text = line.strip()
        if not text:
            continue
        if re.search(rf"(^|[^A-Za-z0-9])#(N[/A]?[A-Z]+|DIV/0!|VALUE!|REF!|NAME!|NUM!|SPILL!|NULL!|ERR!)", text, re.I):
            errors.append(text)
            if len(errors) >= 8:
                break
            continue
        if re.search(rf"\b{fn_esc}\s*\(", text, flags=re.I):
            # Useful for notes that mention this function.
            if "example" not in text.lower() and "=" not in text and len(text) < 320:
                errors.append(text)
                if len(errors) >= 8:
                    break
    return errors


def extract_formula_examples(text: str, fn: str) -> List[str]:
    signatures = []
    fn_esc = re.escape(fn)
    for m in CODE_RE.finditer(text):
        snippet = decode_html(m.group(1))
        if "=" in snippet or re.search(rf"\b{fn_esc}\s*\(", snippet, flags=re.I):
            lines = [line.strip() for line in snippet.splitlines() if line.strip()]
            for line in lines:
                if line.startswith("=") or re.search(rf"\b{fn_esc}\s*\(", line, flags=re.I):
                    cleaned = line.strip().strip("`").strip()
                    if cleaned and cleaned not in signatures:
                        signatures.append(cleaned)
    for attr_re in (IMG_ALT_RE, IMG_ALT_SINGLE_RE):
        for m in attr_re.finditer(text):
            alt = html.unescape(m.group(1)).strip()
            if "=" in alt and fn.lower() in alt.lower() and re.search(rf"\b{fn}\b", alt, flags=re.I):
                if alt not in signatures:
                    signatures.append(alt)
    body_text = decode_html(text)
    for m in re.finditer(rf"(?<![A-Za-z0-9_])=\s*{fn_esc}\s*\([^\n\r]{{0,220}}\)", body_text, flags=re.I):
        snippet = m.group(0).strip()
        if snippet not in signatures:
            signatures.append(snippet)
    return signatures[:12]


def split_sections(html_text: str) -> List[Tuple[str, str]]:
    headings = list(HEADING_RE.finditer(html_text))
    if not headings:
        return []
    sections = []
    for idx, match in enumerate(headings):
        title = re.sub(r"<[^>]+>", "", match.group(2))
        title = html.unescape(title).strip().lower()
        start = match.end()
        end = headings[idx + 1].start() if idx + 1 < len(headings) else len(html_text)
        body = html_text[start:end]
        sections.append((title, body))
    return sections


def pick_section_html(sections: List[Tuple[str, str]], keywords: Iterable[str]) -> str:
    keywords_set = {k.lower() for k in keywords}
    for title, body in sections:
        if any(k in title for k in keywords_set):
            return body
    return ""


def pick_section_text(sections: List[Tuple[str, str]], keywords: Iterable[str]) -> str:
    keywords_set = {k.lower() for k in keywords}
    for title, body in sections:
        if any(k in title for k in keywords_set):
            cleaned = decode_html(body)
            if cleaned:
                return cleaned
    return ""


def extract_signatures(html_text: str, fn: str, sections: List[Tuple[str, str]]) -> List[str]:
    values: List[str] = []
    fn_esc = re.escape(fn)
    candidate_regions: List[str] = []
    syntax_section = pick_section_html(sections, SECTION_KEYWORDS["syntax"])
    if syntax_section:
        candidate_regions.append(syntax_section)
    return_section = pick_section_html(sections, SECTION_KEYWORDS["return"])
    if return_section:
        candidate_regions.append(return_section)
    candidate_regions.append(html_text)

    for region in candidate_regions:
        for m in BOLD_TAG_RE.finditer(region):
            fragment = decode_html(m.group(1)).replace("\n", " ").strip()
            if re.search(rf"^\(?\s*{fn_esc}\s*\(", fragment, flags=re.I):
                value = fragment.strip("`")
                if value and value not in values:
                    values.append(value)
                    if len(values) >= 5:
                        return values
        for m in CODE_RE.finditer(region):
            fragment = decode_html(m.group(1)).replace("\n", " ").strip()
            for m2 in re.finditer(rf"\b{fn_esc}\s*\([^\n\r)]{{0,220}}\)", fragment, flags=re.I):
                value = m2.group(0).strip()
                if value and value not in values:
                    values.append(value)
                    if len(values) >= 5:
                        return values
        if region is not html_text:
            continue
        body = decode_html(region)
        for m in re.finditer(
            rf"(?<![A-Za-z0-9_=]){fn_esc}\s*\([^\n\r=)]{{0,220}}\)",
            body,
            flags=re.I,
        ):
            value = m.group(0).strip()
            if value and value not in values:
                values.append(value)
                if len(values) >= 5:
                    return values
        for m in re.finditer(rf"\b{fn_esc}\s*\([^\n\r)]{{0,220}}\)", body, flags=re.I):
            value = m.group(0).strip()
            if value.startswith("="):
                continue
            if value and value not in values:
                values.append(value)
                if len(values) >= 5:
                    return values
        # Microsoft pages sometimes render signatures as plain text inside syntax section.
        for line in decode_html(region).splitlines():
            line = line.strip()
            if not line:
                continue
            # Allow `NAME (arg1, arg2)` or `NAME(arg1, arg2)`.
            for match in re.finditer(rf"\b{fn_esc}\s*\([^\n\r)]{{0,220}}\)", line, flags=re.I):
                value = match.group(0).strip("`").strip()
                if value and value not in values:
                    values.append(value)
                    if len(values) >= 5:
                        return values
            # Fallback for headings like "VLOOKUP (lookup_value, ...)"
            match = re.search(rf"\b{fn_esc}\s*\([^\n\r)]{{0,220}}\)", line, flags=re.I)
            if match:
                value = match.group(0).strip()
                if value not in values:
                    values.append(value)
                    if len(values) >= 5:
                        return values

    for v in extract_table_pairs(html_text, fn):
        if "(" in v and ")" in v and fn.lower() in v.lower() and len(values) < 5:
            match = re.search(rf"\b{fn_esc}\s*\([^\)]{{0,220}}\)", v, flags=re.I)
            if match:
                candidate = match.group(0).strip()
                if candidate and candidate not in values:
                    values.append(candidate)

    if not values:
        return []
    return values


def extract_examples_text(html_text: str, fn: str) -> str:
    sections = split_sections(html_text)
    examples: List[str] = []

    for title, body in sections:
        if "example" in title:
            examples.extend(extract_formula_examples(body, fn))
            examples.extend(extract_table_formulas(body, fn))
            table_pairs = extract_table_pairs(body, fn)
            for pair in table_pairs[:8]:
                if len(pair) > 1:
                    examples.append(pair)
            if examples:
                return "Examples: " + " | ".join(str(item) for item in examples[:8])
            decoded = decode_html(body)
            plain_calls = find_function_calls(decoded, fn)
            if plain_calls:
                examples.extend(plain_calls)
            if examples:
                return "Examples: " + " | ".join(str(item) for item in examples[:8])

    # Microsoft and Google pages sometimes only include formulas in later sections.
    body_text = decode_html(html_text)
    plain_calls = find_function_calls(body_text, fn, max_items=12)
    if plain_calls:
        return "Examples: " + " | ".join(plain_calls[:10])

    if fn in html_text.upper():
        fallback_examples = extract_formula_examples(html_text, fn)
        if fallback_examples:
            return "Examples: " + " | ".join(fallback_examples[:10])
        table_formulas = extract_table_formulas(html_text, fn)
        if table_formulas:
            return "Examples: " + " | ".join(table_formulas[:10])
        fallback_tables = extract_table_pairs(html_text, fn)
        if fallback_tables:
            return "Examples: " + " | ".join(str(item) for item in fallback_tables[:8])
    return ""


def extract_error_section_text(sections: List[Tuple[str, str]], fn: str) -> str:
    error_terms = ("troubleshoot", "common problems", "possible error", "error", "errors", "tips")
    collected: List[str] = []
    for title, body in sections:
        if any(term in title.lower() for term in error_terms):
            collected.extend(extract_problematic_error_lines(body, fn))
            if len(collected) >= 8:
                break
    if collected:
        return " | ".join(dict.fromkeys(collected))
    return ""


def summarize(text: str, max_len: int = 650) -> str:
    clean = " ".join(text.split())
    if not clean:
        return "Not captured from source."
    return clean if len(clean) <= max_len else clean[:max_len].rstrip() + "…"


def examples_include_fn(examples: List[str], fn: str) -> bool:
    fn_esc = re.escape(fn)
    for example in examples:
        if re.search(rf"\b{fn_esc}\s*\(", example, flags=re.I):
            return True
    return False


def section_for_provider(
    provider: str,
    fn: str,
    url: str,
    html_text: str,
    matrix_available: bool,
    fetch_error: str | None = None,
    fallback_summary: str | None = None,
    fallback_signatures: List[str] | None = None,
    fallback_examples: List[str] | None = None,
    fallback_notes: str | None = None,
    fallback_errors: str | None = None,
) -> List[str]:
    if "unsupported" in url:
        return [
            f"## Documentation ({provider})",
            "",
            f"- Source URL: {url}",
            "- Summary: Function is not present in the provider's function index for this batch.",
            "- Signatures: Not available for this provider.",
            "- Examples: Not available for this provider.",
            "- Notes: Use provider compatibility layer only when a canonical equivalent exists.",
            "",
        ]

    if fetch_error:
        summary = fallback_summary or summarize(
            fallback_notes or (fallback_examples[0] if fallback_examples else "Source temporarily unavailable.")
        )
        signatures = fallback_signatures or []
        examples = fallback_examples or []
        notes = fallback_notes or "Source temporarily unavailable. Use local documentation details only."
        errors = fallback_errors or "See source for provider-specific behavior details."
        lines = [
            f"## Documentation ({provider})",
            "",
            f"- Source URL: {url}",
            f"- Source fetch status: failed after {MAX_FETCH_ATTEMPTS} attempts",
            f"- Summary: {summary}",
        ]
        if signatures:
            lines.append("- Signatures:")
            for sig in signatures[:4]:
                lines.append(f"  - `{sig}`")
        else:
            lines.append("- Signatures: No signatures available for this function.")

        if examples:
            lines.append("- Examples:")
            for example in examples[:6]:
                lines.append(f"  - {summarize(example, 240)}")
        else:
            lines.append("- Examples: No examples available for this function.")

        lines.append(f"- Notes: {summarize(notes)}")
        lines.append(f"- Error behavior: {summarize(errors)}")
        lines.append("")
        return lines

    summary = summarize(parse_meta(html_text, "description"))
    if not summary:
        meta_desc = parse_meta(html_text, "og:description")
        summary = summarize(meta_desc) if meta_desc else "No short description extracted."
    if _looks_like_provider_summary(summary) and fallback_summary:
        summary = summarize(fallback_summary)

    sections = split_sections(html_text)
    syntax_raw = pick_section_html(sections, SECTION_KEYWORDS["syntax"])
    if not syntax_raw:
        syntax_raw = pick_section_html(sections, SECTION_KEYWORDS["return"])
    examples_raw = pick_section_text(sections, SECTION_KEYWORDS["examples"]) or extract_examples_text(html_text, fn)
    if fallback_examples:
        has_formula = bool(_find_formula_examples(examples_raw.split(" | ") if examples_raw else [], fn))
        if not has_formula:
            fallback_candidate = _find_formula_examples(
                ["- " + item for item in fallback_examples], fn, include_partial=True
            )
            if fallback_candidate:
                examples_raw = "Examples: " + " | ".join(fallback_candidate)

    remarks_raw = pick_section_text(sections, SECTION_KEYWORDS["remarks"]) or pick_section_text(
        sections, SECTION_KEYWORDS["remarks_compat"]
    )
    errors_raw = pick_section_text(sections, SECTION_KEYWORDS["errors"]) or extract_error_section_text(sections, fn)
    if not errors_raw:
        errors_raw = extract_named_section_text(
            sections, SECTION_KEYWORDS["troubleshoot"]
        )
    table_pairs = extract_table_pairs(html_text, fn)

    signatures = extract_signatures(syntax_raw or html_text, fn, sections)
    if not matrix_available:
        # keep deterministic message when function marked unavailable at matrix level.
        signatures = ["Not implemented for this provider per matrix metadata."]
    elif not signatures and fallback_signatures:
        signatures = fallback_signatures
    if not signatures and fallback_summary:
        if provider.lower().startswith("microsoft"):
            signatures = [line.strip("`").strip() for line in _find_formula_examples([f"`{fallback_summary}`"], fn)]
        elif fallback_signatures:
            signatures = fallback_signatures


    lines = [f"## Documentation ({provider})", "", f"- Source URL: {url}", f"- Summary: {summary}"]
    if signatures:
        lines.append("- Signatures:")
        for sig in signatures[:4]:
            lines.append(f"  - `{sig}`")
    else:
        lines.append("- Signatures: No signature captured from source page or local syntax.")

    if examples_raw:
        if "Examples:" in examples_raw:
            # `extract_examples_text` may return structured items already.
            examples_lines = [part.strip() for part in examples_raw.replace("Examples: ", "", 1).split(" | ")]
            lines.append("- Examples:")
            if not examples_include_fn(examples_lines, fn) and signatures:
                for sig in signatures:
                    if sig not in examples_lines:
                        examples_lines.append(sig)
            for example in examples_lines:
                if example:
                    lines.append(f"  - {summarize(example, 240)}")
        else:
            if not examples_include_fn([examples_raw], fn) and signatures:
                lines.append("- Examples:")
                for sig in signatures[:6]:
                    lines.append(f"  - {summarize(sig, 240)}")
            else:
                lines.append(f"- Examples: {summarize(examples_raw)}")
    else:
        if fallback_examples:
            lines.append("- Examples:")
            for example in fallback_examples[:6]:
                lines.append(f"  - {summarize(example, 240)}")
        else:
            example_lines = [sig.strip("`").strip() for sig in signatures if "(" in sig and ")" in sig]
            if example_lines:
                lines.append("- Examples:")
                for example in example_lines[:6]:
                    lines.append(f"  - {summarize(example, 240)}")
            else:
                lines.append("- Examples: No examples captured from source page or local docs.")

    if remarks_raw:
        lines.append(f"- Notes: {summarize(remarks_raw)}")
    else:
        if table_pairs:
            notes = summarize(" | ".join(table_pairs[:4]))
            if notes and notes != "Not captured from source.":
                lines.append(f"- Notes: {notes}")
            else:
                lines.append(f"- Notes: {summarize(fallback_notes or 'See source link for provider-specific behavior details.')}")
        else:
            lines.append(f"- Notes: {summarize(fallback_notes or 'See source link for provider-specific behavior details.')}")
    if errors_raw:
        lines.append(f"- Error behavior: {summarize(errors_raw)}")
    else:
        if fallback_errors:
            lines.append(f"- Error behavior: {fallback_errors}")
        else:
            lines.append("- Error behavior: Not explicitly documented on source page.")

    lines.append("")
    if not matrix_available:
        lines.append("- Compatibility note: Function is not listed as supported for this provider in the shared matrix.")
        lines.append("")
    return lines


def upsert_section(lines: List[str], heading: str, replacement: List[str]) -> List[str]:
    target = heading.strip().lower()
    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip().lower() == target:
            start = i
            continue
        if start is not None and line.startswith("## "):
            end = i
            break
    if start is None:
        # Insert before Sources so it sits near provenance metadata.
        insert_at = len(lines)
        for i, line in enumerate(lines):
            if line.strip().lower() == "## sources":
                insert_at = i
                break
        return lines[:insert_at] + [line + "\n" for line in replacement] + lines[insert_at:]

    if end is None:
        end = len(lines)
    return lines[:start] + [line + "\n" for line in replacement] + lines[end:]


def load_matrix_row(matrix: Dict[str, Dict[str, str]], fn: str) -> Tuple[str, str]:
    row = matrix.get(fn, {"excel": "N", "sheets": "N"})
    return row["excel"], row["sheets"]


def main() -> int:
    batch = parse_batch_arg(sys.argv)
    offline = parse_offline_arg(sys.argv)
    use_report = parse_report_arg(sys.argv)
    report_path = parse_report_path(sys.argv)
    batch_label = "REPORT" if use_report else batch
    print(f"[batch={batch_label}] Starting documentation enrichment...")
    try:
        if use_report:
            report_source = report_path or VALIDATION_REPORT
            batch_functions = load_report_functions(report_source)
        else:
            batch_functions = load_batch_functions(batch)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    if not batch_functions:
        print(f"No functions found for batch {batch_label}", file=sys.stderr)
        return 1

    try:
        matrix = read_matrix_functions(MATRIX_PATH)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    rows: List[Tuple[str, str, str]] = []
    updated = 0
    missing = 0

    for fn in sorted(batch_functions):
        doc = DOCS_DIR / f"{fn}.md"
        if not doc.exists():
            rows.append((fn, "MISSING_DOC", str(doc)))
            missing += 1
            print(f"[batch={batch}] [MISS] {fn} no doc")
            continue

        excel_row, sheets_row = load_matrix_row(matrix, fn)
        sources = extract_sources(doc)

        excel_url = sources.get("excel", "https://support.microsoft.com/en-us/office")
        sheets_url = sources.get("google_sheets", "https://support.google.com/docs")
        doc_lines = doc.read_text().splitlines()
        syntax_section = extract_section(doc_lines, "## syntax")
        examples_section = extract_section(doc_lines, "## examples (expected outputs)")
        notes_section = extract_section(doc_lines, "## notes")
        errors_section = extract_section(doc_lines, "## error cases")
        purpose_section = extract_section(doc_lines, "## purpose")
        fallback_signatures_ms = parse_signature_lines(syntax_section, "excel", fn)
        fallback_signatures_gs = parse_signature_lines(syntax_section, "google sheets", fn)
        fallback_examples = parse_formula_lines(examples_section, fn)
        fallback_notes = parse_first_text(notes_section)
        fallback_errors = parse_first_text(errors_section)
        fallback_summary = parse_first_nonempty(purpose_section) or parse_first_text(purpose_section)

        print(f"[batch={batch_label}] [FN] {fn}")
        provider_sections: List[List[str]] = []

        for provider, url, avail in (
            ("Microsoft", excel_url, excel_row == "Y"),
            ("Google Sheets", sheets_url, sheets_row == "Y"),
        ):
            print(f"  [SOURCE] {provider}: {url}")
            if "unsupported" in url and (not avail):
                provider_section = section_for_provider(
                    provider, fn, url, "", False, None, fallback_signatures_ms if provider == "Microsoft" else fallback_signatures_gs, fallback_examples, fallback_notes, fallback_errors
                )
            elif offline:
                provider_section = section_for_provider(
                    provider,
                    fn,
                    url,
                    "",
                    avail,
                    fetch_error="offline mode; no external fetch",
                    fallback_summary=fallback_summary,
                    fallback_signatures=fallback_signatures_ms if provider == "Microsoft" else fallback_signatures_gs,
                    fallback_examples=fallback_examples,
                    fallback_notes=fallback_notes,
                    fallback_errors=fallback_errors,
                )
            else:
                try:
                    html_text = fetch(url, batch=batch_label, fn=fn, provider=provider)
                    provider_section = section_for_provider(
                        provider,
                        fn,
                        url,
                        html_text,
                        avail,
                        fallback_summary=fallback_summary,
                        fallback_signatures=fallback_signatures_ms if provider == "Microsoft" else fallback_signatures_gs,
                        fallback_examples=fallback_examples,
                        fallback_notes=fallback_notes,
                        fallback_errors=fallback_errors,
                    )
                except Exception as exc:
                    msg = f"fetch_failed: {exc}"
                    provider_section = section_for_provider(
                        provider,
                        fn,
                        url,
                        "",
                        False,
                        msg,
                        fallback_summary=fallback_summary,
                        fallback_signatures=fallback_signatures_ms if provider == "Microsoft" else fallback_signatures_gs,
                        fallback_examples=fallback_examples,
                        fallback_notes=fallback_notes,
                        fallback_errors=fallback_errors,
                    )
            provider_sections.append(provider_section)

        lines = doc.read_text().splitlines()
        updated_doc = lines
        for section in provider_sections:
            heading = section[0]
            replacement = section
            updated_doc = upsert_section(updated_doc, heading, replacement)

        doc.write_text("\n".join(updated_doc).rstrip() + "\n")
        rows.append((fn, "UPDATED", str(doc)))
        updated += 1
        print(f"[batch={batch_label}] [OK] {fn} enriched")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["batch", "function_name", "status", "doc_path"])
        for fn, status, path in rows:
            w.writerow([batch_label, fn, status, path])

    print(f"[batch={batch_label}] Enrichment complete. updated={updated} missing={missing}")
    if missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
