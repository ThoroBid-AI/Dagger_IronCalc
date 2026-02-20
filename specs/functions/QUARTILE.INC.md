# QUARTILE.INC

## QUARTILE.INC

## Purpose
Returns inclusive quartile value.

## Syntax
- Excel: `QUARTILE.INC(array, quartile)`
- Google Sheets: `QUARTILE.INC(array, quartile)`

## Behavior
Uses percentile method including dataset endpoints.

## Examples (expected outputs)
- `QUARTILE.INC({1,2,3,4,5,6,7,8},2)` -> `4`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/percentile.rs`
- Proposed handler: `fn_quartile.inc`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `QUARTILE.INC(array, quartile)`

- Examples:

  - QUARTILE.INC({1,2,3,4,5,6,7,8},2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094041

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `QUARTILE.INC(array, quartile)`

- Examples:

  - QUARTILE.INC({1,2,3,4,5,6,7,8},2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d
- Google Sheets: https://support.google.com/docs/answer/3094041
