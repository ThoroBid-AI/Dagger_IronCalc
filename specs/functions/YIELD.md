# YIELD
## YIELD
## Purpose
Returns bond yield based on price and terms.
## Syntax
- Excel: `YIELD(settlement,maturity,rate,pr,redemption,frequency,[basis])`
- Google Sheets: `YIELD(settlement,maturity,rate,pr,redemption,frequency,[basis])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- YIELD("2026-01-01","2027-01-01",0.05,95,100,2) -> value
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_yield`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe

- Source fetch status: failed after 4 attempts

- Summary: Returns bond yield based on price and terms.

- Signatures:

  - `YIELD(settlement,maturity,rate,pr,redemption,frequency,[basis])`

- Examples:

  - YIELD("2026-01-01","2027-01-01",0.05,95,100,2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093255

- Source fetch status: failed after 4 attempts

- Summary: Returns bond yield based on price and terms.

- Signatures:

  - `YIELD(settlement,maturity,rate,pr,redemption,frequency,[basis])`

- Examples:

  - YIELD("2026-01-01","2027-01-01",0.05,95,100,2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe
- Google Sheets: https://support.google.com/docs/answer/3093255
