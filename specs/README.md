# Specs Directory Guide

This directory contains specifications, coverage matrices, test pipelines, and reports.

## Structure
- `functions/`: Function behavior specs (optional in this snapshot). One file per function when available.
- `matrices/`: Coverage matrices (Excel, Sheets, IronCalc, HyperFormula).
- `pipelines/`: Oracle + conformance pipeline documentation and runbooks.
- `planning/`: Implementation plans and backlogs (Lua workflow).
- `reports/`: Generated and tracking reports (see `reports/README.md`).
- `data/`: Legacy data files used by older tooling (optional).
- `lua_prompts.md`: Consolidated Lua implementation prompts for all functions.
- `unsupported_functions.md`: Known unsupported functions list.

## Notes
- Runtime execution target is Rust (`base` crate); `lua_prompts.md` is a planning/spec artifact.
- For the current Lua workflow, `lua_prompts.md` is the primary source for per-function behavior summaries.
- When `specs/functions/<FUNCTION>.md` exists, treat it as an additional detailed reference.
- Use `specs/planning/implementation_handoff_contract.md` when handing implementation to another LLM.
- Do not delete `functions/`, `matrices/`, `pipelines/`, or `planning/`.
- `reports/` contains generated outputs; keep unless explicitly cleaning.
