# VSTACK
## VSTACK
## Purpose
Stacks arrays vertically.
## Syntax
- Excel: `VSTACK(value1, value2, ...)`
- Google Sheets: `VSTACK(value1, value2, ...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- VSTACK({1,2},{3,4}) -> {{1,2},{3,4}}
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_vstack`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/vstack-function-a4b86897-be0f-48fc-adca-fcc10d795a9c

- Source fetch status: failed after 4 attempts

- Summary: Stacks arrays vertically.

- Signatures:

  - `VSTACK(value1, value2, ...)`

- Examples:

  - VSTACK({1,2},{3,4})

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13191461

- Source fetch status: failed after 4 attempts

- Summary: Stacks arrays vertically.

- Signatures:

  - `VSTACK(value1, value2, ...)`

- Examples:

  - VSTACK({1,2},{3,4})

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/vstack-function-a4b86897-be0f-48fc-adca-fcc10d795a9c
- Google Sheets: https://support.google.com/docs/answer/13191461
