# OFFSET
## OFFSET
## Purpose
Returns range offset from a reference.
## Syntax
- Excel: `OFFSET(reference, rows, cols, [height], [width])`
- Google Sheets: `OFFSET(reference, rows, cols, [height], [width])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `OFFSET(A1,1,1,2,1)`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_offset`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/offset-function-c8de19ae-dd79-4b9b-a14e-b4d906d11b66

- Source fetch status: failed after 4 attempts

- Summary: Returns range offset from a reference.

- Signatures:

  - `OFFSET(reference, rows, cols, [height], [width])`

- Examples:

  - OFFSET(A1,1,1,2,1)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093379

- Source fetch status: failed after 4 attempts

- Summary: Returns range offset from a reference.

- Signatures:

  - `OFFSET(reference, rows, cols, [height], [width])`

- Examples:

  - OFFSET(A1,1,1,2,1)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/offset-function-c8de19ae-dd79-4b9b-a14e-b4d906d11b66
- Google Sheets: https://support.google.com/docs/answer/3093379
