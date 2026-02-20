# NORM.S.DIST

## NORM.S.DIST

## Purpose
Standard normal distribution function.

## Syntax
- Excel: `NORM.S.DIST(z, cumulative)`
- Google Sheets: `NORM.S.DIST(z, cumulative)`

## Behavior
Computes distribution values for mean 0 and standard deviation 1.

## Examples (expected outputs)
- `NORM.S.DIST(0, TRUE)` -> `0.5`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.s.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/normsdist-function-463369ea-0345-445d-802a-4ff0d6ce7cac

- Source fetch status: failed after 4 attempts

- Summary: Standard normal distribution function.

- Signatures:

  - `NORM.S.DIST(z, cumulative)`

- Examples:

  - NORM.S.DIST(0, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094089

- Source fetch status: failed after 4 attempts

- Summary: Standard normal distribution function.

- Signatures:

  - `NORM.S.DIST(z, cumulative)`

- Examples:

  - NORM.S.DIST(0, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/normsdist-function-463369ea-0345-445d-802a-4ff0d6ce7cac
- Google Sheets: https://support.google.com/docs/answer/3094089
