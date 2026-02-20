# T
## T
## Purpose
Returns text argument as text or empty string.
## Syntax
- Excel: `T(value)`
- Google Sheets: `T(value)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- T("x") -> ""
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_t`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-function-fb83aeec-45e7-4924-af95-53e073541228

- Source fetch status: failed after 4 attempts

- Summary: Returns text argument as text or empty string.

- Signatures:

  - `T(value)`

- Examples:

  - T("x")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094138

- Source fetch status: failed after 4 attempts

- Summary: Returns text argument as text or empty string.

- Signatures:

  - `T(value)`

- Examples:

  - T("x")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-function-fb83aeec-45e7-4924-af95-53e073541228
- Google Sheets: https://support.google.com/docs/answer/3094138
