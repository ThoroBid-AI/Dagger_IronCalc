# EVEN

## EVEN

## Purpose
Rounds a number up to the nearest even integer.

## Syntax
- Excel: `EVEN(number)`
- Google Sheets: `EVEN(number)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EVEN(2.3) -> 4`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_even`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/even-function-197b5f06-c795-4c1e-8696-3c3b8a646cf9

- Source fetch status: failed after 4 attempts

- Summary: Rounds a number up to the nearest even integer.

- Signatures:

  - `EVEN(number)`

- Examples:

  - EVEN(2.3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093409

- Source fetch status: failed after 4 attempts

- Summary: Rounds a number up to the nearest even integer.

- Signatures:

  - `EVEN(number)`

- Examples:

  - EVEN(2.3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/even-function-197b5f06-c795-4c1e-8696-3c3b8a646cf9
- Google Sheets: https://support.google.com/docs/answer/3093409
