# UNARY_PERCENT
## UNARY_PERCENT
## Purpose
Computes UNARY_PERCENT semantics for spreadsheet formulas.
## Syntax
- Excel: `UNARY_PERCENT(...)`
- Google Sheets: `UNARY_PERCENT(...)`
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
- Proposed handler: `fn_unary_percent`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `UNARY_PERCENT(...)`

- Examples: No examples available for this function.

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3093982

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `UNARY_PERCENT(...)`

- Examples:
  - `=UNARY_PERCENT(1, 2)`,
  - `=UNARY_PERCENT(A1, B1)`,
  - `=UNARY_PERCENT(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093982
