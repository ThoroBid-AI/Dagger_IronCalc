#!/usr/bin/env python3
import csv
import html
import re
import sys
import urllib.request
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "specs" / "matrices" / "function_matrix_normalized.csv"
BATCH_PATH = ROOT / "specs" / "data" / "function_batches.csv"
DOCS_DIR = ROOT / "specs" / "functions"
REPORT = ROOT / "specs" / "reports" / "batch_source_updates.csv"
EXCEL_INDEX = "https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188"
SHEETS_INDEX = "https://support.google.com/docs/table/25273?hl=en"
EXCEL_HOME = "https://support.microsoft.com/en-us/office"
SHEETS_HOME = "https://support.google.com/docs"

HARD_CODED_EXCEL_URLS = {
    "FORECAST": "https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99",
    "FORECAST.LINEAR": "https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99",
    "FORECAST.ETS": "https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41",
    "FORECAST.ETS.CONFINT": "https://support.microsoft.com/en-us/office/forecast-ets-confint-function-6d4a7557-11fa-4678-9e6a-dbcc31a7c7df",
    "FORECAST.ETS.SEASONALITY": "https://support.microsoft.com/en-us/office/forecast-ets-seasonality-function-32a27a3b-d22f-42ce-8c5d-ef3649269f3c",
    "FORECAST.ETS.STAT": "https://support.microsoft.com/en-us/office/forecast-ets-stat-function-60f2ae14-d0cf-465e-9736-625ccaaa60b4",
    "GAMMA.DIST": "https://support.microsoft.com/en-us/office/gamma-dist-function-9b6f1538-d11c-4d5f-8966-21f6a2201def",
    "ISBLANK": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISERR": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISERROR": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISLOGICAL": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISNA": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISNONTEXT": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISNUMBER": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISODD": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISREF": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
    "ISTEXT": "https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665",
}

REQUEST_PROFILES = [
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
    },
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
    },
    {
        "User-Agent": "Mozilla/5.0 (compatible; IronCalc-SourceMapper/1.1)",
    },
]
MAX_FETCH_ATTEMPTS = 4
RETRY_DELAYS_SECONDS = [0.5, 1.0, 2.0]

ANCHOR_RE = re.compile(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', re.I | re.S)
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.I | re.S)
TD_RE = re.compile(r"<td[^>]*>(.*?)</td>", re.I | re.S)


