# BITOR

## BITOR

## Purpose
Returns bitwise OR of two integers.

## Syntax
- Excel: `BITOR(number1, number2)`
- Google Sheets: `BITOR(number1, number2)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `BITOR(6,3)` -> `7`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bitor`
- File: `base/src/functions/engineering/bit_operations.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bitor-function-f6ead5c8-5b98-4c9e-9053-8ad5234919b2

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BITOR(number1, number2)`

- Examples:

  - BITOR(6,3)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9083934

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BITOR(number1, number2)`

- Examples:

  - BITOR(6,3)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bitor-function-f6ead5c8-5b98-4c9e-9053-8ad5234919b2
- Google Sheets: https://support.google.com/docs/answer/9083934
