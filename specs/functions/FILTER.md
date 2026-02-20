# FILTER
## FILTER
## Purpose
Filters array values by condition.
## Syntax
- Excel: `FILTER(array, include, [if_empty])`
- Google Sheets: `FILTER(array, include, [if_empty])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `FILTER({1,2,3},{TRUE,FALSE,TRUE}) -> {1,3}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_filter`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `FILTER(array, include, [if_empty])`

- Examples:

  - FILTER({1,2,3},{TRUE,FALSE,TRUE})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093197

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `FILTER(array, include, [if_empty])`

- Examples:

  - FILTER({1,2,3},{TRUE,FALSE,TRUE})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759
- Google Sheets: https://support.google.com/docs/answer/3093197
