#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run oracle conformance fixtures against IronCalc.")
    parser.add_argument("--fixtures", default="fixtures", help="Fixture root directory")
    parser.add_argument("--report", default="specs/reports/conformance_report.csv", help="CSV report path")
    parser.add_argument("--engine", choices=["excel", "sheets"], help="Optional engine filter")
    args = parser.parse_args()

    fixtures = str(Path(args.fixtures))
    report = str(Path(args.report))

    if args.engine == "sheets":
        print(
            "Running Sheets conformance via Rust test harness (report output is not generated).",
            flush=True,
        )
        return subprocess.call(
            [
                "cargo",
                "test",
                "-p",
                "ironcalc_base",
                "sheets_oracle_fixtures_match_ironcalc",
                "--",
                "--nocapture",
            ]
        )

    cmd = [
        "cargo",
        "run",
        "-p",
        "ironcalc_base",
        "--bin",
        "conformance_runner",
        "--",
        "--fixtures",
        fixtures,
        "--report",
        report,
    ]
    if args.engine:
        cmd.extend(["--engine", args.engine])

    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
