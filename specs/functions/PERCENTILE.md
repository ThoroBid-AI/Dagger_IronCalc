# PERCENTILE

## PERCENTILE

## Purpose
Returns the k-th percentile of data.

## Syntax
- Excel: `PERCENTILE(array, k)`
- Google Sheets: `PERCENTILE(array, k)`

## Behavior
Computes percentile by Excel interpolation variant.

## Examples (expected outputs)
- `PERCENTILE({1,2,3,4},0.5)` -> `2.5`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentile`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/percentile-function-91b43a53-543c-4708-93de-d626debdddca

- Source fetch status: failed after 4 attempts

- Summary: Returns the k-th percentile of data.

- Signatures:

  - `PERCENTILE(array, k)`

- Examples:

  - PERCENTILE({1,2,3,4},0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094093

- Source fetch status: failed after 4 attempts

- Summary: Returns the k-th percentile of data.

- Signatures:

  - `PERCENTILE(array, k)`

- Examples:

  - PERCENTILE({1,2,3,4},0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/percentile-function-91b43a53-543c-4708-93de-d626debdddca
- Google Sheets: https://support.google.com/docs/answer/3094093
