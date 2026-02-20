# SQRTPI
## SQRTPI
## Purpose
Computes SQRTPI semantics for spreadsheet formulas.
## Syntax
- Excel: `SQRTPI(...)`
- Google Sheets: `SQRTPI(...)`
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
- Handler: `fn_sqrtpi`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sqrtpi-function-1fb4e63f-9b51-46d6-ad68-b3e7a8b519b4

- Source fetch status: failed after 4 attempts

- Summary: Computes SQRTPI semantics for spreadsheet formulas.

- Signatures:

  - `SQRTPI(...)`

- Examples: `=SQRTPI(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093579

- Source fetch status: failed after 4 attempts

- Summary: Computes SQRTPI semantics for spreadsheet formulas.

- Signatures:

  - `SQRTPI(...)`

- Examples: `=SQRTPI(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sqrtpi-function-1fb4e63f-9b51-46d6-ad68-b3e7a8b519b4
- Google Sheets: https://support.google.com/docs/answer/3093579
