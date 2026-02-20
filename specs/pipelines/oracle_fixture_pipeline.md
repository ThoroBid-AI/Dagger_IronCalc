# Oracle Fixture Pipeline

## Goal
Provide a deterministic, repeatable process to capture oracle outputs and validate IronCalc.

## Inputs
- Function name, formula, input ranges/arrays.
- Engine target: Excel 365 or Google Sheets.
- Locale: en-US.

## Pipeline Steps
1. **Fixture definition**
   - Define test cases with inputs and formulas.
2. **Oracle capture**
   - Evaluate in Excel 365 and/or Google Sheets.
   - Record outputs with version/build metadata.
3. **Fixture storage**
   - Save as JSON in `fixtures/<function>/<case_id>.json`.
4. **Conformance run**
   - Execute IronCalc against fixtures.
   - Compare outputs using tolerance policy.
5. **Report**
   - Emit pass/fail with mismatches and diffs.

## Tooling (Proposed)
- `scripts/generate_fixtures.py`
- `scripts/run_conformance.py`

## Determinism Rules
- Stable JSON key ordering.
- Fixed numeric formatting policy.
- No reliance on system time unless explicitly provided via calculation context.
