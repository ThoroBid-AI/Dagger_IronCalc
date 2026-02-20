# YIELDMAT
## YIELDMAT
## Purpose
Returns annual yield of bond with maturity date.
## Syntax
- Excel: `YIELDMAT(settlement,maturity,issue,first_coupon,rate,yield,redemption,frequency,[basis])`
- Google Sheets: `YIELDMAT(settlement,maturity,issue,first_coupon,rate,yield,redemption,frequency,[basis])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- YIELDMAT("2026-01-01","2027-01-01","2025-01-01",0.5,0.05,100,100,2) -> value
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_yieldmat`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/yieldmat-function-ba7d1809-0d33-4bcb-96c7-6c56ec62ef6f

- Source fetch status: failed after 4 attempts

- Summary: Returns annual yield of bond with maturity date.

- Signatures:

  - `YIELDMAT(settlement,maturity,issue,first_coupon,rate,yield,redemption,frequency,[basis])`

- Examples: `YIELDMAT(1,2,3)` -> `0`

  - YIELDMAT("2026-01-01","2027-01-01","2025-01-01",0.5,0.05,100,100,2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9000132

- Source fetch status: failed after 4 attempts

- Summary: Returns annual yield of bond with maturity date.

- Signatures:

  - `YIELDMAT(settlement,maturity,issue,first_coupon,rate,yield,redemption,frequency,[basis])`

- Examples: `YIELDMAT(1,2,3)` -> `0`

  - YIELDMAT("2026-01-01","2027-01-01","2025-01-01",0.5,0.05,100,100,2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/yieldmat-function-ba7d1809-0d33-4bcb-96c7-6c56ec62ef6f
- Google Sheets: https://support.google.com/docs/answer/9000132
