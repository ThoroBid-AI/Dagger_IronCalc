# Reports Guide

This folder contains **generated reports** and **tracking files** used by the planning and coverage workflow.

## Generated Reports
These can be regenerated from scripts in `Dagger_IronCalc/scripts/`.
- `function_impl_mapping.csv` (from `scripts/map_function_impls.py`)
- `hyperformula_missing.csv` (from `scripts/generate_hf_coverage_reports.py`)
- `hyperformula_vs_ironcalc.csv` (from `scripts/generate_hf_coverage_reports.py`)
- `ironcalc_missing_but_in_hf.csv` (from `scripts/generate_hf_coverage_reports.py`)
- `ironcalc_missing_but_in_hf_grouped.csv` (derived from the above)

## Tracking Files (manual/ongoing)
These are updated as part of workflow execution.
- `lua_backlog_status.csv` (progress tracker for Lua backlog)
- `oracle_capture_status.csv` (updated by `scripts/import_oracle_workbook.py`)
- `function_unsupported_nimpl.csv` (current gap tracking)

## Cleanup Policy
- Keep this folder clean: remove obsolete generated reports only after replacing them.
- Do not delete tracking files unless the workflow changes.
