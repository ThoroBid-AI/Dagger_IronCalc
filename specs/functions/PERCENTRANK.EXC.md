# PERCENTRANK.EXC

## PERCENTRANK.EXC

## Purpose
Returns exclusive percentile rank.

## Syntax
- Excel: `PERCENTRANK.EXC(array, x, [significance])`
- Google Sheets: `PERCENTRANK.EXC(array, x, [significance])`

## Behavior
Calculates percentile with exclusive interpolation constraints.

## Examples (expected outputs)
- `PERCENTRANK.EXC({1,2,3,4},3)` -> `0.6667`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentrank.exc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTRANK.EXC(array, x, [significance])`

- Examples:

  - PERCENTRANK.EXC({1,2,3,4},3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267357

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERCENTRANK.EXC(array, x, [significance])`

- Examples:

  - PERCENTRANK.EXC({1,2,3,4},3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314
- Google Sheets: https://support.google.com/docs/answer/3267357
