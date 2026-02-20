# MAKEARRAY

## MAKEARRAY

## Purpose
Creates an array with lambda-generated values.

## Syntax
- Excel: `MAKEARRAY(rows, cols, lambda)`
- Google Sheets: `MAKEARRAY(rows, cols, lambda)`

## Behavior
- Calls lambda for each row/col index.

## Examples (expected outputs)
- `MAKEARRAY(2,2,LAMBDA(r,c,r+c)) -> {{2,3},{3,4}}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_makearray`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/makearray-function-b80da5ad-b338-4149-a523-5b221da09097

- Source fetch status: failed after 4 attempts

- Summary: Creates an array with lambda-generated values.

- Signatures:

  - `MAKEARRAY(rows, cols, lambda)`

- Examples:

  - MAKEARRAY(2,2,LAMBDA(r,c,r+c)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12569202

- Source fetch status: failed after 4 attempts

- Summary: Creates an array with lambda-generated values.

- Signatures:

  - `MAKEARRAY(rows, cols, lambda)`

- Examples:

  - MAKEARRAY(2,2,LAMBDA(r,c,r+c)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/makearray-function-b80da5ad-b338-4149-a523-5b221da09097
- Google Sheets: https://support.google.com/docs/answer/12569202
