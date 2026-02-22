# SEQUENCE
## SEQUENCE
## Purpose
Generates sequential numeric array.
## Syntax
- Excel: `SEQUENCE(rows, [columns], [start], [step])`
- Google Sheets: `SEQUENCE(rows, [columns], [start], [step])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `SEQUENCE(3,1) -> {1,2,3}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sequence`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90

- Source fetch status: failed after 4 attempts

- Summary: Generates sequential numeric array.

- Signatures:

  - `SEQUENCE(rows, [columns], [start], [step])`

- Examples:

  - SEQUENCE(3,1)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368244

- Source fetch status: failed after 4 attempts

- Summary: Generates sequential numeric array.

- Signatures:

  - `SEQUENCE(rows, [columns], [start], [step])`

- Examples:

  - SEQUENCE(3,1)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90
- Google Sheets: https://support.google.com/docs/answer/9368244
