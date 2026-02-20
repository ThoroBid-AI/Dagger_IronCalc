# DISC

## DISC

## Purpose
Returns the discount for a security at settlement and maturity.

## Syntax
- Excel: `DISC(settlement, maturity, pr, redemption, [basis])`
- Google Sheets: `DISC(settlement, maturity, pr, redemption, [basis])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DISC("01/01/2026", "01/01/2027", 95, 100, 0) -> 0.0526`

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
  1. `derive discount = (redemption - pr) / (maturity - settlement) * basisAdjusted`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53

- Source fetch status: failed after 4 attempts

- Summary: DISC("01/01/2026", "01/01/2027", 95, 100, 0)

- Signatures:

  - `DISC(settlement, maturity, pr, redemption, [basis])`

- Examples:

  - DISC("01/01/2026", "01/01/2027", 95, 100, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093216

- Source fetch status: failed after 4 attempts

- Summary: DISC("01/01/2026", "01/01/2027", 95, 100, 0)

- Signatures:

  - `DISC(settlement, maturity, pr, redemption, [basis])`

- Examples:

  - DISC("01/01/2026", "01/01/2027", 95, 100, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53
- Google Sheets: https://support.google.com/docs/answer/3093216
