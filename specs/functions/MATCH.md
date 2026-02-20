# MATCH
## MATCH
## Purpose
Returns position of value within array.
## Syntax
- Excel: `MATCH(lookup_value, lookup_array, [match_type])`
- Google Sheets: `MATCH(lookup_value, lookup_array, [match_type])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `MATCH("b",{"a","b","c"},0) -> 2`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_match`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible date arithmetic.

- Signatures:

  - `MATCH(lookup_value, lookup_array, [match_type])`

- Examples:

  - MATCH("b",{"a","b","c"},0)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093378

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible date arithmetic.

- Signatures:

  - `MATCH(lookup_value, lookup_array, [match_type])`

- Examples:

  - MATCH("b",{"a","b","c"},0)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a
- Google Sheets: https://support.google.com/docs/answer/3093378
