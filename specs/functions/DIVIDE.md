# DIVIDE

## DIVIDE

## Purpose
Divides one number by another.

## Syntax
- Excel: `DIVIDE(dividend, divisor)`
- Google Sheets: `DIVIDE(dividend, divisor)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DIVIDE(10,4) -> 2.5`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/mathematical.rs`
- Pseudocode:
  1. `if divisor is 0, return #DIV/0!, else numerator/denominator with exact IEEE checks`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Divides one number by another.

- Signatures:

  - `DIVIDE(dividend, divisor)`

- Examples:

  - DIVIDE(10,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093973

- Source fetch status: failed after 4 attempts

- Summary: Divides one number by another.

- Signatures:

  - `DIVIDE(dividend, divisor)`

- Examples:

  - DIVIDE(10,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093973
