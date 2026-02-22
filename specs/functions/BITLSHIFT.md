# BITLSHIFT

## BITLSHIFT

## Purpose
Shifts bits left by a specified amount.

## Syntax
- Excel: `BITLSHIFT(number, shift_amount)`
- Google Sheets: `BITLSHIFT(number, shift)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `BITLSHIFT(5,2)` -> `20`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bitlshift`
- File: `base/src/functions/engineering/bit_operations.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bitlshift-function-c55bb27e-cacd-4c7c-b258-d80861a03c9c

- Source fetch status: failed after 4 attempts

- Summary: Shifts bits left by a specified amount.

- Signatures:

  - `BITLSHIFT(number, shift_amount)`

- Examples:

  - BITLSHIFT(5,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061443

- Source fetch status: failed after 4 attempts

- Summary: Shifts bits left by a specified amount.

- Signatures:

  - `BITLSHIFT(number, shift)`

- Examples:

  - BITLSHIFT(5,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bitlshift-function-c55bb27e-cacd-4c7c-b258-d80861a03c9c
- Google Sheets: https://support.google.com/docs/answer/9061443
