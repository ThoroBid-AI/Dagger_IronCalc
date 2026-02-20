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

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples: No examples captured from source page or local docs.

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093606

- Summary: Returns a number with the sign reversed. Sample Usage UMINUS(-4) UMINUS(A2) Syntax UMINUS(value) value - The number to have its sign reversed. Equivalently, the number to multiply by

- Signatures:

  - `UMINUS(value)`

- Examples:

  - UMINUS(-4)

  - UMINUS(A2)

  - UMINUS(value)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093606
