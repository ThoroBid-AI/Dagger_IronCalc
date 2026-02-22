# DMIN

## DMIN

## Purpose
Returns the minimum value in a database field matching criteria.

## Syntax
- Excel: `DMIN(database, field, criteria)`
- Google Sheets: `DMIN(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DMIN(db, "Sales", criteria) -> 12000`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dmin`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dmin-function-4ae6f1d9-1f26-40f1-a783-6dc3680192a3

- Source fetch status: failed after 4 attempts

- Summary: Returns the minimum value in a database field matching criteria.

- Signatures:

  - `DMIN(database, field, criteria)`

- Examples:

  - DMIN(db, "Sales", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094149

- Source fetch status: failed after 4 attempts

- Summary: Returns the minimum value in a database field matching criteria.

- Signatures:

  - `DMIN(database, field, criteria)`

- Examples:

  - DMIN(db, "Sales", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dmin-function-4ae6f1d9-1f26-40f1-a783-6dc3680192a3
- Google Sheets: https://support.google.com/docs/answer/3094149
