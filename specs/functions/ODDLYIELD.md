# ODDLYIELD

## ODDLYIELD

## Purpose
Returns odd-last-period bond yield.

## Syntax
- Excel: `ODDLYIELD(settlement, maturity, last_coupon, rate, pr, redemption, frequency, [basis])`
- Google Sheets: `ODDLYIELD(settlement, maturity, last_coupon, rate, pr, redemption, frequency, [basis])`

## Behavior
Computes yield for odd-last bond schedules.

## Examples (expected outputs)
- `ODDLYIELD("2026-01-01","2027-01-01","2026-12-31",0.05,100,100,2,0)` -> `0.04`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddlyield`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/oddlyield-function-c873d088-cf40-435f-8d41-c8232fee9238

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `ODDLYIELD(settlement, maturity, last_coupon, rate, pr, redemption, frequency, [basis])`

- Examples:

  - ODDLYIELD("2026-01-01","2027-01-01","2026-12-31",0.05,100,100,2,0)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=ODDLYIELD

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/oddlyield-function-c873d088-cf40-435f-8d41-c8232fee9238
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=ODDLYIELD
