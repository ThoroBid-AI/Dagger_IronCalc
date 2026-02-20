# COMPLEX

## COMPLEX

## Purpose
Constructs a complex number from real and imaginary parts.

## Syntax
- Excel: `COMPLEX(real_num, i_num, [suffix])`
- Google Sheets: `COMPLEX(real_num, i_num, [suffix])`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `COMPLEX(3,4)` -> `3+4i`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_complex`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/complex-function-f0b8f3a9-51cc-4d6d-86fb-3a9362fa4128

- Source fetch status: failed after 4 attempts

- Summary: Constructs a complex number from real and imaginary parts.

- Signatures:

  - `COMPLEX(real_num, i_num, [suffix])`

- Examples:

  - COMPLEX(3,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7407888

- Source fetch status: failed after 4 attempts

- Summary: Constructs a complex number from real and imaginary parts.

- Signatures:

  - `COMPLEX(real_num, i_num, [suffix])`

- Examples:

  - COMPLEX(3,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/complex-function-f0b8f3a9-51cc-4d6d-86fb-3a9362fa4128
- Google Sheets: https://support.google.com/docs/answer/7407888
