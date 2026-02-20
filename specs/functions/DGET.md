# DGET

## DGET

## Purpose
Returns one matching value from a database-like table filtered by criteria.

## Syntax
- Excel: `DGET(database, field, criteria)`
- Google Sheets: `DGET(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DGET({"A1:A4"},"field","criteria") -> 100`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dget`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dget-function-455568bf-4eef-45f7-90f0-ec250d00892e

- Source fetch status: failed after 4 attempts

- Summary: Returns one matching value from a database-like table filtered by criteria.

- Signatures:

  - `DGET(database, field, criteria)`

- Examples:

  - DGET({"A1:A4"},"field","criteria")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094148

- Source fetch status: failed after 4 attempts

- Summary: Returns one matching value from a database-like table filtered by criteria.

- Signatures:

  - `DGET(database, field, criteria)`

- Examples:

  - DGET({"A1:A4"},"field","criteria")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dget-function-455568bf-4eef-45f7-90f0-ec250d00892e
- Google Sheets: https://support.google.com/docs/answer/3094148
