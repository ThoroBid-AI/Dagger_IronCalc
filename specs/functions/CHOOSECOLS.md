# CHOOSECOLS
## CHOOSECOLS
## Purpose
Returns selected columns from an array.
## Syntax
- Excel: `CHOOSECOLS(array, col_num1, ...)`
- Google Sheets: `CHOOSECOLS(array, col_num1, ...)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `CHOOSECOLS({{1,2,3},{4,5,6}},2) -> {2,5}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_choosecols`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/choosecols-function-bf117976-2722-4466-9b9a-1c01ed9aebff

- Source fetch status: failed after 4 attempts

- Summary: Returns selected columns from an array.

- Signatures:

  - `CHOOSECOLS(array, col_num1, ...)`

- Examples:

  - CHOOSECOLS({{1,2,3},{4,5,6}},2)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13197914

- Source fetch status: failed after 4 attempts

- Summary: Returns selected columns from an array.

- Signatures:

  - `CHOOSECOLS(array, col_num1, ...)`

- Examples:

  - CHOOSECOLS({{1,2,3},{4,5,6}},2)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/choosecols-function-bf117976-2722-4466-9b9a-1c01ed9aebff
- Google Sheets: https://support.google.com/docs/answer/13197914
