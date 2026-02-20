# BYCOL
## BYCOL
## Purpose
Applies a lambda across each column in an array.
## Syntax
- Excel: `BYCOL(array, lambda)`
- Google Sheets: `BYCOL(array, lambda)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `BYCOL({{1,2},{3,4}}, LAMBDA(c, SUM(c))) -> {3,7}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_bycol`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bycol-function-58463999-7de5-49ce-8f38-b7f7a2192bfb

- Source fetch status: failed after 4 attempts

- Summary: Applies a lambda across each column in an array.

- Signatures:

  - `BYCOL(array, lambda)`

- Examples:

  - BYCOL({{1,2},{3,4}}, LAMBDA(c, SUM(c)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12571032

- Source fetch status: failed after 4 attempts

- Summary: Applies a lambda across each column in an array.

- Signatures:

  - `BYCOL(array, lambda)`

- Examples:

  - BYCOL({{1,2},{3,4}}, LAMBDA(c, SUM(c)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bycol-function-58463999-7de5-49ce-8f38-b7f7a2192bfb
- Google Sheets: https://support.google.com/docs/answer/12571032
