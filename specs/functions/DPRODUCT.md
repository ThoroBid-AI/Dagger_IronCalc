# DPRODUCT

## DPRODUCT

## Purpose
Multiplies selected database field values after applying criteria.

## Syntax
- Excel: `DPRODUCT(database, field, criteria)`
- Google Sheets: `DPRODUCT(database, field, criteria)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DPRODUCT(db, "Qty", criteria) -> 240`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dproduct`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dproduct-function-4f96b13e-d49c-47a7-b769-22f6d017cb31

- Source fetch status: failed after 4 attempts

- Summary: Multiplies selected database field values after applying criteria.

- Signatures:

  - `DPRODUCT(database, field, criteria)`

- Examples:

  - DPRODUCT(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094230

- Source fetch status: failed after 4 attempts

- Summary: Multiplies selected database field values after applying criteria.

- Signatures:

  - `DPRODUCT(database, field, criteria)`

- Examples:

  - DPRODUCT(db, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dproduct-function-4f96b13e-d49c-47a7-b769-22f6d017cb31
- Google Sheets: https://support.google.com/docs/answer/3094230
