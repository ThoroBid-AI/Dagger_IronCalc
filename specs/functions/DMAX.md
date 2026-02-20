# DMAX

## DMAX

## Purpose
Returns the maximum value in a database field matching criteria.

## Syntax
- Excel: `DMAX(database, field, criteria)`
- Google Sheets: `DMAX(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DMAX(db, "Sales", criteria) -> 45000`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dmax`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dmax-function-f4e8209d-8958-4c3d-a1ee-6351665d41c2

- Source fetch status: failed after 4 attempts

- Summary: DMAX(db, "Sales", criteria)

- Signatures:

  - `DMAX(database, field, criteria)`

- Examples:

  - DMAX(db, "Sales", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094227

- Source fetch status: failed after 4 attempts

- Summary: DMAX(db, "Sales", criteria)

- Signatures:

  - `DMAX(database, field, criteria)`

- Examples:

  - DMAX(db, "Sales", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dmax-function-f4e8209d-8958-4c3d-a1ee-6351665d41c2
- Google Sheets: https://support.google.com/docs/answer/3094227
