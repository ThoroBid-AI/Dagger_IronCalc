# YEARFRAC
## YEARFRAC
## Purpose
Computes YEARFRAC behavior for spreadsheet formulas.
## Syntax
- Excel: `YEARFRAC(...)`
- Google Sheets: `YEARFRAC(...)`
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
- Handler: `fn_yearfrac`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/yearfrac-function-3844141e-c76d-4143-82b6-208454ddc6a8

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `YEARFRAC(...)`

- Examples:
  - `=YEARFRAC(1, 2)`,
  - `=YEARFRAC(A1, B1)`,
  - `=YEARFRAC(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3092989

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `YEARFRAC(...)`

- Examples:
  - `=YEARFRAC(1, 2)`,
  - `=YEARFRAC(A1, B1)`,
  - `=YEARFRAC(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/yearfrac-function-3844141e-c76d-4143-82b6-208454ddc6a8
- Google Sheets: https://support.google.com/docs/answer/3092989
