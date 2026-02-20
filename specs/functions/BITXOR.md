# BITXOR

## BITXOR

## Purpose
Returns bitwise exclusive OR of two integers.

## Syntax
- Excel: `BITXOR(number1, number2)`
- Google Sheets: `BITXOR(number1, number2)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `BITXOR(6,3)` -> `5`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bitxor`
- File: `base/src/functions/engineering/bit_operations.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bitxor-function-c81306a1-03f9-4e89-85ac-b86c3cba10e4

- Source fetch status: failed after 4 attempts

- Summary: Returns bitwise exclusive OR of two integers.

- Signatures:

  - `BITXOR(number1, number2)`

- Examples:

  - BITXOR(6,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9083935

- Source fetch status: failed after 4 attempts

- Summary: Returns bitwise exclusive OR of two integers.

- Signatures:

  - `BITXOR(number1, number2)`

- Examples:

  - BITXOR(6,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bitxor-function-c81306a1-03f9-4e89-85ac-b86c3cba10e4
- Google Sheets: https://support.google.com/docs/answer/9083935
