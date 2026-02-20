# STDEVA
## STDEVA
## Purpose
Computes STDEVA semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEVA(...)`
- Google Sheets: `STDEVA(...)`
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
- Handler: `fn_stdeva`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEVA semantics for spreadsheet formulas.

- Signatures:

  - `STDEVA(...)`

- Examples: `=STDEVA(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094055

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEVA semantics for spreadsheet formulas.

- Signatures:

  - `STDEVA(...)`

- Examples: `=STDEVA(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d
- Google Sheets: https://support.google.com/docs/answer/3094055
