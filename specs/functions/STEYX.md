# STEYX
## STEYX
## Purpose
Computes STEYX semantics for spreadsheet formulas.
## Syntax
- Excel: `STEYX(...)`
- Google Sheets: `STEYX(...)`
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
- Handler: `fn_steyx`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab

- Source fetch status: failed after 4 attempts

- Summary: Computes STEYX semantics for spreadsheet formulas.

- Signatures:

  - `STEYX(...)`

- Examples: `=STEYX(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094108

- Source fetch status: failed after 4 attempts

- Summary: Computes STEYX semantics for spreadsheet formulas.

- Signatures:

  - `STEYX(...)`

- Examples: `=STEYX(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab
- Google Sheets: https://support.google.com/docs/answer/3094108
