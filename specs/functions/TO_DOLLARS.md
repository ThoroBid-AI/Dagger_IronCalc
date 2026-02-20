# TO_DOLLARS
## TO_DOLLARS
## Purpose
Computes TO_DOLLARS semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_DOLLARS(...)`
- Google Sheets: `TO_DOLLARS(...)`
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
- Proposed handler: `fn_to_dollars`
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



- Source URL: https://support.google.com/docs/answer/3094241

- Summary: Converts a provided number to a dollar value. Sample Usage TO_DOLLARS(A2) TO_DOLLARS(40826.43) Syntax TO_DOLLARS(value) value - The argument or reference to a cell to be convert

- Signatures:

  - `TO_DOLLARS(value)`

- Examples:

  - TO_DOLLARS(A2)

  - TO_DOLLARS(40826.43)

  - TO_DOLLARS(value)

- Notes: - Because dates and percentages are backed by numbers, TO_DOLLARS will convert them successfully. However, these conversions are not typically meaningful. - TO_DOLLARS is equivalent to applying Format -> Number -> Currency from the menu bar. - TO_DOLLARS differs from the related function DOLLAR in that DOLLAR outputs text rather than applying a cell format to a number. - TO_DOLLARS does not convert from other currencies into US Dollars. Please use the GoogleFinance function to convert currencies at current exchange rates.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094241
