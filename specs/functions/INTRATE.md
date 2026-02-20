# INTRATE

## INTRATE

## Purpose
Returns the interest rate for an investment over a period.

## Syntax
- Excel: `INTRATE(settlement, maturity, investment, redemption, [basis])`
- Google Sheets: `INTRATE(settlement, maturity, investment, redemption, [basis])`

## Behavior
- Uses discount method and compounding basis to derive annualized rate.

## Examples (expected outputs)
- `INTRATE("01/01/2026","01/01/2027",900,1000,0) -> 0.111111`

## Error Cases
- Settlement after maturity or invalid basis returns error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_intrate`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/intrate-function-5cb34dde-a221-4cb6-b3eb-0b9e55e1316f

- Source fetch status: failed after 4 attempts

- Summary: INTRATE("01/01/2026","01/01/2027",900,1000,0)

- Signatures:

  - `INTRATE(settlement, maturity, investment, redemption, [basis])`

- Examples:

  - INTRATE("01/01/2026","01/01/2027",900,1000,0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Settlement after maturity or invalid basis returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093174

- Source fetch status: failed after 4 attempts

- Summary: INTRATE("01/01/2026","01/01/2027",900,1000,0)

- Signatures:

  - `INTRATE(settlement, maturity, investment, redemption, [basis])`

- Examples:

  - INTRATE("01/01/2026","01/01/2027",900,1000,0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Settlement after maturity or invalid basis returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/intrate-function-5cb34dde-a221-4cb6-b3eb-0b9e55e1316f
- Google Sheets: https://support.google.com/docs/answer/3093174
