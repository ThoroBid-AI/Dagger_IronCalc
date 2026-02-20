# F.INV

## F.INV

## Purpose
Returns inverse of F distribution CDF (given cumulative probability).

## Syntax
- Excel: `F.INV(probability, d1, d2)`
- Google Sheets: `F.INV(probability, d1, d2)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `F.INV(0.05, 5, 10) -> 0.42`

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
  1. `invert F CDF with monotonic search and precision limits`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/finv-function-4d46c97c-c368-4852-bc15-41e8e31140b1

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of F distribution CDF (given cumulative probability).

- Signatures:

  - `F.INV(probability, d1, d2)`

- Examples:

  - F.INV(0.05, 5, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7003960

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of F distribution CDF (given cumulative probability).

- Signatures:

  - `F.INV(probability, d1, d2)`

- Examples:

  - F.INV(0.05, 5, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/finv-function-4d46c97c-c368-4852-bc15-41e8e31140b1
- Google Sheets: https://support.google.com/docs/answer/7003960
