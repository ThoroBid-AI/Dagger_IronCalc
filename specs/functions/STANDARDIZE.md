# STANDARDIZE
## STANDARDIZE
## Purpose
Computes STANDARDIZE semantics for spreadsheet formulas.
## Syntax
- Excel: `STANDARDIZE(...)`
- Google Sheets: `STANDARDIZE(...)`
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
- Handler: `fn_standardize`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standardize.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/standardize-function-81d66554-2d54-40ec-ba83-6437108ee775

- Source fetch status: failed after 4 attempts

- Summary: Computes STANDARDIZE semantics for spreadsheet formulas.

- Signatures:

  - `STANDARDIZE(...)`

- Examples: `=STANDARDIZE(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094102

- Source fetch status: failed after 4 attempts

- Summary: Computes STANDARDIZE semantics for spreadsheet formulas.

- Signatures:

  - `STANDARDIZE(...)`

- Examples: `=STANDARDIZE(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/standardize-function-81d66554-2d54-40ec-ba83-6437108ee775
- Google Sheets: https://support.google.com/docs/answer/3094102
