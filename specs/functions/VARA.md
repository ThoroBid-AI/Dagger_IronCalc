# VARA
## VARA
## Purpose
Computes VARA behavior for spreadsheet formulas.
## Syntax
- Excel: `VARA(...)`
- Google Sheets: `VARA(...)`
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
- Handler: `fn_vara`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07

- Source fetch status: failed after 4 attempts

- Summary: Computes VARA behavior for spreadsheet formulas.

- Signatures:

  - `VARA(...)`

- Examples: `=VARA(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094064

- Source fetch status: failed after 4 attempts

- Summary: Computes VARA behavior for spreadsheet formulas.

- Signatures:

  - `VARA(...)`

- Examples: `=VARA(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07
- Google Sheets: https://support.google.com/docs/answer/3094064
