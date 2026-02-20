# MONTH

## MONTH

## Purpose
Returns month number.

## Syntax
- Excel: `MONTH(serial_number)`
- Google Sheets: `MONTH(date)`

## Behavior
- Returns 1-12.

## Examples (expected outputs)
- `MONTH("2026-02-19") -> 2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_month`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MONTH(serial_number)`

- Examples:

  - MONTH("2026-02-19")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093052

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MONTH(date)`

- Examples:

  - MONTH("2026-02-19")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8
- Google Sheets: https://support.google.com/docs/answer/3093052
