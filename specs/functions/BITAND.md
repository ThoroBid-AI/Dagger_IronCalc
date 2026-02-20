# BITAND

## BITAND

## Purpose
Returns bitwise AND of two integers.

## Syntax
- Excel: `BITAND(number1, number2)`
- Google Sheets: `BITAND(number1, number2)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `BITAND(6,3)` -> `2`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bitand`
- File: `base/src/functions/engineering/bit_operations.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bitand-function-8a2be3d7-91c3-4b48-9517-64548008563a

- Source fetch status: failed after 4 attempts

- Summary: Returns bitwise AND of two integers.

- Signatures:

  - `BITAND(number1, number2)`

- Examples:

  - BITAND(6,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061440

- Source fetch status: failed after 4 attempts

- Summary: Returns bitwise AND of two integers.

- Signatures:

  - `BITAND(number1, number2)`

- Examples:

  - BITAND(6,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bitand-function-8a2be3d7-91c3-4b48-9517-64548008563a
- Google Sheets: https://support.google.com/docs/answer/9061440
