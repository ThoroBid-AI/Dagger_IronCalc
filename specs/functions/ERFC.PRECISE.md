# ERFC.PRECISE

## ERFC.PRECISE

## Purpose
Returns the complementary error function with higher precision behavior.

## Syntax
- Excel: `ERFC.PRECISE(x)`
- Google Sheets: `ERFC.PRECISE(x)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `ERFC.PRECISE(1) -> 0.15729920705`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/engineering/bessel.rs`
- Pseudocode:
  1. `delegate to erfc implementation with strict precision mode`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/erfc-precise-function-e90e6bab-f45e-45df-b2ac-cd2eb4d4a273

- Source fetch status: failed after 4 attempts

- Summary: Returns the complementary error function with higher precision behavior.

- Signatures:

  - `ERFC.PRECISE(x)`

- Examples:

  - ERFC.PRECISE(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093407

- Source fetch status: failed after 4 attempts

- Summary: Returns the complementary error function with higher precision behavior.

- Signatures:

  - `ERFC.PRECISE(x)`

- Examples:

  - ERFC.PRECISE(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/erfc-precise-function-e90e6bab-f45e-45df-b2ac-cd2eb4d4a273
- Google Sheets: https://support.google.com/docs/answer/3093407
