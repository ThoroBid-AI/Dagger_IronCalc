# UNIQUE
## UNIQUE
## Purpose
Returns unique values from array.
## Syntax
- Excel: `UNIQUE(range_or_array, [by_col], [exactly_once])`
- Google Sheets: `UNIQUE(range_or_array, [by_col], [exactly_once])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `UNIQUE({1,2,1}) -> {1,2}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_unique`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `UNIQUE(range_or_array, [by_col], [exactly_once])`

- Examples:

  - UNIQUE({1,2,1})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/10522653

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `UNIQUE(range_or_array, [by_col], [exactly_once])`

- Examples:

  - UNIQUE({1,2,1})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e
- Google Sheets: https://support.google.com/docs/answer/10522653
