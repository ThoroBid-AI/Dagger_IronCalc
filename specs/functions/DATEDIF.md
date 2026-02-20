# DATEDIF
## DATEDIF
## Purpose
Returns difference between two dates by unit.
## Syntax
- Excel: `DATEDIF(start_date, end_date, unit)`
- Google Sheets: `DATEDIF(start_date, end_date, unit)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `DATEDIF("2026-01-01","2026-12-31","y") -> 0`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_datedif`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c

- Source fetch status: failed after 4 attempts

- Summary: Returns difference between two dates by unit.

- Signatures:

  - `DATEDIF(start_date, end_date, unit)`

- Examples:

  - DATEDIF("2026-01-01","2026-12-31","y")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055612

- Source fetch status: failed after 4 attempts

- Summary: Returns difference between two dates by unit.

- Signatures:

  - `DATEDIF(start_date, end_date, unit)`

- Examples:

  - DATEDIF("2026-01-01","2026-12-31","y")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c
- Google Sheets: https://support.google.com/docs/answer/6055612
