#!/usr/bin/env python3
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_RS = ROOT / "base" / "src" / "functions" / "mod.rs"
FUNCS_DIR = ROOT / "base" / "src" / "functions"
REPORT = ROOT / "specs" / "reports" / "function_impl_mapping.csv"
LOG = ROOT / "specs" / "reports" / "function_impl_mapping.log"

MATCH_RE = re.compile(r"Function::([A-Za-z0-9_]+)\s*=>\s*self\.([A-Za-z0-9_]+)\(")
FN_RE = re.compile(r"\bfn\s+([A-Za-z0-9_]+)\s*\(")
MACRO_RE = re.compile(r"\b[A-Za-z0-9_]+!\(\s*(fn_[A-Za-z0-9_]+)")


def load_handlers() -> dict:
    if not MOD_RS.exists():
        raise FileNotFoundError(f"Missing {MOD_RS}")
    handlers = {}
    text = MOD_RS.read_text()
    for m in MATCH_RE.finditer(text):
        func = m.group(1)
        handler = m.group(2)
        handlers[func] = handler
    return handlers


def index_function_defs() -> dict:
    defs = {}
    for path in FUNCS_DIR.rglob("*.rs"):
        text = path.read_text()
        for m in FN_RE.finditer(text):
            name = m.group(1)
            defs.setdefault(name, path)
        for m in MACRO_RE.finditer(text):
            name = m.group(1)
            defs.setdefault(name, path)
    return defs


def main() -> int:
    try:
        handlers = load_handlers()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    defs = index_function_defs()

    log_lines = []
    log_lines.append(f"Loaded handlers: {len(handlers)}")
    log_lines.append(f"Indexed definitions: {len(defs)}")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["function", "handler", "file_path"])
        missing = 0
        for func in sorted(handlers):
            handler = handlers[func]
            path = defs.get(handler)
            if not path:
                missing += 1
                log_lines.append(f"Missing handler location: Function::{func} -> {handler} (not found in {FUNCS_DIR})")
            w.writerow([func, handler, str(path) if path else ""])

    LOG.write_text("\n".join(log_lines) + "\n")

    if missing:
        print(f"Mapping complete with {missing} missing handler locations. See {LOG}", file=sys.stderr)
        return 1
    print(f"Mapping complete. Log written to {LOG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
