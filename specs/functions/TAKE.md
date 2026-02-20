# TAKE
## TAKE
## Purpose
Computes TAKE semantics for spreadsheet formulas.
## Syntax
- Excel: `TAKE(...)`
- Google Sheets: `TAKE(...)`
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
- Proposed handler: `fn_take`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/take-function-25382ff1-5da1-4f78-ab43-f33bd2e4e003

- Summary: Computes TAKE semantics for spreadsheet formulas.

- Signatures:

  - `TAKE(array, rows,[columns])`

- Examples:
  - `=TAKE(1, 2)`,
  - `=TAKE(A1, B1)`,
  - `=TAKE(10, 20, 30)`,
- Notes: Current Channel Monthly Enterprise Channel Semi-Annual Enterprise Channel Semi-Annual Enterprise Channel (Preview) Office for Mac Returns a specified number of contiguous rows or columns from the start or end of an array.

- Error behavior: - Excel returns a #CALC! error to indicate an empty array when either rows or columns is 0. - Excel returns a #NUM when array is too large.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=TAKE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/take-function-25382ff1-5da1-4f78-ab43-f33bd2e4e003
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=TAKE
