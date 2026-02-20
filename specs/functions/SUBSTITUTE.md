# SUBSTITUTE
## SUBSTITUTE
## Purpose
Computes SUBSTITUTE semantics for spreadsheet formulas.
## Syntax
- Excel: `SUBSTITUTE(...)`
- Google Sheets: `SUBSTITUTE(...)`
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
- Handler: `fn_substitute`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332

- Source fetch status: failed after 4 attempts

- Summary: Computes SUBSTITUTE semantics for spreadsheet formulas.

- Signatures:

  - `SUBSTITUTE(...)`

- Examples: `=SUBSTITUTE(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094215

- Source fetch status: failed after 4 attempts

- Summary: Computes SUBSTITUTE semantics for spreadsheet formulas.

- Signatures:

  - `SUBSTITUTE(...)`

- Examples: `=SUBSTITUTE(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332
- Google Sheets: https://support.google.com/docs/answer/3094215
