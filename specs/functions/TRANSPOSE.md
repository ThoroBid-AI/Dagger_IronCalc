# TRANSPOSE
## TRANSPOSE
## Purpose
Computes TRANSPOSE semantics for spreadsheet formulas.
## Syntax
- Excel: `TRANSPOSE(...)`
- Google Sheets: `TRANSPOSE(...)`
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
- Proposed handler: `fn_transpose`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027

- Source fetch status: failed after 4 attempts

- Summary: Computes TRANSPOSE semantics for spreadsheet formulas.

- Signatures:

  - `TRANSPOSE(...)`

- Examples: `=TRANSPOSE(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094262

- Source fetch status: failed after 4 attempts

- Summary: Computes TRANSPOSE semantics for spreadsheet formulas.

- Signatures:

  - `TRANSPOSE(...)`

- Examples: `=TRANSPOSE(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027
- Google Sheets: https://support.google.com/docs/answer/3094262
