# DVAR

## DVAR

## Purpose
Returns the sample variance of database values matching criteria.

## Syntax
- Excel: `DVAR(database, field, criteria)`
- Google Sheets: `DVAR(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DVAR(db, "Score", criteria) -> 48.2`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dvar`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dvar-function-d6747ca9-99c7-48bb-996e-9d7af00f3ed1

- Source fetch status: failed after 4 attempts

- Summary: Returns the sample variance of database values matching criteria.

- Signatures:

  - `DVAR(database, field, criteria)`

- Examples:

  - DVAR(db, "Score", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094236

- Source fetch status: failed after 4 attempts

- Summary: Returns the sample variance of database values matching criteria.

- Signatures:

  - `DVAR(database, field, criteria)`

- Examples:

  - DVAR(db, "Score", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dvar-function-d6747ca9-99c7-48bb-996e-9d7af00f3ed1
- Google Sheets: https://support.google.com/docs/answer/3094236
