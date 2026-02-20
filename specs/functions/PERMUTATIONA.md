# PERMUTATIONA

## PERMUTATIONA

## Purpose
Returns number of permutations with repetition.

## Syntax
- Excel: `PERMUTATIONA(number, number_chosen)`
- Google Sheets: `PERMUTATIONA(number, number_chosen)`

## Behavior
Counts ordered selections with repetition.

## Examples (expected outputs)
- `PERMUTATIONA(5,3)` -> `125`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_permutationa`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/permutationa-function-6c7d7fdc-d657-44e6-aa19-2857b25cae4e

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERMUTATIONA(number, number_chosen)`

- Examples:

  - PERMUTATIONA(5,3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368324

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PERMUTATIONA(number, number_chosen)`

- Examples:

  - PERMUTATIONA(5,3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/permutationa-function-6c7d7fdc-d657-44e6-aa19-2857b25cae4e
- Google Sheets: https://support.google.com/docs/answer/9368324
