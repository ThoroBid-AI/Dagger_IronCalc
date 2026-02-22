# WRAPCOLS
## WRAPCOLS
## Purpose
Wraps a one-dimensional array into columns.
## Syntax
- Excel: `WRAPCOLS(array, wrap_count, [pad_with])`
- Google Sheets: `WRAPCOLS(array, wrap_count, [pad_with])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- WRAPCOLS({1,2,3},2) -> {{1,2},{3}}
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_wrapcols`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/wrapcols-function-d038b05a-57b7-4ee0-be94-ded0792511e2

- Source fetch status: failed after 4 attempts

- Summary: Wraps a one-dimensional array into columns.

- Signatures:

  - `WRAPCOLS(array, wrap_count, [pad_with])`

- Examples:

  - WRAPCOLS({1,2,3},2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13184284

- Source fetch status: failed after 4 attempts

- Summary: Wraps a one-dimensional array into columns.

- Signatures:

  - `WRAPCOLS(array, wrap_count, [pad_with])`

- Examples:

  - WRAPCOLS({1,2,3},2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/wrapcols-function-d038b05a-57b7-4ee0-be94-ded0792511e2
- Google Sheets: https://support.google.com/docs/answer/13184284
