# STDEV.P
## STDEV.P
## Purpose
Computes STDEV.P semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEV.P(...)`
- Google Sheets: `STDEV.P(...)`
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
- Proposed handler: `fn_stdev.p`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEV.P semantics for spreadsheet formulas.

- Signatures:

  - `STDEV.P(...)`

- Examples: `=STDEV.P(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094105

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEV.P semantics for spreadsheet formulas.

- Signatures:

  - `STDEV.P(...)`

- Examples: `=STDEV.P(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195
- Google Sheets: https://support.google.com/docs/answer/3094105
