# Lua Implementation Backlog (HF + Excel/Sheets)

## Purpose
Define a complete, ordered implementation backlog (using Lua prompts as guidance) based on the global function coverage matrix. This backlog is the primary list for closing parity gaps in IronCalc by leveraging HyperFormula coverage.

## Runtime Contract
- Implementation runtime in this repository is Rust (`base` crate).
- `specs/lua_prompts.md` is a planning/spec artifact used for behavior guidance.
- See `specs/planning/implementation_runtime_contract.md`.
- Use `specs/planning/implementation_handoff_contract.md` as the per-function execution contract.

## Source Files
- Coverage matrix: `specs/matrices/function_matrix_normalized.csv`
- HF vs IronCalc report: `specs/reports/ironcalc_missing_but_in_hf.csv`
- Grouped backlog: `specs/reports/ironcalc_missing_but_in_hf_grouped.csv`
- Lua prompts: `specs/lua_prompts.md`
- Optional detailed specs: `specs/functions/<FUNCTION>.md` (when present)
- Status tracker: `specs/reports/lua_backlog_status.csv`

## Backlog Definition
Functions that are **missing in IronCalc**, but **present in HyperFormula** and **present in Excel or Sheets**.

## Implementation Order (Recommended)
1. **Text + Lookup/Reference** (low risk, deterministic behavior)
2. **Math/Financial** (moderate risk, numeric precision)
3. **Statistical** (higher risk, distributions/tolerance)
4. **Array/Matrix** (highest risk, shape/spill rules)
5. **Sheets‑only** functions (validate gaps vs Excel)

## Backlog (Grouped)

### Text
- `CHAR`
- `CLEAN`
- `CODE`
- `PROPER`
- `REPLACE`
- `UNICHAR`

### Lookup/Reference
- `ADDRESS`
- `HYPERLINK`

### Math/Financial
- `FVSCHEDULE`
- `MULTINOMIAL`
- `SERIESSUM`
- `SUMPRODUCT`

### Statistical
- `CRITBINOM`

### Array/Matrix
- `ARRAYFORMULA` (Sheets only)
- `ARRAY_CONSTRAIN` (Sheets only)
- `FILTER`
- `MMULT`
- `SPLIT` (Sheets only)
- `TRANSPOSE`

### Aggregation
- `COUNTUNIQUE` (Sheets only)

## Execution Checklist (Per Function)
1. Open prompt: search for the function in `specs/lua_prompts.md`
2. Review behavior sections in `specs/lua_prompts.md` as primary spec input.
3. If available, review `specs/functions/<FUNCTION>.md` for extra detail.
4. Confirm expected behavior across Excel + Sheets.
5. Implement in Rust engine code with error/array/coercion rules.
6. Add tests + fixtures as required by the main plan.
7. Update status in tracking (if applicable).
