# SUMIFS
## SUMIFS
## Purpose
Computes SUMIFS semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMIFS(...)`
- Google Sheets: `SUMIFS(...)`
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
- Handler: `fn_sumifs`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMIFS semantics for spreadsheet formulas.

- Signatures:

  - `SUMIFS(...)`

- Examples: `=SUMIFS(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3238496

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMIFS semantics for spreadsheet formulas.

- Signatures:

  - `SUMIFS(...)`

- Examples: `=SUMIFS(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b
- Google Sheets: https://support.google.com/docs/answer/3238496
