# TO_PERCENT
## TO_PERCENT
## Purpose
Computes TO_PERCENT semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_PERCENT(...)`
- Google Sheets: `TO_PERCENT(...)`
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
- Proposed handler: `fn_to_percent`
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



- Source URL: https://support.google.com/docs/answer/3094284

- Summary: Converts a provided number to a percentage. Sample Usage TO_PERCENT(A2) TO_PERCENT(0.40826) Syntax TO_PERCENT(value) value - The argument or reference to a cell to be converted

- Signatures:

  - `TO_PERCENT(value)`

- Examples:

  - TO_PERCENT(A2)

  - TO_PERCENT(0.40826)

  - TO_PERCENT(value)

- Notes: - Because dates and percentages are both numbers, TO_PERCENT will convert dates to percentages successfully. However, these conversions are not typically meaningful. - TO_PERCENT is equivalent to clicking Format Number Percent from the menu bar.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094284
