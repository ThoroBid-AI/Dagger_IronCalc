# BYROW
## BYROW
## Purpose
Applies a lambda across each row in an array.
## Syntax
- Excel: `BYROW(array, lambda)`
- Google Sheets: `BYROW(array, lambda)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `BYROW({{1,2},{3,4}}, LAMBDA(r, SUM(r))) -> {3,7}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_byrow`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/byrow-function-2e04c677-78c8-4e6b-8c10-a4602f2602bb

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BYROW(array, lambda)`

- Examples:

  - BYROW({{1,2},{3,4}}, LAMBDA(r, SUM(r)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12570930

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BYROW(array, lambda)`

- Examples:

  - BYROW({{1,2},{3,4}}, LAMBDA(r, SUM(r)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/byrow-function-2e04c677-78c8-4e6b-8c10-a4602f2602bb
- Google Sheets: https://support.google.com/docs/answer/12570930
