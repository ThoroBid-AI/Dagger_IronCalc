# MINUTE

## MINUTE

## Purpose
Returns minute from time/date.

## Syntax
- Excel: `MINUTE(serial_number)`
- Google Sheets: `MINUTE(time)`

## Behavior
- 0-59 minute component.

## Examples (expected outputs)
- `MINUTE("12:34:56") -> 34`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_minute`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/minute-function-af728df0-05c4-4b07-9eed-a84801a60589

- Source fetch status: failed after 4 attempts

- Summary: Returns minute from time/date.

- Signatures:

  - `MINUTE(serial_number)`

- Examples:

  - MINUTE("12:34:56")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093048

- Source fetch status: failed after 4 attempts

- Summary: Returns minute from time/date.

- Signatures:

  - `MINUTE(time)`

- Examples:

  - MINUTE("12:34:56")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/minute-function-af728df0-05c4-4b07-9eed-a84801a60589
- Google Sheets: https://support.google.com/docs/answer/3093048
