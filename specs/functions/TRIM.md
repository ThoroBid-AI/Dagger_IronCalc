# TRIM
## TRIM
## Purpose
Removes extra spaces from text.
## Syntax
- Excel: `TRIM(text)`
- Google Sheets: `TRIM(text)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TRIM(" a  b ") -> "a b"
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_trim`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9

- Source fetch status: failed after 4 attempts

- Summary: Removes extra spaces from text.

- Signatures:

  - `TRIM(text)`

- Examples:

  - TRIM(" a b ")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094140

- Source fetch status: failed after 4 attempts

- Summary: Removes extra spaces from text.

- Signatures:

  - `TRIM(text)`

- Examples:

  - TRIM(" a b ")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9
- Google Sheets: https://support.google.com/docs/answer/3094140
