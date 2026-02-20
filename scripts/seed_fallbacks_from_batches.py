#!/usr/bin/env python3
import csv
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
BATCHES_CSV = ROOT / "specs" / "planning" / "function_batches.csv"
FALLBACKS_CSV = ROOT / "specs" / "pipelines" / "function_fallbacks.csv"
LANGUAGE_JSON = ROOT / "base" / "src" / "language" / "language.json"
IMPL_MAPPING_CSV = ROOT / "specs" / "reports" / "function_impl_mapping.csv"

DEFAULT_HEADER = [
    "batch_id",
    "function_name",
    "action",
    "target",
    "min_args",
    "max_args",
    "test_cell",
    "test_formula",
    "expected_text",
    "setup",
    "test_cell_2",
    "test_formula_2",
    "expected_text_2",
    "setup_2",
    "implemented_in_code",
    "handler",
    "file_path",
]


def read_batches() -> List[Dict[str, str]]:
    if not BATCHES_CSV.exists():
        raise SystemExit(f"Missing batch list: {BATCHES_CSV}")
    with BATCHES_CSV.open(newline="") as f:
        return list(csv.DictReader(f))


def read_fallbacks() -> (List[str], List[Dict[str, str]]):
    if not FALLBACKS_CSV.exists():
        return DEFAULT_HEADER, []
    with FALLBACKS_CSV.open(newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or DEFAULT_HEADER
        for column in DEFAULT_HEADER:
            if column not in header:
                header.append(column)
        return header, list(reader)


def normalize_name(name: str) -> str:
    return name.replace(".", "").replace("_", "").upper()


def read_language_functions() -> set:
    if not LANGUAGE_JSON.exists():
        raise SystemExit(f"Missing language file: {LANGUAGE_JSON}")
    import json

    data = json.loads(LANGUAGE_JSON.read_text())
    functions = data["en"]["functions"].values()
    return {normalize_name(name) for name in functions}


def read_impl_mapping() -> dict:
    if not IMPL_MAPPING_CSV.exists():
        raise SystemExit(f"Missing impl mapping: {IMPL_MAPPING_CSV}")
    with IMPL_MAPPING_CSV.open(newline="") as f:
        rows = list(csv.DictReader(f))
    mapping = {}
    for row in rows:
        func = (row.get("function") or "").strip()
        if not func:
            continue
        mapping[normalize_name(func)] = row
    return mapping


def main() -> int:
    batches = read_batches()
    header, existing_rows = read_fallbacks()
    language_funcs = read_language_functions()
    impl_mapping = read_impl_mapping()

    existing_by_name = {
        row["function_name"]: row for row in existing_rows if row.get("function_name")
    }
    seen = set()
    merged: List[Dict[str, str]] = []

    for row in batches:
        name = row.get("function_name", "").strip()
        if not name:
            continue
        batch_id = row.get("batch_id", "").strip()
        seen.add(name)
        if name in existing_by_name:
            merged_row = existing_by_name[name]
            if batch_id:
                merged_row["batch_id"] = batch_id
            current_action = (merged_row.get("action") or "").strip()
            if current_action in ("", "implemented", "unimplemented"):
                if normalize_name(name) in language_funcs:
                    merged_row["action"] = "implemented"
                else:
                    merged_row["action"] = "unimplemented"
            impl_row = impl_mapping.get(normalize_name(name))
            if impl_row:
                merged_row["implemented_in_code"] = "yes"
                merged_row["handler"] = impl_row.get("handler", "")
                merged_row["file_path"] = impl_row.get("file_path", "")
            else:
                merged_row["implemented_in_code"] = "no"
            merged.append(merged_row)
        else:
            default_action = (
                "implemented" if normalize_name(name) in language_funcs else "unimplemented"
            )
            impl_row = impl_mapping.get(normalize_name(name))
            merged.append(
                {
                    "batch_id": batch_id,
                    "function_name": name,
                    "action": default_action,
                    "target": "",
                    "min_args": "",
                    "max_args": "",
                    "test_cell": "",
                    "test_formula": "",
                    "expected_text": "",
                    "setup": "",
                    "test_cell_2": "",
                    "test_formula_2": "",
                    "expected_text_2": "",
                    "setup_2": "",
                    "implemented_in_code": "yes" if impl_row else "no",
                    "handler": (impl_row or {}).get("handler", ""),
                    "file_path": (impl_row or {}).get("file_path", ""),
                }
            )

    # Preserve any fallback rows that are not in the batch list.
    for row in existing_rows:
        name = row.get("function_name", "").strip()
        if name and name not in seen:
            impl_row = impl_mapping.get(normalize_name(name))
            if impl_row:
                row["implemented_in_code"] = "yes"
                row["handler"] = impl_row.get("handler", "")
                row["file_path"] = impl_row.get("file_path", "")
            else:
                row["implemented_in_code"] = "no"
            merged.append(row)

    FALLBACKS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with FALLBACKS_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in merged:
            writer.writerow({key: row.get(key, "") for key in header})

    print(f"Wrote {FALLBACKS_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