def normalize(name: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", name.upper())


def parse_batch_arg(argv: List[str]) -> str:
    for i, token in enumerate(argv):
        if token == "--batch" and i + 1 < len(argv):
            return argv[i + 1]
    return ""


def load_batch_functions(batch_id: str) -> Tuple[str, Set[str]]:
    functions: Set[str] = set()
    if not BATCH_PATH.exists():
        raise FileNotFoundError(f"Missing batch plan: {BATCH_PATH}")
    with BATCH_PATH.open(newline="") as f:
        rows = csv.DictReader(f)
        for row in rows:
            if row.get("batch_id") == batch_id:
                functions.add(row["function_name"].strip().upper())
    return batch_id, functions


def read_matrix() -> Dict[str, Dict[str, str]]:
    if not MATRIX_PATH.exists():
        raise FileNotFoundError(f"Missing matrix: {MATRIX_PATH}")
    matrix: Dict[str, Dict[str, str]] = {}
    with MATRIX_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            fn = row["Function"].strip().upper()
            matrix[fn] = {"excel": row.get("Excel", "N"), "sheets": row.get("GoogleSheets", row.get("Google", "N"))}
    return matrix


def build_request(url: str, profile: Dict[str, str]) -> urllib.request.Request:
    headers = dict(profile)
    headers.setdefault("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    headers.setdefault("Accept-Language", "en-US,en;q=0.9")
    headers.setdefault("Cache-Control", "no-cache")
    return urllib.request.Request(url, headers=headers)


def fetch(url: str, source: str, batch: str) -> str:
    last_error: Exception | None = None
    for attempt in range(1, MAX_FETCH_ATTEMPTS + 1):
        profile = REQUEST_PROFILES[min(attempt - 1, len(REQUEST_PROFILES) - 1)]
        req = build_request(url, profile)
        print(
            f"[batch={batch}] [source-attempt] source={source} attempt={attempt}/{MAX_FETCH_ATTEMPTS} url={url}",
            file=sys.stderr,
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                status = getattr(resp, "status", None)
                print(f"[batch={batch}] [source-ok] source={source} status={status or 'unknown'}", file=sys.stderr)
                return resp.read().decode("utf-8", errors="replace")
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            status = getattr(exc, "code", None)
            status_text = f"HTTP {status}" if isinstance(exc, HTTPError) else str(exc)
            print(
                f"[batch={batch}] [source-fail] source={source} attempt={attempt}/{MAX_FETCH_ATTEMPTS} "
                f"status={status_text} error={exc}",
                file=sys.stderr,
            )
        if attempt < MAX_FETCH_ATTEMPTS:
            time.sleep(RETRY_DELAYS_SECONDS[min(attempt - 1, len(RETRY_DELAYS_SECONDS) - 1)])

    raise RuntimeError(f"{source} fetch failed: {last_error}")


def parse_excel_links() -> Dict[str, str]:
    try:
        html_text = fetch(EXCEL_INDEX, "excel-index-en-us", "1")
    except Exception:
        # Some CDN edges intermittently block en-us locale. Fall back to en-gb path.
        html_text = fetch(EXCEL_INDEX.replace("en-us", "en-gb"), "excel-index-en-gb", "1")
    links: Dict[str, str] = {}
    for m in ANCHOR_RE.finditer(html_text):
        href = m.group(1).strip()
        name_html = m.group(2)
        name = html.unescape(re.sub(r"<[^>]+>", "", name_html)).strip().upper()
        if not name or not re.fullmatch(r"[A-Za-z0-9_. ]+", name):
            continue
        if "/office/" not in href or "-function-" not in href:
            continue
        url = href
        if href.startswith("/"):
            url = "https://support.microsoft.com" + href
        if name.startswith("FUNCTION ") or name.lower().startswith("functions "):
            continue
        links[normalize(name)] = url
    return links


def parse_sheets_links() -> Dict[str, str]:
    html_text = fetch(SHEETS_INDEX, "google-index", "1")
    links: Dict[str, str] = {}
    link_re = re.compile(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>', re.I)
    for row in ROW_RE.finditer(html_text):
        row_html = row.group(1)
        tds = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in TD_RE.findall(row_html)]
        if len(tds) < 2:
            continue
        raw_name = tds[1]
        if not raw_name:
            continue
        name = re.sub(r"\\s+", " ", raw_name).strip()
        if not re.fullmatch(r"[A-Z0-9_.]+", name, re.I):
            continue
        href = ""
        for m in link_re.finditer(row_html):
            candidate = m.group(1).strip()
            if "/docs/answer/" in candidate:
                href = candidate
                break
        if not href:
            continue
        if href.startswith("/"):
            href = "https://support.google.com" + href
        links[normalize(name)] = href
    return links


def load_docs(functions: Iterable[str]) -> Dict[str, Path]:
    docs: Dict[str, Path] = {}
    for name in functions:
        p = DOCS_DIR / f"{name}.md"
        if p.exists():
            docs[name] = p
    return docs


def replace_sources(lines: List[str], fn: str, excel_url: str, sheets_url: str) -> Tuple[List[str], bool]:
    updated = False
    out: List[str] = []
    in_sources = False
    has_excel = False
    has_sheets = False

    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith("## sources"):
            in_sources = True
            out.append(line)
            continue
        if in_sources and stripped.startswith("## "):
            in_sources = False
        if in_sources and stripped.lower().startswith("- excel:"):
            out.append(f"- Excel: {excel_url}\n")
            has_excel = True
            updated = True
            continue
        if in_sources and stripped.lower().startswith("- google sheets:"):
            out.append(f"- Google Sheets: {sheets_url}\n")
            has_sheets = True
            updated = True
            continue
        if in_sources:
            if stripped.startswith("-") and stripped.lstrip().lower().startswith("- ") and not has_excel:
                # keep any non-source lines but still continue scanning
                pass
        out.append(line)

    if not has_excel:
        insertion_idx = len(out)
        # place source lines before next section/end
        for i in range(len(out) - 1, -1, -1):
            if out[i].startswith("## Sources"):
                insertion_idx = i + 1
                break
        out.insert(insertion_idx, f"- Excel: {excel_url}\n")
        updated = True

    if not has_sheets:
        insertion_idx = len(out)
        for i in range(len(out) - 1, -1, -1):
            if out[i].startswith("## Sources"):
                insertion_idx = i + 1
                break
        out.insert(insertion_idx + (1 if not has_excel else 1), f"- Google Sheets: {sheets_url}\n")
        updated = True

    return out, updated


def main() -> int:
    batch = parse_batch_arg(sys.argv)
    if not batch:
        print("Missing --batch argument", file=sys.stderr)
        return 2

    print(f"Loading batch {batch}...")
    batch_label, batch_functions = load_batch_functions(batch)
    if not batch_functions:
        print(f"No functions in batch {batch}", file=sys.stderr)
        return 1

    matrix = read_matrix()
    excel_map = parse_excel_links()
    sheets_map = parse_sheets_links()
    doc_paths = load_docs(batch_functions)

    updates = []
    unresolved: List[Tuple[str, str]] = []
    for fn in sorted(batch_functions):
        doc = doc_paths.get(fn)
        if not doc:
            unresolved.append((fn, "MISSING_DOC"))
            continue

        row = matrix.get(fn, {"excel": "N", "sheets": "N"})
        excel_url = HARD_CODED_EXCEL_URLS.get(fn)
        if not excel_url:
            excel_url = excel_map.get(normalize(fn))
        sheets_url = sheets_map.get(normalize(fn))
        if row["excel"] != "Y":
            excel_url = f"{EXCEL_HOME}/" if not excel_url else excel_url
        if not excel_url:
            excel_url = "https://support.microsoft.com/en-us/office"
        if row["sheets"] != "Y":
            unsupported_suffix = quote(fn, safe="._")
            sheets_url = f"{SHEETS_HOME}/table/25273?hl=en&unsupported={unsupported_suffix}"
        elif not sheets_url:
            sheets_url = SHEETS_HOME
        if not sheets_url:
            sheets_url = SHEETS_HOME

        lines = doc.read_text().splitlines(keepends=True)
        new_lines, changed = replace_sources(lines, fn, excel_url, sheets_url)
        if changed:
            doc.write_text("".join(new_lines))
            updates.append((fn, "updated", str(doc)))
            print(f"[batch={batch_label}] UPDATED {fn}")
        else:
            updates.append((fn, "unchanged", str(doc)))
            print(f"[batch={batch_label}] UNCHANGED {fn}")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["batch", "function_name", "status", "doc_path"])
        for fn in sorted(batch_functions):
            row_status = "updated"
            if not (DOCS_DIR / f"{fn}.md").exists():
                row_status = "missing_doc"
            writer.writerow([batch_label, fn, row_status, str(DOCS_DIR / f"{fn}.md")])

    if unresolved:
        print(f"[SUMMARY] unresolved={len(unresolved)}", file=sys.stderr)
        for fn, reason in unresolved:
            print(f"  - {fn}: {reason}", file=sys.stderr)
        print("Batch source population incomplete.", file=sys.stderr)
        return 1
    print(f"Batch source population complete. Updated {sum(1 for _, st, _ in updates if st == 'updated')} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
