# XIRR
## XIRR
## Purpose
Computes XIRR behavior for spreadsheet formulas.
## Syntax
- Excel: `XIRR(...)`
- Google Sheets: `XIRR(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_xirr`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d

- Source fetch status: failed after 4 attempts

- Summary: Computes XIRR behavior for spreadsheet formulas.

- Signatures:

  - `XIRR(...)`

- Examples: `XIRR(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093266

- Source fetch status: failed after 4 attempts

- Summary: Computes XIRR behavior for spreadsheet formulas.

- Signatures:

  - `XIRR(...)`

- Examples: `XIRR(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d
- Google Sheets: https://support.google.com/docs/answer/3093266
