# RECEIVED

## RECEIVED

## Purpose
Returns amount received from an investment at periodic settlement.

## Syntax
- Excel: `RECEIVED(settlement, maturity, investment, discount, basis)`
- Google Sheets: `RECEIVED(settlement, maturity, investment, discount, basis)`

## Behavior
Computes redemption amount from investment and discount rate.

## Examples (expected outputs)
- `RECEIVED("2026-01-01","2027-01-01",100,0.05,0)` -> approx

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_received`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5

- Source fetch status: failed after 4 attempts

- Summary: Returns amount received from an investment at periodic settlement.

- Signatures:

  - `RECEIVED(settlement, maturity, investment, discount, basis)`

- Examples:

  - RECEIVED("2026-01-01","2027-01-01",100,0.05,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093244

- Source fetch status: failed after 4 attempts

- Summary: Returns amount received from an investment at periodic settlement.

- Signatures:

  - `RECEIVED(settlement, maturity, investment, discount, basis)`

- Examples:

  - RECEIVED("2026-01-01","2027-01-01",100,0.05,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5
- Google Sheets: https://support.google.com/docs/answer/3093244
