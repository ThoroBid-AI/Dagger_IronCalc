# POISSON.DIST

## POISSON.DIST

## Purpose
Returns Poisson distribution values.

## Syntax
- Excel: `POISSON.DIST(x, mean, cumulative)`
- Google Sheets: `POISSON.DIST(x, mean, cumulative)`

## Behavior
Computes Poisson probability mass or cumulative probability.

## Examples (expected outputs)
- `POISSON.DIST(2,3,TRUE)` -> `0.42319008`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_poisson.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/poisson-dist-function-8fe148ff-39a2-46cb-abf3-7772695d9636

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `POISSON.DIST(x, mean, cumulative)`

- Examples:

  - POISSON.DIST(2,3,TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094097

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `POISSON.DIST(x, mean, cumulative)`

- Examples:

  - POISSON.DIST(2,3,TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/poisson-dist-function-8fe148ff-39a2-46cb-abf3-7772695d9636
- Google Sheets: https://support.google.com/docs/answer/3094097
