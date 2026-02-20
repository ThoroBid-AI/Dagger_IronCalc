# DSUM

## DSUM

## Purpose
Sums database field values matching criteria.

## Syntax
- Excel: `DSUM(database, field, criteria)`
- Google Sheets: `DSUM(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DSUM(db, "Qty", criteria) -> 720`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dsum`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dsum-function-53181285-0c4b-4f5a-aaa3-529a322be41b

- Source fetch status: failed after 4 attempts

- Summary: Sums database field values matching criteria.

- Signatures:

  - `DSUM(database, field, criteria)`

- Examples:

  - DSUM(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094281

- Source fetch status: failed after 4 attempts

- Summary: Sums database field values matching criteria.

- Signatures:

  - `DSUM(database, field, criteria)`

- Examples:

  - DSUM(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dsum-function-53181285-0c4b-4f5a-aaa3-529a322be41b
- Google Sheets: https://support.google.com/docs/answer/3094281
