# DSTDEVP

## DSTDEVP

## Purpose
Returns the population standard deviation of database values matching criteria.

## Syntax
- Excel: `DSTDEVP(database, field, criteria)`
- Google Sheets: `DSTDEVP(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DSTDEVP(db, "Qty", criteria) -> 10.01`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dstdevp`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dstdevp-function-04b78995-da03-4813-bbd9-d74fd0f5d94b

- Source fetch status: failed after 4 attempts

- Summary: DSTDEVP(db, "Qty", criteria)

- Signatures:

  - `DSTDEVP(database, field, criteria)`

- Examples:

  - DSTDEVP(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094280

- Source fetch status: failed after 4 attempts

- Summary: DSTDEVP(db, "Qty", criteria)

- Signatures:

  - `DSTDEVP(database, field, criteria)`

- Examples:

  - DSTDEVP(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dstdevp-function-04b78995-da03-4813-bbd9-d74fd0f5d94b
- Google Sheets: https://support.google.com/docs/answer/3094280
