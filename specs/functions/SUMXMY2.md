# SUMXMY2
## SUMXMY2
## Purpose
Computes SUMXMY2 semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMXMY2(...)`
- Google Sheets: `SUMXMY2(...)`
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
- Handler: `fn_sumxmy2`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumxmy2-function-9d144ac1-4d79-43de-b524-e2ecee23b299

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMXMY2 semantics for spreadsheet formulas.

- Signatures:

  - `SUMXMY2(...)`

- Examples: `=SUMXMY2(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094298

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMXMY2 semantics for spreadsheet formulas.

- Signatures:

  - `SUMXMY2(...)`

- Examples: `=SUMXMY2(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumxmy2-function-9d144ac1-4d79-43de-b524-e2ecee23b299
- Google Sheets: https://support.google.com/docs/answer/3094298
