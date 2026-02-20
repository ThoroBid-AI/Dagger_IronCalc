# XNPV
## XNPV
## Purpose
Computes XNPV behavior for spreadsheet formulas.
## Syntax
- Excel: `XNPV(...)`
- Google Sheets: `XNPV(...)`
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
- Handler: `fn_xnpv`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `XNPV(...)`

- Examples:
  - `=XNPV(1, 2)`,
  - `=XNPV(A1, B1)`,
  - `=XNPV(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3093268

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `XNPV(...)`

- Examples:
  - `=XNPV(1, 2)`,
  - `=XNPV(A1, B1)`,
  - `=XNPV(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7
- Google Sheets: https://support.google.com/docs/answer/3093268
