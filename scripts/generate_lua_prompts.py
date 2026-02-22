#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "specs" / "matrices" / "function_matrix_normalized.csv"
IO_SHAPE = ROOT / "specs" / "data" / "function_io_shape.csv"
SPECS_DIR = ROOT / "specs" / "functions"
PROMPTS_DIR = ROOT / "specs" / "lua_prompts"
PROMPTS_MD = ROOT / "specs" / "lua_prompts.md"
IMPL_MAP = ROOT / "specs" / "reports" / "function_impl_mapping.csv"


SECTION_KEYS = {
    "purpose": "Purpose",
    "syntax": "Syntax",
    "behavior": "Behavior",
    "examples": "Examples",
    "examples (expected outputs)": "Examples",
    "error cases": "Error Cases",
    "notes": "Notes",
    "code location": "Code Location",
}


def load_matrix(path: Path) -> List[dict]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def load_io_shapes(path: Path) -> Dict[str, Tuple[List[str], List[str]]]:
    if not path.exists():
        return {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        shapes: Dict[str, Tuple[List[str], List[str]]] = {}
        for row in reader:
            func = row["function_name"].strip().upper()
            input_shape = row.get("input_shape", "").strip()
            output_shape = row.get("output_shape", "").strip()
            if func not in shapes:
                shapes[func] = ([], [])
            if input_shape and input_shape not in shapes[func][0]:
                shapes[func][0].append(input_shape)
            if output_shape and output_shape not in shapes[func][1]:
                shapes[func][1].append(output_shape)
        return shapes


def load_impl_map(path: Path) -> Dict[str, Tuple[str, str]]:
    if not path.exists():
        return {}

    def normalize_file_path(value: str) -> str:
        value = value.strip()
        if not value:
            return value
        root_prefix = f"{ROOT.as_posix()}/"
        if value.startswith(root_prefix):
            return value[len(root_prefix) :]
        for marker in ("/base/", "/xlsx/", "/bindings/", "/specs/", "/webapp/"):
            if marker in value:
                remainder = value.split(marker, 1)[1]
                return f"{marker.strip('/')}/{remainder}"
        return value

    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        out = {}
        for row in reader:
            func = row.get("function", "").strip().upper()
            handler = row.get("handler", "").strip()
            file_path = normalize_file_path(row.get("file_path", ""))
            if func:
                out[func] = (handler, file_path)
        return out


def strip_non_ascii(text: str) -> Tuple[str, bool]:
    ascii_text = text.encode("ascii", errors="ignore").decode("ascii")
    return ascii_text, ascii_text != text


def extract_sections(text: str) -> Dict[str, str]:
    lines = text.splitlines()
    current_key = None
    sections: Dict[str, List[str]] = {}

    for line in lines:
        m = re.match(r"^(#{2,3})\s+(.*)$", line.strip())
        if m:
            title = m.group(2).strip().lower()
            key = SECTION_KEYS.get(title)
            current_key = key
            if key and key not in sections:
                sections[key] = []
            continue
        if current_key:
            sections[current_key].append(line)

    out: Dict[str, str] = {}
    for key, content_lines in sections.items():
        content = "\n".join(content_lines).strip()
        out[key] = content
    return out


def format_section(title: str, content: str) -> str:
    if not content:
        return f"### {title}\n- Spec section missing.\n"
    return f"### {title}\n{content}\n"


def build_prompt(
    func: str,
    status: dict,
    io_shape: Tuple[List[str], List[str]],
    impl_info: Tuple[str, str] | None,
    spec_text: str | None,
    spec_path: Path | None,
) -> str:
    input_shapes, output_shapes = io_shape
    input_shape = ", ".join(input_shapes) if input_shapes else "unknown"
    output_shape = ", ".join(output_shapes) if output_shapes else "unknown"
    handler = impl_info[0] if impl_info else ""
    file_path = impl_info[1] if impl_info else ""

    missing_in_hf = "Yes" if status.get("missing_in_hf") else "No"
    missing_in_iron = "Yes" if status.get("missing_in_ironcalc") else "No"

    sections = extract_sections(spec_text) if spec_text else {}

    def safe_section(title: str) -> str:
        content = sections.get(title, "")
        if not content and spec_text:
            return f"### {title}\n- Not specified in spec.\n"
        if not content:
            return f"### {title}\n- Spec not found.\n"
        content_ascii, changed = strip_non_ascii(content)
        if changed:
            content_ascii += "\n\n- Note: Non-ASCII characters omitted. See spec for full text."
        return f"### {title}\n{content_ascii}\n"

    if spec_path:
        try:
            spec_ref = spec_path.relative_to(ROOT).as_posix()
        except ValueError:
            spec_ref = spec_path.as_posix()
    else:
        spec_ref = "Spec not found"

    prompt = (
        f"# {func} — Lua Implementation Prompt\n\n"
        "## Status\n"
        f"- IronCalc: {status.get('IronCalc')}\n"
        f"- Excel: {status.get('Excel')}\n"
        f"- Google Sheets: {status.get('GoogleSheets')}\n"
        f"- HyperFormula: {status.get('HyperFormula')}\n"
        f"- Missing in HyperFormula: {missing_in_hf}\n"
        f"- Missing in IronCalc: {missing_in_iron}\n"
        f"- IronCalc Handler: {handler or 'n/a'}\n"
        f"- IronCalc File: {file_path or 'n/a'}\n\n"
        "## IO Shape\n"
        f"- Input: {input_shape or 'unknown'}\n"
        f"- Output: {output_shape or 'unknown'}\n\n"
        "## Spec Summary\n"
        f"{safe_section('Purpose')}\n"
        f"{safe_section('Syntax')}\n"
        f"{safe_section('Behavior')}\n"
        f"{safe_section('Examples')}\n"
        f"{safe_section('Error Cases')}\n"
        f"{safe_section('Notes')}\n"
        f"{safe_section('Code Location')}\n"
        "## Implementation Checklist (Lua)\n"
        "- Parse and coerce arguments per Excel/Sheets semantics.\n"
        "- Implement error propagation and return codes exactly.\n"
        "- Respect array/range inputs based on IO shape.\n"
        "- Match numeric precision and rounding behavior.\n"
        "- Add tests that mirror spec examples and error cases.\n\n"
        f"## Reference\n- Spec file: {spec_ref}\n"
    )
    return prompt


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Lua implementation prompts per function.")
    parser.add_argument("--matrix", default=str(MATRIX), help="Normalized function matrix CSV")
    parser.add_argument("--io-shape", default=str(IO_SHAPE), help="IO shape CSV")
    parser.add_argument("--impl-map", default=str(IMPL_MAP), help="Function impl mapping CSV")
    parser.add_argument("--specs-dir", default=str(SPECS_DIR), help="Specs/functions directory")
    parser.add_argument(
        "--out-dir",
        default="",
        help="If set, write per-function prompt files to this directory",
    )
    parser.add_argument(
        "--single-md",
        default=str(PROMPTS_MD),
        help="Write a single consolidated markdown file (default enabled)",
    )
    args = parser.parse_args()

    matrix = load_matrix(Path(args.matrix))
    io_shapes = load_io_shapes(Path(args.io_shape))
    impl_map = load_impl_map(Path(args.impl_map))

    out_dir = Path(args.out_dir) if args.out_dir else None
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
    specs_dir = Path(args.specs_dir)
    single_md_path = Path(args.single_md) if args.single_md else None
    combined: List[str] = []

    if single_md_path:
        combined.append("# Lua Implementation Prompts (All Functions)\n")

    for row in matrix:
        func = row["Function"].strip()
        func_key = func.upper()
        spec_path = specs_dir / f"{func}.md"
        spec_text = spec_path.read_text(encoding="utf-8", errors="replace") if spec_path.exists() else None

        status = {
            "IronCalc": row.get("IronCalc", "N"),
            "Excel": row.get("Excel", "N"),
            "GoogleSheets": row.get("GoogleSheets", "N"),
            "HyperFormula": row.get("HyperFormula", "N"),
        }
        status["missing_in_hf"] = (
            status["HyperFormula"] != "Y"
            and (status["Excel"] == "Y" or status["GoogleSheets"] == "Y" or status["IronCalc"] == "Y")
        )
        status["missing_in_ironcalc"] = (
            status["IronCalc"] != "Y" and (status["Excel"] == "Y" or status["GoogleSheets"] == "Y")
        )

        io_shape = io_shapes.get(func_key, ([], []))
        impl_info = impl_map.get(func_key)

        prompt = build_prompt(func, status, io_shape, impl_info, spec_text, spec_path if spec_text else None)
        if out_dir:
            out_path = out_dir / f"{func}.md"
            out_path.write_text(prompt)

        if single_md_path:
            combined.append(prompt.replace("# ", "## ", 1))
            combined.append("\n---\n")

    if single_md_path:
        single_md_path.write_text("\n".join(combined))
        print(f"Wrote consolidated prompts to {single_md_path}")

    if out_dir:
        print(f"Wrote prompts to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
