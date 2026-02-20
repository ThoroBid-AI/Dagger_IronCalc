# YEAR
## YEAR
## Purpose
Computes YEAR behavior for spreadsheet formulas.
## Syntax
- Excel: `YEAR(...)`
- Google Sheets: `YEAR(...)`
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
- Handler: `fn_year`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `YEAR(...)`

- Examples:
  - `=YEAR(1, 2)`,
  - `=YEAR(A1, B1)`,
  - `=YEAR(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3093061

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `YEAR(...)`

- Examples:
  - `=YEAR(1, 2)`,
  - `=YEAR(A1, B1)`,
  - `=YEAR(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9
- Google Sheets: https://support.google.com/docs/answer/3093061
