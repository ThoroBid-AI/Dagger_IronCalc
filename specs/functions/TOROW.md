# TOROW
## TOROW
## Purpose
Computes TOROW semantics for spreadsheet formulas.
## Syntax
- Excel: `TOROW(...)`
- Google Sheets: `TOROW(...)`
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
- Proposed handler: `fn_torow`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289

- Summary: Computes TOROW semantics for spreadsheet formulas.

- Signatures:

  - `TOROW(array, [ignore], [scan_by_column])`

- Examples:

  - TOROW(array, [ignore], [scan_by_column])

- Notes: Current Channel Monthly Enterprise Channel Semi-Annual Enterprise Channel Semi-Annual Enterprise Channel (Preview) Office for Mac Returns the array in a single row.

- Error behavior: - Excel returns a #VALUE! when an array constant contains one or more numbers that are not a whole number. - Excel returns a #NUM when array is too large.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13187459

- Summary: This function transforms an array or range of cells into a single row. TOROW can scan values: By column, top to bottom By row, left to right The scan_by_column argument is a boolean value that

- Signatures:

  - `TOROW(array_or_range, [ignore], [scan_by_column])`

- Examples:

  - TOROW(A1:C3)

  - TOROW(A1:C3, 1, TRUE)

  - TOROW(array_or_range, [ignore], [scan_by_column])

  - TOROW(A1:C3, 1)

  - TOROW(A1:C3, 0, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289
- Google Sheets: https://support.google.com/docs/answer/13187459
