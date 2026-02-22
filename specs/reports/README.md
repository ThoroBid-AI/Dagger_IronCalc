# Reports Guide

This folder contains **generated reports** and **tracking files** used by the planning and coverage workflow.

## Generated Reports
These can be regenerated from scripts in `scripts/`.
- `hyperformula_missing.csv` (from `scripts/generate_hf_coverage_reports.py`)
- `hyperformula_vs_ironcalc.csv` (from `scripts/generate_hf_coverage_reports.py`)
- `ironcalc_missing_but_in_hf.csv` (from `scripts/generate_hf_coverage_reports.py`)
- `ironcalc_missing_but_in_hf_grouped.csv` (derived from the above)

Optional generated file:
- `function_impl_mapping.csv` (consumed by `scripts/generate_lua_prompts.py` when present)

## Tracking Files (manual/ongoing)
These are updated as part of workflow execution.
- `lua_backlog_status.csv` (progress tracker for Lua backlog)
- `oracle_capture_status.csv` (updated by `scripts/import_oracle_workbook.py`)

Sheets oracle note:
- `SPARKLINE` is tracked as a visual-only exception because Google Sheets export does not provide a stable scalar cell value for conformance assertions.

## Cleanup Policy
- Keep this folder clean: remove obsolete generated reports only after replacing them.
- Do not delete tracking files unless the workflow changes.
