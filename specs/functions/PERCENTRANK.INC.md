# PERCENTRANK.INC

## PERCENTRANK.INC

## Purpose
Returns inclusive percentile rank.

## Syntax
- Excel: `PERCENTRANK.INC(array, x, [significance])`
- Google Sheets: `PERCENTRANK.INC(array, x, [significance])`

## Behavior
Calculates percentile with inclusive interpolation constraints.

## Examples (expected outputs)
- `PERCENTRANK.INC({1,2,3,4},3)` -> `0.6667`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentrank.inc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/percentrank-inc-function-149592c9-00c0-49ba-86c1-c1f45b80463a

- Source fetch status: failed after 4 attempts

- Summary: Returns inclusive percentile rank.

- Signatures:

  - `PERCENTRANK.INC(array, x, [significance])`

- Examples:

  - PERCENTRANK.INC({1,2,3,4},3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267360

- Source fetch status: failed after 4 attempts

- Summary: Returns inclusive percentile rank.

- Signatures:

  - `PERCENTRANK.INC(array, x, [significance])`

- Examples:

  - PERCENTRANK.INC({1,2,3,4},3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/percentrank-inc-function-149592c9-00c0-49ba-86c1-c1f45b80463a
- Google Sheets: https://support.google.com/docs/answer/3267360
