# WEEKNUM
## WEEKNUM
## Purpose
Computes WEEKNUM behavior for spreadsheet formulas.
## Syntax
- Excel: `WEEKNUM(...)`
- Google Sheets: `WEEKNUM(...)`
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
- Handler: `fn_weeknum`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `WEEKNUM(...)`

- Examples:
  - `=WEEKNUM(1, 2)`,
  - `=WEEKNUM(A1, B1)`,
  - `=WEEKNUM(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3294949

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `WEEKNUM(...)`

- Examples:
  - `=WEEKNUM(1, 2)`,
  - `=WEEKNUM(A1, B1)`,
  - `=WEEKNUM(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340
- Google Sheets: https://support.google.com/docs/answer/3294949
