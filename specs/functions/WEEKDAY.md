# WEEKDAY
## WEEKDAY
## Purpose
Computes WEEKDAY behavior for spreadsheet formulas.
## Syntax
- Excel: `WEEKDAY(...)`
- Google Sheets: `WEEKDAY(...)`
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
- Handler: `fn_weekday`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a

- Source fetch status: failed after 4 attempts

- Summary: Computes WEEKDAY behavior for spreadsheet formulas.

- Signatures:

  - `WEEKDAY(...)`

- Examples: `WEEKDAY(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092985

- Source fetch status: failed after 4 attempts

- Summary: Computes WEEKDAY behavior for spreadsheet formulas.

- Signatures:

  - `WEEKDAY(...)`

- Examples: `WEEKDAY(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a
- Google Sheets: https://support.google.com/docs/answer/3092985
