# TODAY
## TODAY
## Purpose
Returns current date.
## Syntax
- Excel: `TODAY()`
- Google Sheets: `TODAY()`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TODAY() -> serial date
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_today`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9

- Source fetch status: failed after 4 attempts

- Summary: Returns current date.

- Signatures:

  - `TODAY()`

- Examples:

  - TODAY()

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092984

- Source fetch status: failed after 4 attempts

- Summary: Returns current date.

- Signatures:

  - `TODAY()`

- Examples:

  - TODAY()

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9
- Google Sheets: https://support.google.com/docs/answer/3092984
