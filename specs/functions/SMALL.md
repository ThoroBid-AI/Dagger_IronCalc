# SMALL
## SMALL
## Purpose
Computes SMALL semantics for spreadsheet formulas.
## Syntax
- Excel: `SMALL(...)`
- Google Sheets: `SMALL(...)`
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
- Handler: `fn_small`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/small-function-17da8222-7c82-42b2-961b-14c45384df07

- Source fetch status: failed after 4 attempts

- Summary: Computes SMALL semantics for spreadsheet formulas.

- Signatures:

  - `SMALL(...)`

- Examples: `=SMALL(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094050

- Source fetch status: failed after 4 attempts

- Summary: Computes SMALL semantics for spreadsheet formulas.

- Signatures:

  - `SMALL(...)`

- Examples: `=SMALL(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/small-function-17da8222-7c82-42b2-961b-14c45384df07
- Google Sheets: https://support.google.com/docs/answer/3094050
