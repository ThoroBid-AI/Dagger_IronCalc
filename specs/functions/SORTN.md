# SORTN
## SORTN
## Purpose
Computes SORTN semantics for spreadsheet formulas.
## Syntax
- Excel: `SORTN(...)`
- Google Sheets: `SORTN(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sortn`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples: No examples captured from source page or local docs.

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7354624

- Summary: Returns the first n items in a data set after performing a sort. Sample Usage SORTN(A1:A10, 2) SORTN(A2:C20, 2, 2, B2:B20, TRUE) SORTN(A2:C20, 2, 3, B2:B20, TRUE, 3, FALSE) Syntax SORTN(range, [

- Signatures:

  - `SORTN(range, [n], [display_ties_mode], [sort_column1, is_ascending1], ...)`

- Examples: The following table is used for the examples below. A B C 1 Student Test 1 score Test 2 score 2 Alice 100 90 3 Bob 75 85 4 Carol 80 85 5 Devon 100 95 6 Eloise 80 90 Formula Result =SORTN(A2:C6) Alice 100 90 =SORTN(A2:C6, 2) Alice 100 90 Bob 75 85 =SORTN(A2:C6, 3, 0, B2:B6, FALSE) Alice 100 90 Devon 100 95 Carol 80 85 =SORTN(A2:C6, 3, 1, B2:B6, FALSE) Alice 100 90 Devon 100 95 Carol 80 85 Eloise 80 90 =SORTN(A2:C6, 3, 2, B2:B6, FALSE) Alice 100 90 Carol 80 85 Bob 75 85 =SORTN(A2:C6, 3, 3, B2:B6, FALSE) Alice 100 90 Devon 100 95 Carol 80 85 Eloise 80 90 Bob 75 85 =SORTN(A2:C6, 3, 3, 2, FALSE, 3, FALSE) Devon 100 95 Alice 100 90 Eloise 80 90

- Notes: - range is sorted only by the specified columns. Other columns are returned in the order they originally appear. - If sort_column1 and is_ascending1 aren't included, the sort is performed on the lowest-index column in range, with subsequent columns used to sort if there are ties.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/7354624
