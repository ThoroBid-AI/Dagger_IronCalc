# NETWORKDAYS
## NETWORKDAYS
## Purpose
Returns business days between dates.
## Syntax
- Excel: `NETWORKDAYS(start_date,end_date,[holidays])`
- Google Sheets: `NETWORKDAYS(start_date,end_date,[holidays])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `NETWORKDAYS("2026-01-01","2026-01-10") -> n`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_networkdays`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7

- Source fetch status: failed after 4 attempts

- Summary: Returns business days between dates.

- Signatures:

  - `NETWORKDAYS(start_date,end_date,[holidays])`

- Examples:

  - NETWORKDAYS("2026-01-01","2026-01-10")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092979

- Source fetch status: failed after 4 attempts

- Summary: Returns business days between dates.

- Signatures:

  - `NETWORKDAYS(start_date,end_date,[holidays])`

- Examples:

  - NETWORKDAYS("2026-01-01","2026-01-10")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7
- Google Sheets: https://support.google.com/docs/answer/3092979
