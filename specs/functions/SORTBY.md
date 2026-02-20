# SORTBY
## SORTBY
## Purpose
Sorts range by sort keys.
## Syntax
- Excel: `SORTBY(range, sort_key1, [sort_order1], ...)`
- Google Sheets: `SORTBY(range, sort_key1, [sort_order1], ...)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `SORTBY({{3,1},{2,0}}, {2,1})`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_sortby`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sortby-function-cd2d7a62-1b93-435c-b561-d6a35134f28f

- Source fetch status: failed after 4 attempts

- Summary: Sorts range by sort keys.

- Signatures:

  - `SORTBY(range, sort_key1, [sort_order1], ...)`

- Examples: `=SORTBY(1, 2, 3)` -> `0`

  - SORTBY({{3,1},{2,0}}, {2,1})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=SORTBY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: `=SORTBY(1, 2, 3)` -> `0`

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sortby-function-cd2d7a62-1b93-435c-b561-d6a35134f28f
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=SORTBY
