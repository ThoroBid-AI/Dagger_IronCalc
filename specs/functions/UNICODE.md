# UNICODE
## UNICODE
## Purpose
Returns numeric codepoint for first character.
## Syntax
- Excel: `UNICODE(text)`
- Google Sheets: `UNICODE(text)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- UNICODE("A") -> 65
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_unicode`
- File: `base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/unicode-function-adb74aaa-a2a5-4dde-aff6-966e4e81f16f

- Source fetch status: failed after 4 attempts

- Summary: Returns numeric codepoint for first character.

- Signatures:

  - `UNICODE(text)`

- Examples:

  - UNICODE("A")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9149523

- Source fetch status: failed after 4 attempts

- Summary: Returns numeric codepoint for first character.

- Signatures:

  - `UNICODE(text)`

- Examples:

  - UNICODE("A")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/unicode-function-adb74aaa-a2a5-4dde-aff6-966e4e81f16f
- Google Sheets: https://support.google.com/docs/answer/9149523
