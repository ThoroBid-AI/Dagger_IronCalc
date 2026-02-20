# TO_TEXT
## TO_TEXT
## Purpose
Computes TO_TEXT semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_TEXT(...)`
- Google Sheets: `TO_TEXT(...)`
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
- Proposed handler: `fn_to_text`
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



- Source URL: https://support.google.com/docs/answer/3094285

- Summary: Converts a provided numeric value to a text value. Sample Usage TO_TEXT(24) TO_TEXT(A2) Syntax TO_TEXT(value) value - The argument or reference to a cell to be converted to text

- Signatures:

  - `TO_TEXT(value)`

- Examples:

  - TO_TEXT(24)

  - TO_TEXT(A2)

  - TO_TEXT(value)

- Notes: - TO_TEXT is equivalent to prefixing a number with an apostrophe (')

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094285
