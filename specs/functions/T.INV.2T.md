# T.INV.2T
## T.INV.2T
## Purpose
Computes T.INV.2T semantics for spreadsheet formulas.
## Syntax
- Excel: `T.INV.2T(...)`
- Google Sheets: `T.INV.2T(...)`
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
- Proposed handler: `fn_t.inv.2t`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-inv-2t-function-ce72ea19-ec6c-4be7-bed2-b9baf2264f17

- Source fetch status: failed after 4 attempts

- Summary: Computes T.INV.2T semantics for spreadsheet formulas.

- Signatures:

  - `T.INV.2T(...)`

- Examples: `=T.INV.2T(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055811

- Source fetch status: failed after 4 attempts

- Summary: Computes T.INV.2T semantics for spreadsheet formulas.

- Signatures:

  - `T.INV.2T(...)`

- Examples: `=T.INV.2T(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-inv-2t-function-ce72ea19-ec6c-4be7-bed2-b9baf2264f17
- Google Sheets: https://support.google.com/docs/answer/6055811
