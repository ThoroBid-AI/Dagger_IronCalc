# QUERY
## QUERY
## Purpose
Runs SQL-like query on arrays.
## Syntax
- Excel: `QUERY(data, query, [headers])`
- Google Sheets: `QUERY(data, query, [headers])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `QUERY({{1,2};{3,4}}, "select Col1")`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_query`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Runs SQL-like query on arrays.

- Signatures:

  - `QUERY(data, query, [headers])`

- Examples:

  - QUERY({{1,2};{3,4}}, "select Col1")

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093343

- Source fetch status: failed after 4 attempts

- Summary: Runs SQL-like query on arrays.

- Signatures:

  - `QUERY(data, query, [headers])`

- Examples:

  - QUERY({{1,2};{3,4}}, "select Col1")

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093343
