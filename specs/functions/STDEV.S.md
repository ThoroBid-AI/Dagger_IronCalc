# STDEV.S
## STDEV.S
## Purpose
Computes STDEV.S semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEV.S(...)`
- Google Sheets: `STDEV.S(...)`
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
- Proposed handler: `fn_stdev.s`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEV.S semantics for spreadsheet formulas.

- Signatures:

  - `STDEV.S(...)`

- Examples: `=STDEV.S(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094054

- Source fetch status: failed after 4 attempts

- Summary: Computes STDEV.S semantics for spreadsheet formulas.

- Signatures:

  - `STDEV.S(...)`

- Examples: `=STDEV.S(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23
- Google Sheets: https://support.google.com/docs/answer/3094054
