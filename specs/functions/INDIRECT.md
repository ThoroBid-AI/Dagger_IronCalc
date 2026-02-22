# INDIRECT
## INDIRECT
## Purpose
Returns range reference from text.
## Syntax
- Excel: `INDIRECT(ref_text, [a1])`
- Google Sheets: `INDIRECT(ref_text, [a1])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `INDIRECT("A1")` resolves reference
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_indirect`
- File: `base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/indirect-function-474b3a3a-8a26-4f44-b491-92b6306fa261

- Source fetch status: failed after 4 attempts

- Summary: Returns range reference from text.

- Signatures:

  - `INDIRECT(ref_text, [a1])`

- Examples:

  - INDIRECT("A1")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093377

- Source fetch status: failed after 4 attempts

- Summary: Returns range reference from text.

- Signatures:

  - `INDIRECT(ref_text, [a1])`

- Examples:

  - INDIRECT("A1")

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/indirect-function-474b3a3a-8a26-4f44-b491-92b6306fa261
- Google Sheets: https://support.google.com/docs/answer/3093377
