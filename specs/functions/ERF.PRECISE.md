# ERF.PRECISE

## ERF.PRECISE

## Purpose
Returns the Gauss error function with higher precision behavior.

## Syntax
- Excel: `ERF.PRECISE(x)`
- Google Sheets: `ERF.PRECISE(x)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `ERF.PRECISE(1) -> 0.84270079295`

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
  1. `delegate to erf implementation with strict precision mode`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/erf-precise-function-9a349593-705c-4278-9a98-e4122831a8e0

- Source fetch status: failed after 4 attempts

- Summary: Returns the Gauss error function with higher precision behavior.

- Signatures:

  - `ERF.PRECISE(x)`

- Examples:

  - ERF.PRECISE(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116267

- Source fetch status: failed after 4 attempts

- Summary: Returns the Gauss error function with higher precision behavior.

- Signatures:

  - `ERF.PRECISE(x)`

- Examples:

  - ERF.PRECISE(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/erf-precise-function-9a349593-705c-4278-9a98-e4122831a8e0
- Google Sheets: https://support.google.com/docs/answer/9116267
