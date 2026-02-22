# NETWORKDAYS.INTL
## NETWORKDAYS.INTL
## Purpose
Returns business days with custom weekend mask.
## Syntax
- Excel: `NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])`
- Google Sheets: `NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `NETWORKDAYS.INTL("2026-01-01","2026-01-10",16) -> n`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Proposed file: `base/src/functions/date_and_time.rs`
- Proposed handler: `fn_networkdays.intl`
- Pseudocode: validate date arguments, apply calendar/business-day logic, return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28

- Source fetch status: failed after 4 attempts

- Summary: Returns business days with custom weekend mask.

- Signatures:

  - `NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])`

- Examples:

  - NETWORKDAYS.INTL("2026-01-01","2026-01-10",16)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3295902

- Source fetch status: failed after 4 attempts

- Summary: Returns business days with custom weekend mask.

- Signatures:

  - `NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])`

- Examples:

  - NETWORKDAYS.INTL("2026-01-01","2026-01-10",16)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28
- Google Sheets: https://support.google.com/docs/answer/3295902
