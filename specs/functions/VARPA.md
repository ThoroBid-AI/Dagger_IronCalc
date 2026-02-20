# VARPA
## VARPA
## Purpose
Computes VARPA behavior for spreadsheet formulas.
## Syntax
- Excel: `VARPA(...)`
- Google Sheets: `VARPA(...)`
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
- Handler: `fn_varpa`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `VARPA(...)`

- Examples:
  - `=VARPA(1, 2)`,
  - `=VARPA(A1, B1)`,
  - `=VARPA(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3094065

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `VARPA(...)`

- Examples:
  - `=VARPA(1, 2)`,
  - `=VARPA(A1, B1)`,
  - `=VARPA(10, 20, 30)`,
- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96
- Google Sheets: https://support.google.com/docs/answer/3094065
