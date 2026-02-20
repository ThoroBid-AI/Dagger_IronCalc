# WORKDAY.INTL
## WORKDAY.INTL
## Purpose
Returns workday date with custom weekend schedule.
## Syntax
- Excel: `WORKDAY.INTL(start_date, days, [weekend], [holidays])`
- Google Sheets: `WORKDAY.INTL(start_date, days, [weekend], [holidays])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `WORKDAY.INTL("2026-01-01",10,1) -> date`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Proposed file: `base/src/functions/date_and_time.rs`
- Proposed handler: `fn_workday.intl`
- Pseudocode: validate date arguments, apply calendar/business-day logic, return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/workday-intl-function-a378391c-9ba7-4678-8a39-39611a9bf81d

- Source fetch status: failed after 4 attempts

- Summary: Returns workday date with custom weekend schedule.

- Signatures:

  - `WORKDAY.INTL(start_date, days, [weekend], [holidays])`

- Examples: `WORKDAY.INTL(1,2,3)` -> `0`

  - WORKDAY.INTL("2026-01-01",10,1)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3294972

- Source fetch status: failed after 4 attempts

- Summary: Returns workday date with custom weekend schedule.

- Signatures:

  - `WORKDAY.INTL(start_date, days, [weekend], [holidays])`

- Examples: `WORKDAY.INTL(1,2,3)` -> `0`

  - WORKDAY.INTL("2026-01-01",10,1)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/workday-intl-function-a378391c-9ba7-4678-8a39-39611a9bf81d
- Google Sheets: https://support.google.com/docs/answer/3294972
