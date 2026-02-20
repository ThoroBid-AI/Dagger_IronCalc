# TRANSPOSE
## TRANSPOSE
## Purpose
Computes TRANSPOSE semantics for spreadsheet formulas.
## Syntax
- Excel: `TRANSPOSE(...)`
- Google Sheets: `TRANSPOSE(...)`
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
- Proposed handler: `fn_transpose`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027

- Summary: How to use the TRANSPOSE function in Excel to switch or rotate cells.

- Signatures:

  - `TRANSPOSE(array)`

- Examples:

  - TRANSPOSE(A1:B4)

  - TRANSPOSE(array)

  - Transpose (rotate)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094262

- Summary: Transposes the rows and columns of an array or range of cells. Sample Usage TRANSPOSE({1,2;3,4;5,6}) TRANSPOSE(A2:F9) Syntax TRANSPOSE(array_or_range) array_or_range - The array or rang

- Signatures:

  - `TRANSPOSE(array_or_range)`

- Examples:

  - TRANSPOSE({1,2;3,4;5,6})

  - TRANSPOSE(A2:F9)

  - TRANSPOSE(array_or_range)

- Notes: - Transposition operates such that the value in the nth row and mth column will become the value in the mth row and nth column. E.g. the value in the fourth row and second column will be put into the second row and fourth column. The result of a transposition on a range of size m rows by n columns is therefore n rows by m columns.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027
- Google Sheets: https://support.google.com/docs/answer/3094262
