# TBILLPRICE
## TBILLPRICE
## Purpose
Returns treasury bill price.
## Syntax
- Excel: `TBILLPRICE(settlement,maturity,discount)`
- Google Sheets: `TBILLPRICE(settlement,maturity,discount)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TBILLPRICE("2026-01-01","2026-07-01",0.05) -> 100
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tbillprice`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2

- Source fetch status: failed after 4 attempts

- Summary: Returns treasury bill price.

- Signatures:

  - `TBILLPRICE(settlement,maturity,discount)`

- Examples: `=TBILLPRICE(1, 2, 3)` -> `0`

  - TBILLPRICE("2026-01-01","2026-07-01",0.05)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093251

- Source fetch status: failed after 4 attempts

- Summary: Returns treasury bill price.

- Signatures:

  - `TBILLPRICE(settlement,maturity,discount)`

- Examples: `=TBILLPRICE(1, 2, 3)` -> `0`

  - TBILLPRICE("2026-01-01","2026-07-01",0.05)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2
- Google Sheets: https://support.google.com/docs/answer/3093251
