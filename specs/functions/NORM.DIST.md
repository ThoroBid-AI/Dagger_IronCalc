# NORM.DIST

## NORM.DIST

## Purpose
Returns normal distribution values.

## Syntax
- Excel: `NORM.DIST(x, mean, standard_dev, cumulative)`
- Google Sheets: `NORM.DIST(x, mean, standard_dev, cumulative)`

## Behavior
Returns density or cumulative probability for normal distribution.

## Examples (expected outputs)
- `NORM.DIST(0, 0, 1, TRUE)` -> `0.5`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/normdist-function-126db625-c53e-4591-9a22-c9ff422d6d58

- Source fetch status: failed after 4 attempts

- Summary: Returns normal distribution values.

- Signatures:

  - `NORM.DIST(x, mean, standard_dev, cumulative)`

- Examples:

  - NORM.DIST(0, 0, 1, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094021

- Source fetch status: failed after 4 attempts

- Summary: Returns normal distribution values.

- Signatures:

  - `NORM.DIST(x, mean, standard_dev, cumulative)`

- Examples:

  - NORM.DIST(0, 0, 1, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/normdist-function-126db625-c53e-4591-9a22-c9ff422d6d58
- Google Sheets: https://support.google.com/docs/answer/3094021
