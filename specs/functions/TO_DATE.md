# TO_DATE
## TO_DATE
## Purpose
Computes TO_DATE semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_DATE(...)`
- Google Sheets: `TO_DATE(...)`
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
- Proposed handler: `fn_to_date`
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



- Source URL: https://support.google.com/docs/answer/3094239

- Summary: Converts a provided number to a date. Sample Usage TO_DATE(25405) TO_DATE(A2) TO_DATE(40826.4375) Syntax TO_DATE(value) value - The argument or reference to

- Signatures:

  - `TO_DATE(value)`

- Examples:

  - TO_DATE(25405)

  - TO_DATE(A2)

  - TO_DATE(40826.4375)

  - TO_DATE(value)

  - TO_DATE(10/10/2000)

  - TO_DATE(0.0005)

- Notes: - TO_DATE does not autoconvert number formats in the same way as direct entry into cells. Therefore, TO_DATE(10/10/2000) is interpreted as TO_DATE(0.0005), the quotient of 10 divided by 10 divided by 2000. - TO_DATE is not as commonly used as DATE, which takes a year, month, and day in numeric format as inputs. - TO_DATE is the inverse of N as applied to a date, and equivalent to applying Format Number Date time from the menu bar.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094239
