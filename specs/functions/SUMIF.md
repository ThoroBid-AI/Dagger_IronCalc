# SUMIF
## SUMIF
## Purpose
Computes SUMIF semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMIF(...)`
- Google Sheets: `SUMIF(...)`
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
- Handler: `fn_sumif`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMIF semantics for spreadsheet formulas.

- Signatures:

  - `SUMIF(...)`

- Examples: `=SUMIF(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093583

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMIF semantics for spreadsheet formulas.

- Signatures:

  - `SUMIF(...)`

- Examples: `=SUMIF(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b
- Google Sheets: https://support.google.com/docs/answer/3093583
