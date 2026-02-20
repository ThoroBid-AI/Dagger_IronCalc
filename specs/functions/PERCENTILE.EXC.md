# PERCENTILE.EXC

## PERCENTILE.EXC

## Purpose
Returns percentile using exclusive interpolation.

## Syntax
- Excel: `PERCENTILE.EXC(array, k)`
- Google Sheets: `PERCENTILE.EXC(array, k)`

## Behavior
Computes exclusive percentile excluding min/max endpoints.

## Examples (expected outputs)
- `PERCENTILE.EXC({1,2,3,4},0.5)` -> `2.5`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentile.exc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTILE.EXC(array, k)`

- Examples:

  - PERCENTILE.EXC({1,2,3,4},0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368167

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTILE.EXC(array, k)`

- Examples:

  - PERCENTILE.EXC({1,2,3,4},0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba
- Google Sheets: https://support.google.com/docs/answer/9368167
