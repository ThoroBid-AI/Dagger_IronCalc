# RANDARRAY

## RANDARRAY

## Purpose
Returns array of random numbers.

## Syntax
- Excel: `RANDARRAY([rows], [columns], [min], [max], [integer])`
- Google Sheets: `RANDARRAY([rows], [columns], [min], [max], [integer])`

## Behavior
Generates deterministic pseudo-random grid when context is seeded.

## Examples (expected outputs)
- `RANDARRAY(2,2,1,10,TRUE)` -> `[[1,2],[3,4]]`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_randarray`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `RANDARRAY([rows], [columns], [min], [max], [integer])`

- Examples:

  - RANDARRAY(2,2,1,10,TRUE)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9211904

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and ordered input handling required.

- Signatures:

  - `RANDARRAY([rows], [columns], [min], [max], [integer])`

- Examples:

  - RANDARRAY(2,2,1,10,TRUE)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33
- Google Sheets: https://support.google.com/docs/answer/9211904
