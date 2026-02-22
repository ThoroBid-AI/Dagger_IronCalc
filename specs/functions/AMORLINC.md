# AMORLINC

## AMORLINC

## Purpose
Calculates linear depreciation for assets over fixed life cycles.

## Syntax
- Excel: `AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis)`
- Google Sheets: `AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis)`

## Behavior
- Uses linear method over useful life.
- Uses dates and basis to compute time fraction for period-level depreciation.

## Examples (expected outputs)
- `AMORLINC(100000, DATE(2024,1,1), 1, 10000, 1, 0.2, 0)` -> depreciation amount

## Error Cases
- Invalid life period inputs return errors.

## Notes
Not implemented in IronCalc. Planned as a dedicated depreciation implementation.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8

- Source fetch status: failed after 4 attempts

- Summary: Calculates linear depreciation for assets over fixed life cycles.

- Signatures:

  - `AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis)`

- Examples:

  - AMORLINC(100000, DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid life period inputs return errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9083932

- Source fetch status: failed after 4 attempts

- Summary: Calculates linear depreciation for assets over fixed life cycles.

- Signatures:

  - `AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis)`

- Examples:

  - AMORLINC(100000, DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid life period inputs return errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8
- Google Sheets: https://support.google.com/docs/answer/9083932
