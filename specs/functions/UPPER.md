# UPPER
## UPPER
## Purpose
Converts text to upper case.
## Syntax
- Excel: `UPPER(text)`
- Google Sheets: `UPPER(text)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- UPPER("abc") -> "ABC"
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_upper`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6

- Source fetch status: failed after 4 attempts

- Summary: Converts text to upper case.

- Signatures:

  - `UPPER(text)`

- Examples: `=UPPER(1)` -> `0`

  - UPPER("abc")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094219

- Source fetch status: failed after 4 attempts

- Summary: Converts text to upper case.

- Signatures:

  - `UPPER(text)`

- Examples: `=UPPER(1)` -> `0`

  - UPPER("abc")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6
- Google Sheets: https://support.google.com/docs/answer/3094219
