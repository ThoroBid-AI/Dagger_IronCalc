# MINVERSE

## MINVERSE

## Purpose
Returns inverse of matrix.

## Syntax
- Excel: `MINVERSE(array)`
- Google Sheets: `MINVERSE(array)`

## Behavior
- Returns matrix inverse for square matrices.

## Examples (expected outputs)
- `MINVERSE({{1,2},{3,4}}) -> {{-2,1},{1.5,-0.5}}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_minverse`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/minverse-function-11f55086-adde-4c9f-8eb9-59da2d72efc6

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of matrix.

- Signatures:

  - `MINVERSE(array)`

- Examples:

  - MINVERSE({{1,2},{3,4}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094253

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of matrix.

- Signatures:

  - `MINVERSE(array)`

- Examples:

  - MINVERSE({{1,2},{3,4}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/minverse-function-11f55086-adde-4c9f-8eb9-59da2d72efc6
- Google Sheets: https://support.google.com/docs/answer/3094253
