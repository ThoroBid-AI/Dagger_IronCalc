# Function Implementation Plan (Lua + Coverage)

## Purpose
Provide a single, clean plan for closing function parity by using:
- Excel + Google Sheets as behavioral truth
- HyperFormula as coverage reference
- Lua prompts as the implementation guide

This plan replaces the old batch/Rust workflow for the new Lua pipeline.

## Runtime Target (Locked)
- Implementation runtime in this repo is Rust (`base` crate), not standalone Lua.
- `specs/lua_prompts.md` is used as implementation guidance.
- Contract: `specs/planning/implementation_runtime_contract.md`
- LLM handoff playbook: `specs/planning/implementation_handoff_contract.md`

## Authoritative Sources
Use these files only:
- Coverage matrix: `specs/matrices/function_matrix_normalized.csv`
- HyperFormula list: `specs/matrices/hyperformula_functions.csv`
- HyperFormula metadata: `specs/matrices/hyperformula_functions.meta.json`
- Lua prompts (all functions): `specs/lua_prompts.md`
- Backlog list: `specs/reports/ironcalc_missing_but_in_hf.csv`
- Grouped backlog: `specs/reports/ironcalc_missing_but_in_hf_grouped.csv`
- Backlog plan: `specs/planning/lua_implementation_backlog.md`
- Execution workflow: `specs/planning/lua_execution_workflow.md`
- Execution charter: `specs/planning/lua_execution_charter.md`
- Backlog tracker: `specs/reports/lua_backlog_status.csv`
- Optional detailed specs (when present): `specs/functions/<FUNCTION>.md`

## Coverage Refresh (When Needed)
1. Update HyperFormula list:
   - `python scripts/update_hyperformula_functions.py --source-html <file>`
2. Refresh the matrix:
   - `python scripts/update_function_matrix.py`
3. Regenerate reports:
   - `python scripts/generate_hf_coverage_reports.py`
4. Regenerate prompts:
   - `python scripts/generate_lua_prompts.py`

## Execution Order
Follow the order in:
- `specs/planning/lua_implementation_backlog.md`

## Definition of Done (Per Function)
A function is done when:
- Rust implementation exists
- Tests added and passing
- Fixtures captured if required
- Tracker shows `status_done=complete`

## Deliverables
- Updated matrix with HyperFormula coverage
- Consolidated Lua prompts
- Backlog list + grouped backlog
- Backlog status tracker
- Execution workflow + charter

## Legacy Data (Not Part of Current Lua Plan)
These files remain for older tooling and can be ignored for the new workflow:
- `specs/data/function_batches.csv`
- `specs/data/function_complexity_map.csv`
- `specs/data/function_io_shape.csv`
