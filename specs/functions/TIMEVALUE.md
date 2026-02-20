# TIMEVALUE
## TIMEVALUE
## Purpose
Converts time text to serial time.
## Syntax
- Excel: `TIMEVALUE(time_text)`
- Google Sheets: `TIMEVALUE(time_text)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `TIMEVALUE("13:30") -> 0.5625`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_timevalue`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/timevalue-function-0b615c12-33d8-4431-bf3d-f3eb6d186645

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible date arithmetic.

- Signatures:

  - `TIMEVALUE(time_text)`

- Examples:

  - TIMEVALUE("13:30")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267350

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible date arithmetic.

- Signatures:

  - `TIMEVALUE(time_text)`

- Examples:

  - TIMEVALUE("13:30")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/timevalue-function-0b615c12-33d8-4431-bf3d-f3eb6d186645
- Google Sheets: https://support.google.com/docs/answer/3267350
