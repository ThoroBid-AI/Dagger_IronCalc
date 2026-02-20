# ACCRINT

## ACCRINT

## Purpose
Returns the accrued interest for a security that pays periodic interest.

## Syntax
- Excel: `ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis, [calc_method])`
- Google Sheets: `ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis, [method])`

## Behavior
- Issue date, first coupon date, settlement, rate, par, frequency, and basis are required.
- Frequency is one of 1, 2, 4 (annual, semiannual, quarterly).
- The optional method controls whether actual/actual interest is rounded.
- Errors are returned if the settlement date is before issue or if parameters are invalid.

## Examples (expected outputs)
- `ACCRINT(DATE(2024,1,1), DATE(2024,6,30), DATE(2024,3,15), 0.08, 1000, 2, 0)` -> `42.5`

## Error Cases
- Returns an error when required date order or frequency is invalid.

## Notes
Not implemented in IronCalc. Planned as a financial function for bond-like schedules.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/accrint-function-fe45d089-6722-4fb3-9379-e1f911d8dc74

- Source fetch status: failed after 4 attempts

- Summary: Returns the accrued interest for a security that pays periodic interest.

- Signatures:

  - `ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis, [calc_method])`

- Examples:

  - ACCRINT(DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns an error when required date order or frequency is invalid.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093200

- Source fetch status: failed after 4 attempts

- Summary: Returns the accrued interest for a security that pays periodic interest.

- Signatures:

  - `ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis, [method])`

- Examples:

  - ACCRINT(DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns an error when required date order or frequency is invalid.



## Sources
- Excel: https://support.microsoft.com/en-us/office/accrint-function-fe45d089-6722-4fb3-9379-e1f911d8dc74
- Google Sheets: https://support.google.com/docs/answer/3093200
