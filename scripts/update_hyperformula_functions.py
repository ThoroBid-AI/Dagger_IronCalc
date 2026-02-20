#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import re
import sys
import urllib.request
from pathlib import Path
from typing import Iterable, List, Set


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URL = "https://hyperformula.handsontable.com/guide/built-in-functions.html"
DEFAULT_OUT = ROOT / "specs" / "matrices" / "hyperformula_functions.csv"


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; IronCalc-HF-List/1.0)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def normalize(name: str) -> str:
    name = name.strip()
    name = name.replace("\u00a0", " ")
    name = re.sub(r"\s+", " ", name)
    return name.upper()


def extract_functions(html_text: str) -> Set[str]:
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", html_text, flags=re.S | re.I)
    names: List[str] = []
    for row in rows:
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, flags=re.S | re.I)
        if not cells:
            continue
        first = html.unescape(re.sub(r"<[^>]+>", "", cells[0])).strip()
        if not first:
            continue
        if "function id" in first.lower():
            continue
        first = normalize(first)
        if re.fullmatch(r"[A-Z0-9_.]+", first):
            names.append(first)
    return set(names)


def write_csv(path: Path, funcs: Iterable[str], source: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["function_name", "source", "notes"])
        writer.writeheader()
        for name in sorted(set(funcs)):
            writer.writerow(
                {
                    "function_name": name,
                    "source": source,
                    "notes": "",
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch HyperFormula built-in functions and write a CSV list."
    )
    parser.add_argument("--source-url", default=DEFAULT_URL, help="HyperFormula docs URL")
    parser.add_argument("--source-html", help="Local HTML file (if provided, no fetch)")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Output CSV path")
    args = parser.parse_args()

    if args.source_html:
        html_text = Path(args.source_html).read_text(encoding="utf-8", errors="replace")
        source = f"file:{args.source_html}"
    else:
        html_text = fetch(args.source_url)
        source = args.source_url

    funcs = extract_functions(html_text)
    if not funcs:
        print("No functions extracted. Check source.", file=sys.stderr)
        return 1

    write_csv(Path(args.out), funcs, source)
    print(f"Wrote {len(funcs)} functions to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
