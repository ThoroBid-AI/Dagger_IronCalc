# PRICEMAT

## PRICEMAT

## Purpose
Returns security price with maturity interest.

## Syntax
- Excel: `PRICEMAT(settlement, maturity, issue, rate, yld, [basis])`
- Google Sheets: `PRICEMAT(settlement, maturity, issue, rate, yld, [basis])`

## Behavior
Calculates price using issue date and annual rate context.

## Examples (expected outputs)
- `PRICEMAT("2026-01-01","2027-01-01","2025-01-01",0.05,0.04)` -> approx

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_pricemat`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pricemat-function-52c3b4da-bc7e-476a-989f-a95f675cae77

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `PRICEMAT(settlement, maturity, issue, rate, yld, [basis])`

- Examples:

  - PRICEMAT("2026-01-01","2027-01-01","2025-01-01",0.05,0.04)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093191

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `PRICEMAT(settlement, maturity, issue, rate, yld, [basis])`

- Examples:

  - PRICEMAT("2026-01-01","2027-01-01","2025-01-01",0.05,0.04)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pricemat-function-52c3b4da-bc7e-476a-989f-a95f675cae77
- Google Sheets: https://support.google.com/docs/answer/3093191
