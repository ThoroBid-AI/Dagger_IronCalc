# MULTINOMIAL

## MULTINOMIAL

## Purpose
Returns multinomial coefficient.

## Syntax
- Excel: `MULTINOMIAL(number1, [number2], ...)`
- Google Sheets: `MULTINOMIAL(number1, [number2], ...)`

## Behavior
- Factorial ratio coefficient.

## Examples (expected outputs)
- `MULTINOMIAL(1,2,3) -> 60`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_multinomial`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/multinomial-function-6fa6373c-6533-41a2-a45e-a56db1db1bf6

- Source fetch status: failed after 4 attempts

- Summary: Returns multinomial coefficient.

- Signatures:

  - `MULTINOMIAL(number1, [number2], ...)`

- Examples:

  - MULTINOMIAL(1,2,3)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093429

- Source fetch status: failed after 4 attempts

- Summary: Returns multinomial coefficient.

- Signatures:

  - `MULTINOMIAL(number1, [number2], ...)`

- Examples:

  - MULTINOMIAL(1,2,3)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/multinomial-function-6fa6373c-6533-41a2-a45e-a56db1db1bf6
- Google Sheets: https://support.google.com/docs/answer/3093429
