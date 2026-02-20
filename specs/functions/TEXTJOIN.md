# TEXTJOIN
## TEXTJOIN
## Purpose
Concatenates values with delimiter.
## Syntax
- Excel: `TEXTJOIN(delimiter, ignore_empty, text1, ...)`
- Google Sheets: `TEXTJOIN(delimiter, ignore_empty, text1, ...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TEXTJOIN(",",TRUE,"a","b") -> "a,b"
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_textjoin`
- File: `base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c

- Source fetch status: failed after 4 attempts

- Summary: Concatenates values with delimiter.

- Signatures:

  - `TEXTJOIN(delimiter, ignore_empty, text1, ...)`

- Examples:

  - TEXTJOIN(",",TRUE,"a","b")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7013992

- Source fetch status: failed after 4 attempts

- Summary: Concatenates values with delimiter.

- Signatures:

  - `TEXTJOIN(delimiter, ignore_empty, text1, ...)`

- Examples:

  - TEXTJOIN(",",TRUE,"a","b")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c
- Google Sheets: https://support.google.com/docs/answer/7013992
