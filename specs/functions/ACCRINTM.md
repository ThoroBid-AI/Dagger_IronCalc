# ACCRINTM

## ACCRINTM

## Purpose
Returns the accrued interest for a security that pays interest at maturity.

## Syntax
- Excel: `ACCRINTM(issue, maturity, rate, par, basis, [day_count])`
- Google Sheets: `ACCRINTM(issue, maturity, rate, par, basis, [day_count])`

## Behavior
- Calculates accrued interest between issue and maturity.
- Basis controls day-count behavior.

## Examples (expected outputs)
- `ACCRINTM(DATE(2024,1,1), DATE(2025,1,1), 0.05, 1000, 0)` -> accrual amount

## Error Cases
- Returns an error when dates are invalid or maturity is before issue.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7

- Source fetch status: failed after 4 attempts

- Summary: Returns the accrued interest for a security that pays interest at maturity.

- Signatures:

  - `ACCRINTM(issue, maturity, rate, par, basis, [day_count])`

- Examples:

  - ACCRINTM(DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns an error when dates are invalid or maturity is before issue.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093202

- Source fetch status: failed after 4 attempts

- Summary: Returns the accrued interest for a security that pays interest at maturity.

- Signatures:

  - `ACCRINTM(issue, maturity, rate, par, basis, [day_count])`

- Examples:

  - ACCRINTM(DATE(2024,1,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns an error when dates are invalid or maturity is before issue.



## Sources
- Excel: https://support.microsoft.com/en-us/office/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7
- Google Sheets: https://support.google.com/docs/answer/3093202
