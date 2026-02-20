# TEXTSPLIT
## TEXTSPLIT
## Purpose
Splits text into array by delimiter.
## Syntax
- Excel: `TEXTSPLIT(text, delimiter)`
- Google Sheets: `TEXTSPLIT(text, delimiter)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `TEXTSPLIT("a,b,c",",") -> {a,b,c}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_textsplit`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `TEXTSPLIT(text, delimiter)`

- Examples:

  - TEXTSPLIT("a,b,c",",")

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=TEXTSPLIT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=TEXTSPLIT
