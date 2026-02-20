# TBILLYIELD
## TBILLYIELD
## Purpose
Returns treasury bill annual yield.
## Syntax
- Excel: `TBILLYIELD(settlement,maturity,price)`
- Google Sheets: `TBILLYIELD(settlement,maturity,price)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TBILLYIELD("2026-01-01","2026-07-01",98) -> 0.055
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tbillyield`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba

- Source fetch status: failed after 4 attempts

- Summary: Returns treasury bill annual yield.

- Signatures:

  - `TBILLYIELD(settlement,maturity,price)`

- Examples: `=TBILLYIELD(1, 2, 3)` -> `0`

  - TBILLYIELD("2026-01-01","2026-07-01",98)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093264

- Source fetch status: failed after 4 attempts

- Summary: Returns treasury bill annual yield.

- Signatures:

  - `TBILLYIELD(settlement,maturity,price)`

- Examples: `=TBILLYIELD(1, 2, 3)` -> `0`

  - TBILLYIELD("2026-01-01","2026-07-01",98)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba
- Google Sheets: https://support.google.com/docs/answer/3093264
