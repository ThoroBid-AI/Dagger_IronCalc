# TRIMMEAN
## TRIMMEAN
## Purpose
Computes TRIMMEAN semantics for spreadsheet formulas.
## Syntax
- Excel: `TRIMMEAN(...)`
- Google Sheets: `TRIMMEAN(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_trimmean`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/trimmean-function-d90c9878-a119-4746-88fa-63d988f511d3

- Source fetch status: failed after 4 attempts

- Summary: Computes TRIMMEAN semantics for spreadsheet formulas.

- Signatures:

  - `TRIMMEAN(...)`

- Examples: `=TRIMMEAN(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094061

- Source fetch status: failed after 4 attempts

- Summary: Computes TRIMMEAN semantics for spreadsheet formulas.

- Signatures:

  - `TRIMMEAN(...)`

- Examples: `=TRIMMEAN(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trimmean-function-d90c9878-a119-4746-88fa-63d988f511d3
- Google Sheets: https://support.google.com/docs/answer/3094061
