# VLOOKUP
## VLOOKUP
## Purpose
Computes VLOOKUP behavior for spreadsheet formulas.
## Syntax
- Excel: `VLOOKUP(...)`
- Google Sheets: `VLOOKUP(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_vlookup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1

- Source fetch status: failed after 4 attempts

- Summary: Computes VLOOKUP behavior for spreadsheet formulas.

- Signatures:

  - `VLOOKUP(...)`

- Examples: `=VLOOKUP(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093318

- Source fetch status: failed after 4 attempts

- Summary: Computes VLOOKUP behavior for spreadsheet formulas.

- Signatures:

  - `VLOOKUP(...)`

- Examples: `=VLOOKUP(1)` -> `0`

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1
- Google Sheets: https://support.google.com/docs/answer/3093318
