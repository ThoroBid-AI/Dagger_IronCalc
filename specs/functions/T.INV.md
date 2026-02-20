# T.INV
## T.INV
## Purpose
Computes T.INV semantics for spreadsheet formulas.
## Syntax
- Excel: `T.INV(...)`
- Google Sheets: `T.INV(...)`
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
- Proposed handler: `fn_t.inv`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tinv-function-a7c85b9d-90f5-41fe-9ca5-1cd2f3e1ed7c

- Source fetch status: failed after 4 attempts

- Summary: Computes T.INV semantics for spreadsheet formulas.

- Signatures:

  - `T.INV(...)`

- Examples: `=T.INV(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055811

- Source fetch status: failed after 4 attempts

- Summary: Computes T.INV semantics for spreadsheet formulas.

- Signatures:

  - `T.INV(...)`

- Examples: `=T.INV(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tinv-function-a7c85b9d-90f5-41fe-9ca5-1cd2f3e1ed7c
- Google Sheets: https://support.google.com/docs/answer/6055811
