# TOROW
## TOROW
## Purpose
Computes TOROW semantics for spreadsheet formulas.
## Syntax
- Excel: `TOROW(...)`
- Google Sheets: `TOROW(...)`
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
- Proposed handler: `fn_torow`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289

- Source fetch status: failed after 4 attempts

- Summary: Computes TOROW semantics for spreadsheet formulas.

- Signatures:

  - `TOROW(...)`

- Examples: `=TOROW(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13187459

- Source fetch status: failed after 4 attempts

- Summary: Computes TOROW semantics for spreadsheet formulas.

- Signatures:

  - `TOROW(...)`

- Examples: `=TOROW(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289
- Google Sheets: https://support.google.com/docs/answer/13187459
