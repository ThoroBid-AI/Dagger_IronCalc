# SUMSQ
## SUMSQ
## Purpose
Computes SUMSQ semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMSQ(...)`
- Google Sheets: `SUMSQ(...)`
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
- Handler: `fn_sumsq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumsq-function-e3313c02-51cc-4963-aae6-31442d9ec307

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMSQ semantics for spreadsheet formulas.

- Signatures:

  - `SUMSQ(...)`

- Examples: `=SUMSQ(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093714

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMSQ semantics for spreadsheet formulas.

- Signatures:

  - `SUMSQ(...)`

- Examples: `=SUMSQ(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumsq-function-e3313c02-51cc-4963-aae6-31442d9ec307
- Google Sheets: https://support.google.com/docs/answer/3093714
