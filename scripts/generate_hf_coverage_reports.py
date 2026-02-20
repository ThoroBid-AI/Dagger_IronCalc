#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "specs" / "matrices" / "function_matrix_normalized.csv"
REPORT_MISSING = ROOT / "specs" / "reports" / "hyperformula_missing.csv"
REPORT_COMPARE = ROOT / "specs" / "reports" / "hyperformula_vs_ironcalc.csv"
REPORT_PRIORITY = ROOT / "specs" / "reports" / "ironcalc_missing_but_in_hf.csv"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate HyperFormula coverage reports.")
    parser.add_argument("--matrix", default=str(MATRIX), help="Normalized function matrix CSV")
    parser.add_argument("--missing-out", default=str(REPORT_MISSING), help="Missing report CSV")
    parser.add_argument("--compare-out", default=str(REPORT_COMPARE), help="Comparison report CSV")
    parser.add_argument(
        "--priority-out",
        default=str(REPORT_PRIORITY),
        help="IronCalc missing but available in HyperFormula CSV",
    )
    args = parser.parse_args()

    matrix_path = Path(args.matrix)
    with matrix_path.open(newline="") as f:
        rows = list(csv.DictReader(f))

    missing_rows = []
    compare_rows = []
    priority_rows = []

    for row in rows:
        func = row["Function"]
        excel = row.get("Excel", "N")
        sheets = row.get("GoogleSheets", "N")
        iron = row.get("IronCalc", "N")
        hf = row.get("HyperFormula", "N")
        missing_in_hf = "Y" if hf != "Y" and (excel == "Y" or sheets == "Y" or iron == "Y") else "N"
        missing_in_iron = "Y" if iron != "Y" and (excel == "Y" or sheets == "Y") else "N"

        compare_rows.append(
            {
                "function_name": func,
                "excel": excel,
                "sheets": sheets,
                "ironcalc": iron,
                "hyperformula": hf,
                "missing_in_hf": missing_in_hf,
                "missing_in_ironcalc": missing_in_iron,
            }
        )

        if missing_in_hf == "Y":
            missing_rows.append(
                {
                    "function_name": func,
                    "excel": excel,
                    "sheets": sheets,
                    "ironcalc": iron,
                    "hyperformula": hf,
                }
            )

        if iron != "Y" and hf == "Y" and (excel == "Y" or sheets == "Y"):
            priority_rows.append(
                {
                    "function_name": func,
                    "excel": excel,
                    "sheets": sheets,
                    "ironcalc": iron,
                    "hyperformula": hf,
                }
            )

    missing_path = Path(args.missing_out)
    missing_path.parent.mkdir(parents=True, exist_ok=True)
    with missing_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["function_name", "excel", "sheets", "ironcalc", "hyperformula"]
        )
        writer.writeheader()
        writer.writerows(missing_rows)

    compare_path = Path(args.compare_out)
    compare_path.parent.mkdir(parents=True, exist_ok=True)
    with compare_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "function_name",
                "excel",
                "sheets",
                "ironcalc",
                "hyperformula",
                "missing_in_hf",
                "missing_in_ironcalc",
            ],
        )
        writer.writeheader()
        writer.writerows(compare_rows)

    print(f"Wrote {missing_path} ({len(missing_rows)} rows)")
    print(f"Wrote {compare_path} ({len(compare_rows)} rows)")
    priority_path = Path(args.priority_out)
    priority_path.parent.mkdir(parents=True, exist_ok=True)
    with priority_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["function_name", "excel", "sheets", "ironcalc", "hyperformula"]
        )
        writer.writeheader()
        writer.writerows(priority_rows)
    print(f"Wrote {priority_path} ({len(priority_rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
