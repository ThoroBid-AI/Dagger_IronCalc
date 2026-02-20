# RANK.AVG

## RANK.AVG

## Purpose
Returns average rank for ties.

## Syntax
- Excel: `RANK.AVG(number, ref, [order])`
- Google Sheets: `RANK.AVG(number, ref, [order])`

## Behavior
When ties occur, average rank is returned.

## Examples (expected outputs)
- `RANK.AVG(3,{1,3,3,4})` -> `2.5`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank.avg`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rank-avg-function-bd406a6f-eb38-4d73-aa8e-6d1c3c72e83a

- Source fetch status: failed after 4 attempts

- Summary: Returns average rank for ties.

- Signatures:

  - `RANK.AVG(number, ref, [order])`

- Examples:

  - RANK.AVG(3,{1,3,3,4})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267309

- Source fetch status: failed after 4 attempts

- Summary: Returns average rank for ties.

- Signatures:

  - `RANK.AVG(number, ref, [order])`

- Examples:

  - RANK.AVG(3,{1,3,3,4})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rank-avg-function-bd406a6f-eb38-4d73-aa8e-6d1c3c72e83a
- Google Sheets: https://support.google.com/docs/answer/3267309
