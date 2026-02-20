# ODDFPRICE

## ODDFPRICE

## Purpose
Returns odd-first-period bond price.

## Syntax
- Excel: `ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])`
- Google Sheets: `ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])`

## Behavior
Uses odd first coupon period conventions to calculate full-price bond value.

## Examples (expected outputs)
- `ODDFPRICE("2026-01-01","2027-01-01","2025-01-01","2025-10-31",0.05,0.04,100,2,0)` -> `100+`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddfprice`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/oddfprice-function-d7d664a8-34df-4233-8d2b-922bcf6a69e1

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])`

- Examples:

  - ODDFPRICE("2026-01-01","2027-01-01","2025-01-01","2025-10-31",0.05,0.04,100,2,0)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=ODDFPRICE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/oddfprice-function-d7d664a8-34df-4233-8d2b-922bcf6a69e1
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=ODDFPRICE
