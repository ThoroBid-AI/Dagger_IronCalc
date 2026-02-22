# MUNIT

## MUNIT

## Purpose
Returns unit (identity) matrix.

## Syntax
- Excel: `MUNIT(dimension)`
- Google Sheets: `MUNIT(dimension)`

## Behavior
- Produces identity matrix.

## Examples (expected outputs)
- `MUNIT(2) -> {{1,0},{0,1}}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_munit`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/munit-function-c9fe916a-dc26-4105-997d-ba22799853a3

- Source fetch status: failed after 4 attempts

- Summary: Returns unit (identity) matrix.

- Signatures:

  - `MUNIT(dimension)`

- Examples:

  - MUNIT(2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368156

- Source fetch status: failed after 4 attempts

- Summary: Returns unit (identity) matrix.

- Signatures:

  - `MUNIT(dimension)`

- Examples:

  - MUNIT(2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/munit-function-c9fe916a-dc26-4105-997d-ba22799853a3
- Google Sheets: https://support.google.com/docs/answer/9368156
