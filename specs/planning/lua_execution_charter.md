# Lua Execution Charter

This document locks the execution decisions before implementation begins.

## 0) Runtime Target (Locked)
- Implement functions in the Rust engine (`base` crate) in this repository.
- `specs/lua_prompts.md` remains the guidance artifact for behavior/spec context.
- See `specs/planning/implementation_runtime_contract.md`.
- Use `specs/planning/implementation_handoff_contract.md` for concrete execution steps.

## 1) Execution Order (Locked)
We will implement functions in this order:
1. Text + Lookup/Reference
2. Math/Financial
3. Statistical
4. Array/Matrix
5. Sheets-only

## 2) Progress Tracking (Locked)
The single source of truth is:
- `specs/reports/lua_backlog_status.csv`

Updates required after each function:
- `status_impl`, `status_tests`, `status_oracle`, `status_done`
- `last_updated` set to YYYY-MM-DD
- `notes` used for engine differences

## 3) Parity Target (Locked)
Engine implementations must match **Excel and Google Sheets behavior**.
HyperFormula is used for coverage reference only.

## 4) Definition of Done (Locked)
A function is done when:
- Implementation exists in the Rust engine
- Tests added and passing
- Fixtures captured if required
- Tracker shows `status_done=complete`
