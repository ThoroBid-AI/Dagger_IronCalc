# SUM
## SUM
## Purpose
Computes SUM semantics for spreadsheet formulas.
## Syntax
- Excel: `SUM(...)`
- Google Sheets: `SUM(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sum`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89

- Source fetch status: failed after 4 attempts

- Summary: Computes SUM semantics for spreadsheet formulas.

- Signatures:

  - `SUM(...)`

- Examples: `=SUM(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093669

- Source fetch status: failed after 4 attempts

- Summary: Computes SUM semantics for spreadsheet formulas.

- Signatures:

  - `SUM(...)`

- Examples: `=SUM(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89
- Google Sheets: https://support.google.com/docs/answer/3093669
