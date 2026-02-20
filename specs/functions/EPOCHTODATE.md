# EPOCHTODATE

## EPOCHTODATE

## Purpose
Converts Unix epoch seconds to a serial date value.

## Syntax
- Excel: `EPOCHTODATE(epoch, [unit])`
- Google Sheets: `EPOCHTODATE(epoch, [unit])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EPOCHTODATE(1700000000) -> 45146`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/date_and_time.rs`
- Pseudocode:
  1. `convert Unix seconds to date serial with timezone-neutral baseline`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `EPOCHTODATE(epoch, [unit])`

- Examples:

  - EPOCHTODATE(1700000000)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13193461

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `EPOCHTODATE(epoch, [unit])`

- Examples:

  - EPOCHTODATE(1700000000)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/13193461
