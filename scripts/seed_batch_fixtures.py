#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
BATCH_CSV = ROOT / "specs" / "data" / "function_batches.csv"


def parse_batches(raw: str) -> List[int]:
    batches: List[int] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s.strip())
            end = int(end_s.strip())
            if start > end:
                start, end = end, start
            batches.extend(range(start, end + 1))
        else:
            batches.append(int(part))
    seen = set()
    out = []
    for b in batches:
        if b not in seen:
            seen.add(b)
            out.append(b)
    return out


def load_batch_functions(batch_ids: Iterable[int]) -> List[str]:
    wanted = set(batch_ids)
    funcs: List[str] = []
    with BATCH_CSV.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["batch_id"]) in wanted:
                funcs.append(row["function_name"])
    return funcs


def make_fixture(function: str, engine: str) -> Dict:
    case_id = function.lower().replace(".", "_") + "_basic"
    version = "Excel 365 (manual)" if engine == "excel" else "Google Sheets (manual)"
    formula = f"={function}(1)"
    return {
        "engine": engine,
        "version": version,
        "locale": "en-US",
        "function": function,
        "case_id": case_id,
        "inputs": [],
        "formula": formula,
        "target": "Sheet1!A1",
        "expected_text": "",
        "notes": "TODO: capture oracle output",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed oracle fixtures for batches.")
    parser.add_argument(
        "--batches",
        required=True,
        help="Comma-separated batch list or ranges (e.g. 2-4,6).",
    )
    parser.add_argument(
        "--fixtures",
        default=str(ROOT / "fixtures"),
        help="Fixtures root directory",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing fixtures",
    )
    args = parser.parse_args()

    batch_ids = parse_batches(args.batches)
    functions = load_batch_functions(batch_ids)
    if not functions:
        print(f"No functions found for batches {batch_ids}")
        return 1

    fixtures_root = Path(args.fixtures)
    created = 0
    skipped = 0

    for function in functions:
        func_dir = fixtures_root / function
        func_dir.mkdir(parents=True, exist_ok=True)
        for engine in ("excel", "sheets"):
            filename = f"{function.lower().replace('.', '_')}_basic_{engine}.json"
            path = func_dir / filename
            if path.exists() and not args.overwrite:
                skipped += 1
                continue
            fixture = make_fixture(function, engine)
            path.write_text(json.dumps(fixture, indent=2) + "\n")
            created += 1

    print(f"Created fixtures: {created}")
    if skipped:
        print(f"Skipped existing: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
