# WORKDAY
## WORKDAY
## Purpose
Returns workday date after specified days.
## Syntax
- Excel: `WORKDAY(start_date, days, [holidays])`
- Google Sheets: `WORKDAY(start_date, days, [holidays])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `WORKDAY("2026-01-01",10) -> date`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_workday`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/workday-function-f764a5b7-05fc-4494-9486-60d494efbf33

- Source fetch status: failed after 4 attempts

- Summary: Returns workday date after specified days.

- Signatures:

  - `WORKDAY(start_date, days, [holidays])`

- Examples:

  - WORKDAY("2026-01-01",10)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093059

- Source fetch status: failed after 4 attempts

- Summary: Returns workday date after specified days.

- Signatures:

  - `WORKDAY(start_date, days, [holidays])`

- Examples:

  - WORKDAY("2026-01-01",10)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/workday-function-f764a5b7-05fc-4494-9486-60d494efbf33
- Google Sheets: https://support.google.com/docs/answer/3093059
