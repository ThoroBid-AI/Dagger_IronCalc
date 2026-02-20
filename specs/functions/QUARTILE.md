# QUARTILE

## QUARTILE

## Purpose
Returns quartile of a data set.

## Syntax
- Excel: `QUARTILE(array, quart)`
- Google Sheets: `QUARTILE(array, quart)`

## Behavior
Returns one of 1st, 2nd, 3rd, or 4th quartiles.

## Examples (expected outputs)
- `QUARTILE({1,2,3,4},1)` -> `1.75`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/percentile.rs`
- Proposed handler: `fn_quartile`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/quartile-function-93cf8f62-60cd-4fdb-8a92-8451041e1a2a

- Source fetch status: failed after 4 attempts

- Summary: Returns quartile of a data set.

- Signatures:

  - `QUARTILE(array, quart)`

- Examples:

  - QUARTILE({1,2,3,4},1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094041

- Source fetch status: failed after 4 attempts

- Summary: Returns quartile of a data set.

- Signatures:

  - `QUARTILE(array, quart)`

- Examples:

  - QUARTILE({1,2,3,4},1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/quartile-function-93cf8f62-60cd-4fdb-8a92-8451041e1a2a
- Google Sheets: https://support.google.com/docs/answer/3094041
