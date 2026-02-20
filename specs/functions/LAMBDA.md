# LAMBDA
## LAMBDA
## Purpose
Defines reusable inline function.
## Syntax
- Excel: `LAMBDA(parameters, calculation)`
- Google Sheets: `LAMBDA(parameters, calculation)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `LAMBDA(x, x+1)`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_lambda`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67

- Source fetch status: failed after 4 attempts

- Summary: Defines reusable inline function.

- Signatures:

  - `LAMBDA(parameters, calculation)`

- Examples:

  - LAMBDA(x, x+1)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12508718

- Source fetch status: failed after 4 attempts

- Summary: Defines reusable inline function.

- Signatures:

  - `LAMBDA(parameters, calculation)`

- Examples:

  - LAMBDA(x, x+1)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67
- Google Sheets: https://support.google.com/docs/answer/12508718
