# MMULT

## MMULT

## Purpose
Returns matrix product.

## Syntax
- Excel: `MMULT(array1, array2)`
- Google Sheets: `MMULT(array1, array2)`

## Behavior
- Row-column multiplication rules for matrices.

## Examples (expected outputs)
- `MMULT({{1,2},{3,4}},{{1,0},{0,1}}) -> {{1,2},{3,4}}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_mmult`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mmult-function-40593ed7-a3cd-4b6b-b9a3-e4ad3c7245eb

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `MMULT(array1, array2)`

- Examples:

  - MMULT({{1,2},{3,4}},{{1,0},{0,1}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094292

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `MMULT(array1, array2)`

- Examples:

  - MMULT({{1,2},{3,4}},{{1,0},{0,1}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mmult-function-40593ed7-a3cd-4b6b-b9a3-e4ad3c7245eb
- Google Sheets: https://support.google.com/docs/answer/3094292
