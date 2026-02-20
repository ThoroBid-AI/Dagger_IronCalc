# XLOOKUP
## XLOOKUP
## Purpose
Searches a range for a match and returns corresponding value.
## Syntax
- Excel: `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])`
- Google Sheets: `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `XLOOKUP("B", {"A","B","C"}, {1,2,3}) -> 2`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_xlookup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/xlookup.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929

- Source fetch status: failed after 4 attempts

- Summary: Searches a range for a match and returns corresponding value.

- Signatures:

  - `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])`

- Examples:

  - XLOOKUP("B", {"A","B","C"}, {1,2,3})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12405947

- Source fetch status: failed after 4 attempts

- Summary: Searches a range for a match and returns corresponding value.

- Signatures:

  - `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])`

- Examples:

  - XLOOKUP("B", {"A","B","C"}, {1,2,3})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929
- Google Sheets: https://support.google.com/docs/answer/12405947
