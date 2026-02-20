# ODDLPRICE

## ODDLPRICE

## Purpose
Returns odd-last-period bond price.

## Syntax
- Excel: `ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])`
- Google Sheets: `ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])`

## Behavior
Prices bonds where last period is not standard length.

## Examples (expected outputs)
- `ODDLPRICE("2026-01-01","2027-01-01","2026-12-31",0.05,0.04,100,2,0)` -> `100+`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddlprice`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/oddlprice-function-fb657749-d200-4902-afaf-ed5445027fc4

- Source fetch status: failed after 4 attempts

- Summary: Returns odd-last-period bond price.

- Signatures:

  - `ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])`

- Examples:

  - ODDLPRICE("2026-01-01","2027-01-01","2026-12-31",0.05,0.04,100,2,0)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=ODDLPRICE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/oddlprice-function-fb657749-d200-4902-afaf-ed5445027fc4
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=ODDLPRICE
