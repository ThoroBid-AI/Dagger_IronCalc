# HLOOKUP

## HLOOKUP

## Purpose
Looks up a value in the first row of a table and returns matching value from a specified row.

## Syntax
- Excel: `HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])`
- Google Sheets: `HLOOKUP(lookup_value, table_array, row_index, [is_sorted])`

## Behavior
- Performs row-oriented lookup with optional approximate matching.

## Examples (expected outputs)
- `HLOOKUP(2, {1,2,3;4,5,6}, 2, FALSE) -> 5`

## Error Cases
Invalid row index or unresolved key returns #N/A-like error behavior.

## Notes
- Implemented in IronCalc.
- Handler: `fn_hlookup`
- File: `base/src/functions/lookup_and_reference.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_hlookup`
- File: `base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f

- Source fetch status: failed after 4 attempts

- Summary: Looks up a value in the first row of a table and returns matching value from a specified row.

- Signatures:

  - `HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])`

- Examples:

  - HLOOKUP(2, {1,2,3;4,5,6}, 2, FALSE)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093375

- Source fetch status: failed after 4 attempts

- Summary: Looks up a value in the first row of a table and returns matching value from a specified row.

- Signatures:

  - `HLOOKUP(lookup_value, table_array, row_index, [is_sorted])`

- Examples:

  - HLOOKUP(2, {1,2,3;4,5,6}, 2, FALSE)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f
- Google Sheets: https://support.google.com/docs/answer/3093375
