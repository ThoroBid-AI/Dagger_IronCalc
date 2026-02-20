# UMINUS
## UMINUS
## Purpose
Computes UMINUS semantics for spreadsheet formulas.
## Syntax
- Excel: `UMINUS(...)`
- Google Sheets: `UMINUS(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_uminus`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Computes UMINUS semantics for spreadsheet formulas.

- Signatures:

  - `UMINUS(...)`

- Examples: `=UMINUS(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093606

- Source fetch status: failed after 4 attempts

- Summary: Computes UMINUS semantics for spreadsheet formulas.

- Signatures:

  - `UMINUS(...)`

- Examples: `=UMINUS(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093606
