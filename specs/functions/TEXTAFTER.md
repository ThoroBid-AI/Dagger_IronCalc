# TEXTAFTER
## TEXTAFTER
## Purpose
Returns text after a delimiter.
## Syntax
- Excel: `TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end])`
- Google Sheets: `TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `TEXTAFTER("a,b,c",",") -> "b,c"`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_textafter`
- File: `base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/textafter-function-c8db2546-5b51-416a-9690-c7e6722e90b4

- Source fetch status: failed after 4 attempts

- Summary: Returns text after a delimiter.

- Signatures:

  - `TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end])`

- Examples:

  - TEXTAFTER("a,b,c",",")

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=TEXTAFTER

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/textafter-function-c8db2546-5b51-416a-9690-c7e6722e90b4
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=TEXTAFTER
