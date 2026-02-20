# TRUNC
## TRUNC
## Purpose
Truncates number to integer/decimal places.
## Syntax
- Excel: `TRUNC(number, [num_digits])`
- Google Sheets: `TRUNC(number, [num_digits])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TRUNC(1.9) -> 1
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_trunc`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/trunc-function-8b86a64c-3127-43db-ba14-aa5ceb292721

- Source fetch status: failed after 4 attempts

- Summary: Truncates number to integer/decimal places.

- Signatures:

  - `TRUNC(number, [num_digits])`

- Examples:

  - TRUNC(1.9)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093588

- Source fetch status: failed after 4 attempts

- Summary: Truncates number to integer/decimal places.

- Signatures:

  - `TRUNC(number, [num_digits])`

- Examples:

  - TRUNC(1.9)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trunc-function-8b86a64c-3127-43db-ba14-aa5ceb292721
- Google Sheets: https://support.google.com/docs/answer/3093588
