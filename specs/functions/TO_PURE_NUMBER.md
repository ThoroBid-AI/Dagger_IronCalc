# TO_PURE_NUMBER
## TO_PURE_NUMBER
## Purpose
Computes TO_PURE_NUMBER semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_PURE_NUMBER(...)`
- Google Sheets: `TO_PURE_NUMBER(...)`
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
- Proposed handler: `fn_to_pure_number`
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



- Source URL: https://support.google.com/docs/answer/3094243

- Summary: Converts a provided date/time, percentage, currency or other formatted numeric value to a pure number without formatting. Sample Usage TO_PURE_NUMBER(50%) TO_PURE_NUMBER(A2) Syntax TO_PURE_NUMBER

- Signatures:

  - `TO_PURE_NUMBER(value)`

- Examples:

  - TO_PURE_NUMBER(50%)

  - TO_PURE_NUMBER(A2)

  - TO_PURE_NUMBER(value)

- Notes: - TO_PURE_NUMBER is similar to applying Format -> Number -> Normal from the menu bar, except that the Normal format includes commas denoting thousands, millions, etc. - TO_PURE_NUMBER is similar to N, except that N returns 0 for non-numeric values except for TRUE which returns 1, whereas TO_PURE_NUMBER returns the value passed without modification for all non-numeric types.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094243
