# PERCENTRANK

## PERCENTRANK

## Purpose
Returns rank percentile of a value in a data set.

## Syntax
- Excel: `PERCENTRANK(array, x, [significance])`
- Google Sheets: `PERCENTRANK(array, x, [significance])`

## Behavior
Finds percentile position of `x` with optional significance.

## Examples (expected outputs)
- `PERCENTRANK({1,2,3,4},3)` -> `0.6666667`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentrank`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/percentrank-function-f1b5836c-9619-4847-9fc9-080ec9024442

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTRANK(array, x, [significance])`

- Examples:

  - PERCENTRANK({1,2,3,4},3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094095

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTRANK(array, x, [significance])`

- Examples:

  - PERCENTRANK({1,2,3,4},3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/percentrank-function-f1b5836c-9619-4847-9fc9-080ec9024442
- Google Sheets: https://support.google.com/docs/answer/3094095
