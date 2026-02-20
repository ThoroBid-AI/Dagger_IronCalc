# VALUE
## VALUE
## Purpose
Converts text to numeric value.
## Syntax
- Excel: `VALUE(text)`
- Google Sheets: `VALUE(text)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- VALUE("123") -> 123
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_value`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/value-function-257d0108-07dc-437d-ae1c-bc2d3953d8c2

- Source fetch status: failed after 4 attempts

- Summary: Converts text to numeric value.

- Signatures:

  - `VALUE(text)`

- Examples: `=VALUE(1)` -> `0`

  - VALUE("123")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094220

- Source fetch status: failed after 4 attempts

- Summary: Converts text to numeric value.

- Signatures:

  - `VALUE(text)`

- Examples: `=VALUE(1)` -> `0`

  - VALUE("123")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/value-function-257d0108-07dc-437d-ae1c-bc2d3953d8c2
- Google Sheets: https://support.google.com/docs/answer/3094220
