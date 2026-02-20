# TEXT
## TEXT
## Purpose
Formats values as text using number format string.
## Syntax
- Excel: `TEXT(value, format_text)`
- Google Sheets: `TEXT(value, format_text)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TEXT(123.45,"0.00") -> "123.45"
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_text`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c

- Source fetch status: failed after 4 attempts

- Summary: Formats values as text using number format string.

- Signatures:

  - `TEXT(value, format_text)`

- Examples:

  - TEXT(123.45,"0.00")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094139

- Source fetch status: failed after 4 attempts

- Summary: Formats values as text using number format string.

- Signatures:

  - `TEXT(value, format_text)`

- Examples:

  - TEXT(123.45,"0.00")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c
- Google Sheets: https://support.google.com/docs/answer/3094139
