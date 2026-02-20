# F.INV.RT

## F.INV.RT

## Purpose
Returns inverse right-tail value of the F distribution.

## Syntax
- Excel: `F.INV.RT(probability, d1, d2)`
- Google Sheets: `F.INV.RT(probability, d1, d2)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `F.INV.RT(0.05, 5, 10) -> 3.35`

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
  1. `invert right-tail probability for F distribution`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/f-inv-rt-function-d371aa8f-b0b1-40ef-9cc2-496f0693ac00

- Source fetch status: failed after 4 attempts

- Summary: F.INV.RT(0.05, 5, 10)

- Signatures:

  - `F.INV.RT(probability, d1, d2)`

- Examples:

  - F.INV.RT(0.05, 5, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7003960

- Source fetch status: failed after 4 attempts

- Summary: F.INV.RT(0.05, 5, 10)

- Signatures:

  - `F.INV.RT(probability, d1, d2)`

- Examples:

  - F.INV.RT(0.05, 5, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/f-inv-rt-function-d371aa8f-b0b1-40ef-9cc2-496f0693ac00
- Google Sheets: https://support.google.com/docs/answer/7003960
