# Lua Implementation Backlog (HF + Excel/Sheets)

## Purpose
Define a complete, ordered Lua implementation backlog based on the global function coverage matrix. This backlog is the primary list for closing parity gaps in IronCalc by leveraging HyperFormula coverage.

## Source Files
- Coverage matrix: `specs/matrices/function_matrix_normalized.csv`
- HF vs IronCalc report: `specs/reports/ironcalc_missing_but_in_hf.csv`
- Grouped backlog: `specs/reports/ironcalc_missing_but_in_hf_grouped.csv`
- Lua prompts: `specs/lua_prompts.md`
- Specs: `specs/functions/<FUNCTION>.md`
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
- `REPLACE` (Sheets only)
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
- `FTEST`
- `GAMMADIST`
- `GAMMAINV`
- `HYPGEOMDIST`
- `NEGBINOMDIST`
- `TTEST`

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
2. Review spec: `specs/functions/<FUNCTION>.md`
3. Confirm expected behavior across Excel + Sheets.
4. Implement in Lua with error/array/coercion rules.
5. Add tests + fixtures as required by the main plan.
6. Update status in tracking (if applicable).
