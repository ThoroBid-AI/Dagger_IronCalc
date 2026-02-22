# HOUR

## HOUR

## Purpose
Extracts the hour component of a time/date serial value.

## Syntax
- Excel: `HOUR(serial_number)`
- Google Sheets: `HOUR(time)`

## Behavior
- Returns integer hour from 0 to 23 using spreadsheet date-time conversion rules.

## Examples (expected outputs)
- `HOUR("2026-02-19 14:30") -> 14`

## Error Cases
Invalid datetime values return an argument error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_hour`
- File: `base/src/functions/date_and_time.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_hour`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hour-function-a3afa879-86cb-4339-b1b5-2dd2d7310ac7

- Source fetch status: failed after 4 attempts

- Summary: Extracts the hour component of a time/date serial value.

- Signatures:

  - `HOUR(serial_number)`

- Examples:

  - HOUR("2026-02-19 14:30")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093045

- Source fetch status: failed after 4 attempts

- Summary: Extracts the hour component of a time/date serial value.

- Signatures:

  - `HOUR(time)`

- Examples:

  - HOUR("2026-02-19 14:30")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hour-function-a3afa879-86cb-4339-b1b5-2dd2d7310ac7
- Google Sheets: https://support.google.com/docs/answer/3093045
