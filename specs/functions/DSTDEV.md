# DSTDEV

## DSTDEV

## Purpose
Returns the sample standard deviation of database values matching criteria.

## Syntax
- Excel: `DSTDEV(database, field, criteria)`
- Google Sheets: `DSTDEV(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DSTDEV(db, "Qty", criteria) -> 12.34`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dstdev`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dstdev-function-026b8c73-616d-4b5e-b072-241871c4ab96

- Source fetch status: failed after 4 attempts

- Summary: DSTDEV(db, "Qty", criteria)

- Signatures:

  - `DSTDEV(database, field, criteria)`

- Examples:

  - DSTDEV(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094151

- Source fetch status: failed after 4 attempts

- Summary: DSTDEV(db, "Qty", criteria)

- Signatures:

  - `DSTDEV(database, field, criteria)`

- Examples:

  - DSTDEV(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dstdev-function-026b8c73-616d-4b5e-b072-241871c4ab96
- Google Sheets: https://support.google.com/docs/answer/3094151
