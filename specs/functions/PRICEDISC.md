# PRICEDISC

## PRICEDISC

## Purpose
Returns discounted security price.

## Syntax
- Excel: `PRICEDISC(settlement, maturity, discount, redemption, [basis])`
- Google Sheets: `PRICEDISC(settlement, maturity, discount, redemption, [basis])`

## Behavior
Prices bond with discount rate and redemption value.

## Examples (expected outputs)
- `PRICEDISC("2026-01-01","2027-01-01",0.06,100)` -> approx

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_pricedisc`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `PRICEDISC(settlement, maturity, discount, redemption, [basis])`

- Examples:

  - PRICEDISC("2026-01-01","2027-01-01",0.06,100)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093240

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `PRICEDISC(settlement, maturity, discount, redemption, [basis])`

- Examples:

  - PRICEDISC("2026-01-01","2027-01-01",0.06,100)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3
- Google Sheets: https://support.google.com/docs/answer/3093240
