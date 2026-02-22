# F.DIST.RT

## F.DIST.RT

## Purpose
Returns the right-tail probability of the F distribution.

## Syntax
- Excel: `F.DIST.RT(x, d1, d2)`
- Google Sheets: `F.DIST.RT(x, d1, d2)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `F.DIST.RT(1.5, 5, 10) -> 0.28`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `compute 1 - CDF tail with stable numerics`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/f-dist-rt-function-d74cbb00-6017-4ac9-b7d7-6049badc0520

- Source fetch status: failed after 4 attempts

- Summary: Returns the right-tail probability of the F distribution.

- Signatures:

  - `F.DIST.RT(x, d1, d2)`

- Examples:

  - F.DIST.RT(1.5, 5, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055799

- Source fetch status: failed after 4 attempts

- Summary: Returns the right-tail probability of the F distribution.

- Signatures:

  - `F.DIST.RT(x, d1, d2)`

- Examples:

  - F.DIST.RT(1.5, 5, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/f-dist-rt-function-d74cbb00-6017-4ac9-b7d7-6049badc0520
- Google Sheets: https://support.google.com/docs/answer/6055799
