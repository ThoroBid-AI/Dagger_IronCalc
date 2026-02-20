# DAYS

## DAYS

## Purpose
Returns difference in days between two dates.

## Syntax
- Excel: `DAYS(end_date, start_date)`
- Google Sheets: `DAYS(end_date, start_date)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DAYS(DATE(2026,3,1), DATE(2026,1,1)) -> 59`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_days`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/days-function-57740535-d549-4395-8728-0f07bff0b9df

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DAYS(end_date, start_date)`

- Examples:

  - DAYS(DATE(2026,3,1)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061296

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DAYS(end_date, start_date)`

- Examples:

  - DAYS(DATE(2026,3,1)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/days-function-57740535-d549-4395-8728-0f07bff0b9df
- Google Sheets: https://support.google.com/docs/answer/9061296
