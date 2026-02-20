# SORT
## SORT
## Purpose
Sorts array by columns and order.
## Syntax
- Excel: `SORT(range, sort_index, [sort_order])`
- Google Sheets: `SORT(range, sort_index, [sort_order])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `SORT({{3,1},{2,0}}, 1, TRUE)`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_sort`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c

- Summary: Learn about the SORT function, which sorts the contents of a range or array. SORT is in a class of functions called dynamic arrays.

- Signatures:

  - `SORT(array,[sort_index],[sort_order],[by_col])`

- Examples:

  - SORT({{3,1},{2,0}}, 1, TRUE)

- Notes: array Required: The range, or array to sort | [sort_index] Optional: A number indicating the row or column to sort by | [sort_order] Optional: A number indicating the desired sort order; 1 for ascending order (default), -1 for descending order | [by_col] Optional: A logical value indicating the desired sort direction; FALSE to sort by row (default), TRUE to sort by column

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093150

- Summary: Sorts the rows of a given array or range by the values in one or more columns. Sample Usage SORT(A2:B26, 1, TRUE) SORT({1, 2; 3, 4; 5, 6}, 2, FALSE) SORT(A2:B26, C2:C26, TRUE) Syntax SORT(range,

- Signatures:

  - `SORT(range, sort_column, is_ascending, [sort_column2, is_ascending2, ...])`

- Examples:

  - SORT({{3,1},{2,0}}, 1, TRUE)

- Notes: - range is sorted only by the specified columns, other columns are returned in the order they originally appear.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c
- Google Sheets: https://support.google.com/docs/answer/3093150
