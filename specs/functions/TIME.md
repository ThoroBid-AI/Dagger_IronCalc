# TIME
## TIME
## Purpose
Converts hour minute second to serial time.
## Syntax
- Excel: `TIME(hour, minute, second)`
- Google Sheets: `TIME(hour, minute, second)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `TIME(1,30,0) -> 0.0625`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_time`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/time-function-9a5aff99-8f7d-4611-845e-747d0b8d5457

- Source fetch status: failed after 4 attempts

- Summary: Converts hour minute second to serial time.

- Signatures:

  - `TIME(hour, minute, second)`

- Examples: `=TIME(1,2,3)` -> `0`

  - TIME(1,30,0)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093056

- Source fetch status: failed after 4 attempts

- Summary: Converts hour minute second to serial time.

- Signatures:

  - `TIME(hour, minute, second)`

- Examples: `=TIME(1,2,3)` -> `0`

  - TIME(1,30,0)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/time-function-9a5aff99-8f7d-4611-845e-747d0b8d5457
- Google Sheets: https://support.google.com/docs/answer/3093056
