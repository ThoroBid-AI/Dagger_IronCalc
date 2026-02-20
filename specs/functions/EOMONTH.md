# EOMONTH

## EOMONTH

## Purpose
Returns the last day of the month offset from a start date.

## Syntax
- Excel: `EOMONTH(start_date, months)`
- Google Sheets: `EOMONTH(start_date, months)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EOMONTH("2/1/2026", 1) -> "3/31/2026"`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_eomonth`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628

- Source fetch status: failed after 4 attempts

- Summary: Returns the last day of the month offset from a start date.

- Signatures:

  - `EOMONTH(start_date, months)`

- Examples:

  - EOMONTH("2/1/2026", 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093044

- Source fetch status: failed after 4 attempts

- Summary: Returns the last day of the month offset from a start date.

- Signatures:

  - `EOMONTH(start_date, months)`

- Examples:

  - EOMONTH("2/1/2026", 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628
- Google Sheets: https://support.google.com/docs/answer/3093044
