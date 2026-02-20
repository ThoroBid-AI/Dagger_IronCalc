# SECOND
## SECOND
## Purpose
Return second component of time.
## Syntax
- Excel: `SECOND(serial_number)`
- Google Sheets: `SECOND(serial_number)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SECOND("00:00:59") -> 59`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_second`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1

- Source fetch status: failed after 4 attempts

- Summary: Return second component of time.

- Signatures:

  - `SECOND(serial_number)`

- Examples:

  - SECOND("00:00:59")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093054

- Source fetch status: failed after 4 attempts

- Summary: Return second component of time.

- Signatures:

  - `SECOND(serial_number)`

- Examples:

  - SECOND("00:00:59")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1
- Google Sheets: https://support.google.com/docs/answer/3093054
