# RANK

## RANK

## Purpose
Returns rank of a number in a dataset.

## Syntax
- Excel: `RANK(number, ref, [order])`
- Google Sheets: `RANK(number, ref, [order])`

## Behavior
Supports ascending or descending rank logic.

## Examples (expected outputs)
- `RANK(3,{1,2,3,4})` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rank-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723

- Source fetch status: failed after 4 attempts

- Summary: Returns rank of a number in a dataset.

- Signatures:

  - `RANK(number, ref, [order])`

- Examples:

  - RANK(3,{1,2,3,4})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094098

- Source fetch status: failed after 4 attempts

- Summary: Returns rank of a number in a dataset.

- Signatures:

  - `RANK(number, ref, [order])`

- Examples:

  - RANK(3,{1,2,3,4})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rank-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723
- Google Sheets: https://support.google.com/docs/answer/3094098
