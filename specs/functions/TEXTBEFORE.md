# TEXTBEFORE
## TEXTBEFORE
## Purpose
Returns text before a delimiter.
## Syntax
- Excel: `TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end])`
- Google Sheets: `TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `TEXTBEFORE("a,b,c",",") -> "a"`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_textbefore`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/textbefore-function-d099c28a-dba8-448e-ac6c-f086d0fa1b29

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end])`

- Examples:

  - TEXTBEFORE("a,b,c",",")

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=TEXTBEFORE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/textbefore-function-d099c28a-dba8-448e-ac6c-f086d0fa1b29
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=TEXTBEFORE
