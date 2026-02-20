# AMORDEGRC

## AMORDEGRC

## Purpose
Calculates depreciation using French accounting with coefficient and full/partial period handling.

## Syntax
- Excel: `AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, basis)`
- Google Sheets: `AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, basis)`

## Behavior
- Uses declining balance variant for French tax-style depreciation.
- Requires valid dates and positive cost basis.

## Examples (expected outputs)
- `AMORDEGRC(100000, DATE(2024,1,1), 1, 10000, 1, 0.3, 0)` -> depreciation amount

## Error Cases
- Returns an error if depreciation period values are inconsistent or negative.

## Notes
Not implemented in IronCalc. Planned with date-aware accrual logic.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/amordegrc-function-a14d0ca1-64a4-42eb-9b3d-b0dededf9e51

- Source fetch status: failed after 4 attempts

- Summary: Calculates depreciation using French accounting with coefficient and full/partial period handling.

- Signatures:

  - `AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, basis)`

- Examples:

  - AMORDEGRC(100000, DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns an error if depreciation period values are inconsistent or negative.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=AMORDEGRC

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/amordegrc-function-a14d0ca1-64a4-42eb-9b3d-b0dededf9e51
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=AMORDEGRC
