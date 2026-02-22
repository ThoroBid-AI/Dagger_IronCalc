# YIELDDISC
## YIELDDISC
## Purpose
Returns discounted bond yield.
## Syntax
- Excel: `YIELDDISC(settlement,maturity,pr,redemption,[basis])`
- Google Sheets: `YIELDDISC(settlement,maturity,pr,redemption,[basis])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- YIELDDISC("2026-01-01","2027-01-01",98,100,0) -> value
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_yielddisc`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/yielddisc-function-a9dbdbae-7dae-46de-b995-615faffaaed7

- Source fetch status: failed after 4 attempts

- Summary: Returns discounted bond yield.

- Signatures:

  - `YIELDDISC(settlement,maturity,pr,redemption,[basis])`

- Examples:

  - YIELDDISC("2026-01-01","2027-01-01",98,100,0)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093270

- Source fetch status: failed after 4 attempts

- Summary: Returns discounted bond yield.

- Signatures:

  - `YIELDDISC(settlement,maturity,pr,redemption,[basis])`

- Examples:

  - YIELDDISC("2026-01-01","2027-01-01",98,100,0)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/yielddisc-function-a9dbdbae-7dae-46de-b995-615faffaaed7
- Google Sheets: https://support.google.com/docs/answer/3093270
