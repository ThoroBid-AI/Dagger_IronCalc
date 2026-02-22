#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that Sheets oracle fixtures have non-empty expected_text, "
            "except for explicit visual-only exceptions."
        )
    )
    parser.add_argument(
        "--fixtures",
        default="fixtures",
        help="Fixtures root directory (default: fixtures)",
    )
    parser.add_argument(
        "--allow-empty",
        default="SPARKLINE",
        help=(
            "Comma-separated function names allowed to have empty expected_text "
            "(default: SPARKLINE)"
        ),
    )
    args = parser.parse_args()

    fixtures_root = Path(args.fixtures)
    allowed_empty = {name.strip().upper() for name in args.allow_empty.split(",") if name.strip()}

    failures: list[tuple[Path, str]] = []
    checked = 0
    allowed = 0

    for fixture_path in sorted(fixtures_root.rglob("*_sheets.json")):
        try:
            data = json.loads(fixture_path.read_text())
        except Exception as exc:
            failures.append((fixture_path, f"invalid JSON: {exc}"))
            continue

        if data.get("engine") != "sheets":
            continue

        checked += 1
        function_name = str(data.get("function") or fixture_path.parent.name).upper()
        expected_text = str(data.get("expected_text", ""))

        if expected_text:
            continue
        if function_name in allowed_empty:
            allowed += 1
            continue

        failures.append((fixture_path, "empty expected_text"))

    if failures:
        print("Sheets fixture expected_text validation failed:")
        for path, reason in failures:
            print(f"- {path}: {reason}")
        return 1

    print(
        "Sheets fixture expected_text validation passed "
        f"({checked} checked, {allowed} allowed-empty exceptions)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
