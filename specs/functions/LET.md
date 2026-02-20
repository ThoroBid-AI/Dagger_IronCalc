# LET
## LET
## Purpose
Assigns names to intermediate values in formulas.
## Syntax
- Excel: `LET(name1, value1, ... , calculation)`
- Google Sheets: `LET(name1, value1, ... , calculation)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `LET(x,1,y,2,x+y)`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_let`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999

- Source fetch status: failed after 4 attempts

- Summary: Assigns names to intermediate values in formulas.

- Signatures:

  - `LET(name1, value1, ... , calculation)`

- Examples:

  - LET(x,1,y,2,x+y)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13190535

- Source fetch status: failed after 4 attempts

- Summary: Assigns names to intermediate values in formulas.

- Signatures:

  - `LET(name1, value1, ... , calculation)`

- Examples:

  - LET(x,1,y,2,x+y)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999
- Google Sheets: https://support.google.com/docs/answer/13190535
