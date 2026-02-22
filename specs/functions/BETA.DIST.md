# BETA.DIST

## BETA.DIST

## Purpose
Returns the cumulative beta distribution or density function depending on parameters.

## Syntax
- Excel: `BETA.DIST(x, alpha, beta, cumulative, A, B, [C], [D])`
- Google Sheets: `BETA.DIST(x, alpha, beta, cumulative, lower, upper)`

## Behavior
- Supports cumulative flag and optional bounds.
- For cumulative=TRUE returns CDF, else PDF.

## Examples (expected outputs)
- `BETA.DIST(0.5, 2, 3, TRUE, 0, 1)` -> value between 0 and 1

## Error Cases
- Invalid alpha/beta or bounds outside domain return error.

## Notes
Not implemented in IronCalc. Planned through dedicated statistical distribution module.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/beta-dist-function-11188c9c-780a-42c7-ba43-9ecb5a878d31

- Source fetch status: failed after 4 attempts

- Summary: Returns the cumulative beta distribution or density function depending on parameters.

- Signatures:

  - `BETA.DIST(x, alpha, beta, cumulative, A, B, [C], [D])`

- Examples:

  - BETA.DIST(0.5, 2, 3, TRUE, 0, 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid alpha/beta or bounds outside domain return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9084099

- Source fetch status: failed after 4 attempts

- Summary: Returns the cumulative beta distribution or density function depending on parameters.

- Signatures:

  - `BETA.DIST(x, alpha, beta, cumulative, lower, upper)`

- Examples:

  - BETA.DIST(0.5, 2, 3, TRUE, 0, 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid alpha/beta or bounds outside domain return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/beta-dist-function-11188c9c-780a-42c7-ba43-9ecb5a878d31
- Google Sheets: https://support.google.com/docs/answer/9084099
