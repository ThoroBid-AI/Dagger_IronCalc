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

- Source fetch status: failed after 4 attempts

- Summary: Sorts array by columns and order.

- Signatures:

  - `SORT(range, sort_index, [sort_order])`

- Examples:

  - SORT({{3,1},{2,0}}, 1, TRUE)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093150

- Source fetch status: failed after 4 attempts

- Summary: Sorts array by columns and order.

- Signatures:

  - `SORT(range, sort_index, [sort_order])`

- Examples:

  - SORT({{3,1},{2,0}}, 1, TRUE)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c
- Google Sheets: https://support.google.com/docs/answer/3093150
