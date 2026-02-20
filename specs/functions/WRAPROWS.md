# WRAPROWS
## WRAPROWS
## Purpose
Wraps a one-dimensional array into rows.
## Syntax
- Excel: `WRAPROWS(array, wrap_count, [pad_with])`
- Google Sheets: `WRAPROWS(array, wrap_count, [pad_with])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- WRAPROWS({1,2,3},2) -> {{1,3},{2}}
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_wraprows`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/wraprows-function-796825f3-975a-4cee-9c84-1bbddf60ade0

- Source fetch status: failed after 4 attempts

- Summary: Wraps a one-dimensional array into rows.

- Signatures:

  - `WRAPROWS(array, wrap_count, [pad_with])`

- Examples: `WRAPROWS(1,2,3)` -> `0`

  - WRAPROWS({1,2,3},2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13184285

- Source fetch status: failed after 4 attempts

- Summary: Wraps a one-dimensional array into rows.

- Signatures:

  - `WRAPROWS(array, wrap_count, [pad_with])`

- Examples: `WRAPROWS(1,2,3)` -> `0`

  - WRAPROWS({1,2,3},2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/wraprows-function-796825f3-975a-4cee-9c84-1bbddf60ade0
- Google Sheets: https://support.google.com/docs/answer/13184285
