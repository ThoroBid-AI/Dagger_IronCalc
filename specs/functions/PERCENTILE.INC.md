# PERCENTILE.INC

## PERCENTILE.INC

## Purpose
Returns percentile with inclusive interpolation.

## Syntax
- Excel: `PERCENTILE.INC(array, k)`
- Google Sheets: `PERCENTILE.INC(array, k)`

## Behavior
Computes inclusive percentile including min/max.

## Examples (expected outputs)
- `PERCENTILE.INC({1,2,3,4},0.5)` -> `2.5`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentile.inc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTILE.INC(array, k)`

- Examples:

  - PERCENTILE.INC({1,2,3,4},0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094093

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTILE.INC(array, k)`

- Examples:

  - PERCENTILE.INC({1,2,3,4},0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed
- Google Sheets: https://support.google.com/docs/answer/3094093
