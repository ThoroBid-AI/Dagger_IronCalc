# STDEVPA
## STDEVPA
## Purpose
Computes STDEVPA semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEVPA(...)`
- Google Sheets: `STDEVPA(...)`
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
- Handler: `fn_stdevpa`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEVPA semantics for spreadsheet formulas.

- Signatures:

  - `STDEVPA(...)`

- Examples: `=STDEVPA(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094058

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEVPA semantics for spreadsheet formulas.

- Signatures:

  - `STDEVPA(...)`

- Examples: `=STDEVPA(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c
- Google Sheets: https://support.google.com/docs/answer/3094058
