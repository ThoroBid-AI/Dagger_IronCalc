# CHOOSEROWS
## CHOOSEROWS
## Purpose
Returns selected rows from an array.
## Syntax
- Excel: `CHOOSEROWS(array, row_num1, ...)`
- Google Sheets: `CHOOSEROWS(array, row_num1, ...)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `CHOOSEROWS({{1,2,3},{4,5,6}},2) -> {4,5,6}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_chooserows`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/chooserows-function-51ace882-9bab-4a44-9625-7274ef7507a3

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CHOOSEROWS(array, row_num1, ...)`

- Examples:

  - CHOOSEROWS({{1,2,3},{4,5,6}},2)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13196659

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CHOOSEROWS(array, row_num1, ...)`

- Examples:

  - CHOOSEROWS({{1,2,3},{4,5,6}},2)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/chooserows-function-51ace882-9bab-4a44-9625-7274ef7507a3
- Google Sheets: https://support.google.com/docs/answer/13196659
