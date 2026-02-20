# F.DIST

## F.DIST

## Purpose
Returns values of the F distribution CDF and inverse behavior via variant args.

## Syntax
- Excel: `F.DIST(x, d1, d2, cumulative)`
- Google Sheets: `F.DIST(x, d1, d2, cumulative)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `F.DIST(1.5, 5, 10, TRUE) -> 0.72`

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
  1. `compute F CDF using beta regularized path`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/fdist-function-ecf76fba-b3f1-4e7d-a57e-6a5b7460b786

- Source fetch status: failed after 4 attempts

- Summary: Returns values of the F distribution CDF and inverse behavior via variant args.

- Signatures:

  - `F.DIST(x, d1, d2, cumulative)`

- Examples:

  - F.DIST(1.5, 5, 10, TRUE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055799

- Source fetch status: failed after 4 attempts

- Summary: Returns values of the F distribution CDF and inverse behavior via variant args.

- Signatures:

  - `F.DIST(x, d1, d2, cumulative)`

- Examples:

  - F.DIST(1.5, 5, 10, TRUE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/fdist-function-ecf76fba-b3f1-4e7d-a57e-6a5b7460b786
- Google Sheets: https://support.google.com/docs/answer/6055799
