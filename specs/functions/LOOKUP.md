# LOOKUP
## LOOKUP
## Purpose
Looks up value in one-row or one-column array.
## Syntax
- Excel: `LOOKUP(lookup_value, lookup_array, [result_array])`
- Google Sheets: `LOOKUP(lookup_value, lookup_array, [result_array])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `LOOKUP(2,{1,2,3},{10,20,30}) -> 20`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_lookup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible date arithmetic.

- Signatures:

  - `LOOKUP(lookup_value, lookup_array, [result_array])`

- Examples:

  - LOOKUP(2,{1,2,3},{10,20,30})

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3256570

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible date arithmetic.

- Signatures:

  - `LOOKUP(lookup_value, lookup_array, [result_array])`

- Examples:

  - LOOKUP(2,{1,2,3},{10,20,30})

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb
- Google Sheets: https://support.google.com/docs/answer/3256570
