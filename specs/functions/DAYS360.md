# DAYS360

## DAYS360

## Purpose
Returns day count using 360-day year convention.

## Syntax
- Excel: `DAYS360(start_date, end_date, [method])`
- Google Sheets: `DAYS360(start_date, end_date, [method])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DAYS360(DATE(2026,1,1), DATE(2026,12,31), FALSE) -> 360`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_days360`
- File: `base/src/functions/date_and_time.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/days360-function-b9a509fd-49ef-407e-94df-0cbda5718c2a

- Source fetch status: failed after 4 attempts

- Summary: Returns day count using 360-day year convention.

- Signatures:

  - `DAYS360(start_date, end_date, [method])`

- Examples:

  - DAYS360(DATE(2026,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093042

- Source fetch status: failed after 4 attempts

- Summary: Returns day count using 360-day year convention.

- Signatures:

  - `DAYS360(start_date, end_date, [method])`

- Examples:

  - DAYS360(DATE(2026,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/days360-function-b9a509fd-49ef-407e-94df-0cbda5718c2a
- Google Sheets: https://support.google.com/docs/answer/3093042
