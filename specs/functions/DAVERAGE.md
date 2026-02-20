# DAVERAGE

## DAVERAGE

## Purpose
Returns average from records matching database criteria.

## Syntax
- Excel: `DAVERAGE(database, field, criteria)`
- Google Sheets: `DAVERAGE(database, field, criteria)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DAVERAGE(database, "Amount", criteria) -> 120`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_daverage`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/daverage-function-a6a2d5ac-4b4b-48cd-a1d8-7b37834e5aee

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DAVERAGE(database, field, criteria)`

- Examples:

  - DAVERAGE(database, "Amount", criteria)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094144

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DAVERAGE(database, field, criteria)`

- Examples:

  - DAVERAGE(database, "Amount", criteria)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/daverage-function-a6a2d5ac-4b4b-48cd-a1d8-7b37834e5aee
- Google Sheets: https://support.google.com/docs/answer/3094144
