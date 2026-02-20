# PERMUT

## PERMUT

## Purpose
Returns number of permutations of items.

## Syntax
- Excel: `PERMUT(number, number_chosen)`
- Google Sheets: `PERMUT(number, number_chosen)`

## Behavior
Counts ordered selections without repetition.

## Examples (expected outputs)
- `PERMUT(5,3)` -> `60`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_permut`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/permut-function-3bd1cb9a-2880-41ab-a197-f246a7a602d3

- Source fetch status: failed after 4 attempts

- Summary: Returns number of permutations of items.

- Signatures:

  - `PERMUT(number, number_chosen)`

- Examples:

  - PERMUT(5,3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094036

- Source fetch status: failed after 4 attempts

- Summary: Returns number of permutations of items.

- Signatures:

  - `PERMUT(number, number_chosen)`

- Examples:

  - PERMUT(5,3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/permut-function-3bd1cb9a-2880-41ab-a197-f246a7a602d3
- Google Sheets: https://support.google.com/docs/answer/3094036
