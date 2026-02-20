# TBILLEQ
## TBILLEQ
## Purpose
Returns treasury bill discount-equivalent yield.
## Syntax
- Excel: `TBILLEQ(settlement, maturity, discount)`
- Google Sheets: `TBILLEQ(settlement, maturity, discount)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TBILLEQ("2026-01-01","2026-07-01",0.05) -> 0.06
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tbilleq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c

- Source fetch status: failed after 4 attempts

- Summary: Returns treasury bill discount-equivalent yield.

- Signatures:

  - `TBILLEQ(settlement, maturity, discount)`

- Examples: `=TBILLEQ(1, 2, 3)` -> `0`

  - TBILLEQ("2026-01-01","2026-07-01",0.05)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093249

- Source fetch status: failed after 4 attempts

- Summary: Returns treasury bill discount-equivalent yield.

- Signatures:

  - `TBILLEQ(settlement, maturity, discount)`

- Examples: `=TBILLEQ(1, 2, 3)` -> `0`

  - TBILLEQ("2026-01-01","2026-07-01",0.05)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c
- Google Sheets: https://support.google.com/docs/answer/3093249
