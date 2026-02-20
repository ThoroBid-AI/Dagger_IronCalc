# Specs Directory Guide

This directory contains specifications, coverage matrices, test pipelines, and reports.

## Structure
- `functions/`: Function behavior specs (authoritative). One file per function.
- `matrices/`: Coverage matrices (Excel, Sheets, IronCalc, HyperFormula).
- `pipelines/`: Oracle + conformance pipeline documentation.
- `planning/`: Implementation plans and backlogs (Lua workflow).
- `reports/`: Generated and tracking reports (see `reports/README.md`).
- `data/`: Legacy data files used by older tooling (optional).
- `lua_prompts.md`: Consolidated Lua implementation prompts for all functions.
- `unsupported_functions.md`: Known unsupported functions list.

## Notes
- Do not delete `functions/`, `matrices/`, `pipelines/`, or `planning/`.
- `reports/` contains generated outputs; keep unless explicitly cleaning.
