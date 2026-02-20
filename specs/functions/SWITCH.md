# SWITCH
## SWITCH
## Purpose
Computes SWITCH semantics for spreadsheet formulas.
## Syntax
- Excel: `SWITCH(...)`
- Google Sheets: `SWITCH(...)`
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
- Handler: `fn_switch`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e

- Source fetch status: failed after 4 attempts

- Summary: Computes SWITCH semantics for spreadsheet formulas.

- Signatures:

  - `SWITCH(...)`

- Examples: `=SWITCH(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7013690

- Source fetch status: failed after 4 attempts

- Summary: Computes SWITCH semantics for spreadsheet formulas.

- Signatures:

  - `SWITCH(...)`

- Examples: `=SWITCH(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e
- Google Sheets: https://support.google.com/docs/answer/7013690
