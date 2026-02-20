# NEGBINOM.DIST

## NEGBINOM.DIST

## Purpose
Returns negative binomial distribution probabilities.

## Syntax
- Excel: `NEGBINOM.DIST(number, number_s, probability_s, cumulative)`
- Google Sheets: `NEGBINOM.DIST(number, number_s, probability_s, cumulative)`

## Behavior
Computes the negative binomial PMF/CDF depending on `cumulative`.

## Examples (expected outputs)
- `NEGBINOM.DIST(1, 5, 0.5, TRUE)` -> `0.03125`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/binom.rs`
- Proposed handler: `fn_negbinom.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/negbinomdist-function-f59b0a37-bae2-408d-b115-a315609ba714

- Source fetch status: failed after 4 attempts

- Summary: Returns negative binomial distribution probabilities.

- Signatures:

  - `NEGBINOM.DIST(number, number_s, probability_s, cumulative)`

- Examples:

  - NEGBINOM.DIST(1, 5, 0.5, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094031

- Source fetch status: failed after 4 attempts

- Summary: Returns negative binomial distribution probabilities.

- Signatures:

  - `NEGBINOM.DIST(number, number_s, probability_s, cumulative)`

- Examples:

  - NEGBINOM.DIST(1, 5, 0.5, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/negbinomdist-function-f59b0a37-bae2-408d-b115-a315609ba714
- Google Sheets: https://support.google.com/docs/answer/3094031
