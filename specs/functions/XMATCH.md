# XMATCH
## XMATCH
## Purpose
Returns relative position of item in array.
## Syntax
- Excel: `XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])`
- Google Sheets: `XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `XMATCH("B", {"A","B","C"}) -> 2`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_xmatch`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/xmatch-function-d966da31-7a6b-4a13-a1c6-5a33ed6a0312

- Source fetch status: failed after 4 attempts

- Summary: Returns relative position of item in array.

- Signatures:

  - `XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])`

- Examples: `XMATCH(1,2,3)` -> `0`

  - XMATCH("B", {"A","B","C"})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=XMATCH

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: `XMATCH(1,2,3)` -> `0`

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xmatch-function-d966da31-7a6b-4a13-a1c6-5a33ed6a0312
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=XMATCH
