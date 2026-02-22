# TOCOL
## TOCOL
## Purpose
Computes TOCOL semantics for spreadsheet formulas.
## Syntax
- Excel: `TOCOL(...)`
- Google Sheets: `TOCOL(...)`
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
- Proposed handler: `fn_tocol`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed

- Summary: Computes TOCOL semantics for spreadsheet formulas.

- Signatures:

  - `TOCOL(array, [ignore], [scan_by_column])`

- Examples:

  - TOCOL(array, [ignore], [scan_by_column])

- Notes: Current Channel Monthly Enterprise Channel Semi-Annual Enterprise Channel Semi-Annual Enterprise Channel (Preview) Office for Mac Returns the array in a single column.

- Error behavior: - Excel returns a #VALUE! when an array constant contains one or more numbers that are not a whole number. - Excel returns a #NUM when array is too large.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13187258

- Summary: This function transforms an array or range of cells into a single column. TOCOL can scan values: By column, top to bottom By row, left to right The scan_by_column argument is a boolean value t

- Signatures:

  - `TOCOL(array_or_range, [ignore], [scan_by_column])`

- Examples:

  - TOCOL(A1:C3)

  - TOCOL(A1:C3, 1, TRUE)

  - TOCOL(array_or_range, [ignore], [scan_by_column])

  - TOCOL(A1:C3, 1)

  - TOCOL(A1:C3, 0, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed
- Google Sheets: https://support.google.com/docs/answer/13187258
