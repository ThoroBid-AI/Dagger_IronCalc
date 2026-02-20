# SUMPRODUCT
## SUMPRODUCT
## Purpose
Computes SUMPRODUCT semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMPRODUCT(...)`
- Google Sheets: `SUMPRODUCT(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_sumproduct`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMPRODUCT semantics for spreadsheet formulas.

- Signatures:

  - `SUMPRODUCT(...)`

- Examples: `=SUMPRODUCT(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094294

- Source fetch status: failed after 4 attempts

- Summary: Computes SUMPRODUCT semantics for spreadsheet formulas.

- Signatures:

  - `SUMPRODUCT(...)`

- Examples: `=SUMPRODUCT(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e
- Google Sheets: https://support.google.com/docs/answer/3094294
