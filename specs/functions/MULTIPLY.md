# MULTIPLY

## MULTIPLY

## Purpose
Returns product of two numbers.

## Syntax
- Excel: `MULTIPLY(number1, number2)`
- Google Sheets: `MULTIPLY(number1, number2)`

## Behavior
- Arithmetic multiplication.

## Examples (expected outputs)
- `MULTIPLY(6,7) -> 42`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_multiply`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns product of two numbers.

- Signatures:

  - `MULTIPLY(number1, number2)`

- Examples:

  - MULTIPLY(6,7)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093978

- Source fetch status: failed after 4 attempts

- Summary: Returns product of two numbers.

- Signatures:

  - `MULTIPLY(number1, number2)`

- Examples:

  - MULTIPLY(6,7)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093978
