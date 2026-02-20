# DURATION

## DURATION

## Purpose
Returns a bond duration-style time-weighted metric.

## Syntax
- Excel: `DURATION(settlement, maturity, coupon, yld, frequency, [basis])`
- Google Sheets: `DURATION(settlement, maturity, coupon, yld, frequency, [basis])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DURATION("01/01/2026", "01/01/2027", 0.05, 0.045, 1, 0) -> 7`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  1. `compute duration formula using settlement/maturity/coupon/yield/frequency/basis`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DURATION(settlement, maturity, coupon, yld, frequency, [basis])`

- Examples:

  - DURATION("01/01/2026", "01/01/2027", 0.05, 0.045, 1, 0)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093169

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DURATION(settlement, maturity, coupon, yld, frequency, [basis])`

- Examples:

  - DURATION("01/01/2026", "01/01/2027", 0.05, 0.045, 1, 0)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038
- Google Sheets: https://support.google.com/docs/answer/3093169
