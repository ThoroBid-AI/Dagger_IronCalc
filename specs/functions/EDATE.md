# EDATE

## EDATE

## Purpose
Returns a date shifted by a number of months.

## Syntax
- Excel: `EDATE(start_date, months)`
- Google Sheets: `EDATE(start_date, months)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EDATE("1/31/2026", 2) -> "3/31/2026"`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_edate`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5

- Source fetch status: failed after 4 attempts

- Summary: Returns a date shifted by a number of months.

- Signatures:

  - `EDATE(start_date, months)`

- Examples:

  - EDATE("1/31/2026", 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092974

- Source fetch status: failed after 4 attempts

- Summary: Returns a date shifted by a number of months.

- Signatures:

  - `EDATE(start_date, months)`

- Examples:

  - EDATE("1/31/2026", 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5
- Google Sheets: https://support.google.com/docs/answer/3092974
