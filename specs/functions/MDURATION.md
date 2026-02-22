# MDURATION

## MDURATION

## Purpose
Returns modified bond duration.

## Syntax
- Excel: `MDURATION(settlement, maturity, coupon, yield, frequency, [basis])`
- Google Sheets: `MDURATION(settlement, maturity, coupon, yield, frequency, [basis])`

## Behavior
- Duration metric under given bond assumptions.

## Examples (expected outputs)
- `MDURATION("1/1/26","1/1/27",0.05,0.04,2) -> 0.95`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_mduration`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mduration-function-b3786a69-4f20-469a-94ad-33e5b90a763c

- Source fetch status: failed after 4 attempts

- Summary: Returns modified bond duration.

- Signatures:

  - `MDURATION(settlement, maturity, coupon, yield, frequency, [basis])`

- Examples:

  - MDURATION("1/1/26","1/1/27",0.05,0.04,2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093178

- Source fetch status: failed after 4 attempts

- Summary: Returns modified bond duration.

- Signatures:

  - `MDURATION(settlement, maturity, coupon, yield, frequency, [basis])`

- Examples:

  - MDURATION("1/1/26","1/1/27",0.05,0.04,2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mduration-function-b3786a69-4f20-469a-94ad-33e5b90a763c
- Google Sheets: https://support.google.com/docs/answer/3093178
