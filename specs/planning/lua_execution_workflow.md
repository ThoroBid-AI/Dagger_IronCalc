# Lua Execution Workflow (Planning Only)

This document defines the end-to-end workflow for implementing functions in Lua without performing any implementation yet. It is the single execution guide to follow once we begin coding.

## 1) Inputs (Authoritative Sources)
Use these files only:
- Coverage matrix: `specs/matrices/function_matrix_normalized.csv`
- HyperFormula list: `specs/matrices/hyperformula_functions.csv`
- HyperFormula metadata: `specs/matrices/hyperformula_functions.meta.json`
- Lua prompts (all functions): `specs/lua_prompts.md`
- Backlog list: `specs/reports/ironcalc_missing_but_in_hf.csv`
- Grouped backlog: `specs/reports/ironcalc_missing_but_in_hf_grouped.csv`
- Backlog plan: `specs/planning/lua_implementation_backlog.md`
- Backlog tracker: `specs/reports/lua_backlog_status.csv`

## 2) How To Choose What To Implement
Follow the backlog plan order:
1. Text + Lookup/Reference
2. Math/Financial
3. Statistical
4. Array/Matrix
5. Sheets-only

Only pick items from `ironcalc_missing_but_in_hf.csv`.

## 3) Per-Function Workflow (When We Start)
For each function:
1. Find the prompt in `specs/lua_prompts.md`.
2. Read the spec: `specs/functions/<FUNCTION>.md`.
3. Confirm Excel/Sheets behavior is clear.
4. Implement in Lua.
5. Add tests and fixtures.
6. Update the tracker in `lua_backlog_status.csv`.

## 4) Definition of Done (Per Function)
A function is done when:
- Lua implementation exists.
- Tests exist and pass.
- Fixtures are added if required.
- Tracker shows `status_done=complete`.

## 5) How To Update the Tracker
In `specs/reports/lua_backlog_status.csv`:
- `status_prompt`: keep `ready`
- `status_impl`: `pending` -> `complete`
- `status_tests`: `pending` -> `complete`
- `status_oracle`: `pending` -> `complete`
- `status_done`: `pending` -> `complete`
- `last_updated`: set to date (YYYY-MM-DD)
- `notes`: use for engine differences or edge cases

## 6) Testing (When We Begin)
- Unit tests for core logic.
- Conformance tests for Excel/Sheets parity.
- Update `oracle_capture_status.csv` only when new oracle outputs are captured.

