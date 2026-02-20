# PRICE

## PRICE

## Purpose
Returns price of a bond per $100 face value.

## Syntax
- Excel: `PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])`
- Google Sheets: `PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])`

## Behavior
Computes clean/dirty price depending on schedule assumptions.

## Examples (expected outputs)
- `PRICE("2026-01-01","2027-01-01",0.05,0.04,100,2,0)` -> approx

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_price`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])`

- Examples:

  - PRICE("2026-01-01","2027-01-01",0.05,0.04,100,2,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093188

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])`

- Examples:

  - PRICE("2026-01-01","2027-01-01",0.05,0.04,100,2,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a
- Google Sheets: https://support.google.com/docs/answer/3093188
