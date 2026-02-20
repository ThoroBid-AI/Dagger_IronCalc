# NEGBINOMDIST

## NEGBINOMDIST

## Purpose
Legacy Excel negative binomial distribution function.

## Syntax
- Excel: `NEGBINOMDIST(f, r, p)`
- Google Sheets: `NEGBINOMDIST(f, r, p)`

## Behavior
Returns the probability of a fixed number of failures before `r` successes.

## Examples (expected outputs)
- `NEGBINOMDIST(2, 5, 0.5)` -> `0.05859375`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_negbinom_dist`
- File: `base/src/functions/statistical/binom.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/negbinomdist-function-f59b0a37-bae2-408d-b115-a315609ba714

- Source fetch status: not captured in this snapshot

- Summary: Legacy Excel negative binomial distribution function.

- Signatures:

  - `NEGBINOMDIST(f, r, p)`

- Examples:

  - NEGBINOMDIST(2, 5, 0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094031

- Source fetch status: not captured in this snapshot

- Summary: Legacy Excel negative binomial distribution function.

- Signatures:

  - `NEGBINOMDIST(f, r, p)`

- Examples:

  - NEGBINOMDIST(2, 5, 0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/negbinomdist-function-f59b0a37-bae2-408d-b115-a315609ba714
- Google Sheets: https://support.google.com/docs/answer/3094031
