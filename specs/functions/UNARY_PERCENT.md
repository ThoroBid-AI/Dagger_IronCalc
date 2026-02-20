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

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples: No examples captured from source page or local docs.

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093982

- Summary: Returns a value interpreted as a percentage; that is, `UNARY_PERCENT(100)` equals `1`. Sample Usage UNARY_PERCENT(A2) UNARY_PERCENT(93) Syntax UNARY_PERCENT(percentage) percentage - The

- Signatures:

  - `UNARY_PERCENT(percentage)`

- Examples:

  - UNARY_PERCENT(100)

  - UNARY_PERCENT(A2)

  - UNARY_PERCENT(93)

  - UNARY_PERCENT(percentage)

- Notes: - UNARY_PERCENT is roughly equivalent to the inverse of TO_PERCENT.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093982
