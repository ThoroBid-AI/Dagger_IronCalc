# EXPON.DIST

## EXPON.DIST

## Purpose
Calculates exponential distribution cumulative or density values.

## Syntax
- Excel: `EXPON.DIST(x, lambda, cumulative)`
- Google Sheets: `EXPON.DIST(x, lambda, cumulative)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EXPON.DIST(1, 0.5, TRUE) -> 0.39347`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/exponential.rs`
- Pseudocode:
  1. `compute pdf/cdf with branch for cumulative flag`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/expondist-function-68ab45fd-cd6d-4887-9770-9357eb8ee06a

- Source fetch status: failed after 4 attempts

- Summary: Calculates exponential distribution cumulative or density values.

- Signatures:

  - `EXPON.DIST(x, lambda, cumulative)`

- Examples:

  - EXPON.DIST(1, 0.5, TRUE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093995

- Source fetch status: failed after 4 attempts

- Summary: Calculates exponential distribution cumulative or density values.

- Signatures:

  - `EXPON.DIST(x, lambda, cumulative)`

- Examples:

  - EXPON.DIST(1, 0.5, TRUE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/expondist-function-68ab45fd-cd6d-4887-9770-9357eb8ee06a
- Google Sheets: https://support.google.com/docs/answer/3093995
