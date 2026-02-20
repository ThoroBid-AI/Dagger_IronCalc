# SQRT
## SQRT
## Purpose
Return square root.
## Syntax
- Excel: `SQRT(number)`
- Google Sheets: `SQRT(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SQRT(9) -> 3`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sqrt`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf

- Source fetch status: failed after 4 attempts

- Summary: Return square root.

- Signatures:

  - `SQRT(number)`

- Examples: `=SQRT(1)` -> `0`

  - SQRT(9)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093577

- Source fetch status: failed after 4 attempts

- Summary: Return square root.

- Signatures:

  - `SQRT(number)`

- Examples: `=SQRT(1)` -> `0`

  - SQRT(9)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf
- Google Sheets: https://support.google.com/docs/answer/3093577
