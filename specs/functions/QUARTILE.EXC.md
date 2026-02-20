# QUARTILE.EXC

## QUARTILE.EXC

## Purpose
Returns exclusive quartile value.

## Syntax
- Excel: `QUARTILE.EXC(array, quartile)`
- Google Sheets: `QUARTILE.EXC(array, quartile)`

## Behavior
Uses percentile method excluding dataset endpoints.

## Examples (expected outputs)
- `QUARTILE.EXC({1,2,3,4,5,6,7,8},2)` -> `3`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/percentile.rs`
- Proposed handler: `fn_quartile.exc`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad

- Source fetch status: failed after 4 attempts

- Summary: Returns exclusive quartile value.

- Signatures:

  - `QUARTILE.EXC(array, quartile)`

- Examples:

  - QUARTILE.EXC({1,2,3,4,5,6,7,8},2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368240

- Source fetch status: failed after 4 attempts

- Summary: Returns exclusive quartile value.

- Signatures:

  - `QUARTILE.EXC(array, quartile)`

- Examples:

  - QUARTILE.EXC({1,2,3,4,5,6,7,8},2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad
- Google Sheets: https://support.google.com/docs/answer/9368240
