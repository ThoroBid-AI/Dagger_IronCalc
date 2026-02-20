# MDETERM

## MDETERM

## Purpose
Returns determinant of a square matrix.

## Syntax
- Excel: `MDETERM(array)`
- Google Sheets: `MDETERM(array)`

## Behavior
- Deterministic determinant calculation.

## Examples (expected outputs)
- `MDETERM({{1,2},{3,4}}) -> -2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_mdeterm`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mdeterm-function-e7bfa857-3834-422b-b871-0ffd03717020

- Source fetch status: failed after 4 attempts

- Summary: Returns determinant of a square matrix.

- Signatures:

  - `MDETERM(array)`

- Examples:

  - MDETERM({{1,2},{3,4}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094290

- Source fetch status: failed after 4 attempts

- Summary: Returns determinant of a square matrix.

- Signatures:

  - `MDETERM(array)`

- Examples:

  - MDETERM({{1,2},{3,4}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mdeterm-function-e7bfa857-3834-422b-b871-0ffd03717020
- Google Sheets: https://support.google.com/docs/answer/3094290
