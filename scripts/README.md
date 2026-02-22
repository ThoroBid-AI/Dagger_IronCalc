# Scripts Guide

This folder contains scripts for coverage, fixtures, and documentation workflows.

## Current Lua + HyperFormula Workflow
- `update_hyperformula_functions.py`
- `update_function_matrix.py`
- `generate_lua_prompts.py`
- `generate_hf_coverage_reports.py`

Note:
- `generate_lua_prompts.py` can enrich prompt metadata from `specs/reports/function_impl_mapping.csv` when that file exists, but it is optional.

## Legacy / Optional Workflows
These rely on files in `specs/data/` and older batch tooling:
- `generate_oracle_workbook.py`
- `import_oracle_workbook.py`
- `seed_batch_fixtures.py`
- `seed_fallbacks_from_batches.py`
- `update_batch_sources.py`
- `enrich_function_docs.py`
- `validate_function_docs.py`

Use legacy scripts only if you are running the older batch-based pipeline.
