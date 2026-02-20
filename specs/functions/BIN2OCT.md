# BIN2OCT

## BIN2OCT

## Purpose
Converts a binary value to an octal text representation.

## Syntax
- Excel: `BIN2OCT(number, [places])`
- Google Sheets: `BIN2OCT(number, [places])`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `BIN2OCT(10,4)` -> `12`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bin2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bin2oct-function-0a4e01ba-ac8d-4158-9b29-16c25c4c23fd

- Source fetch status: failed after 4 attempts

- Summary: Converts a binary value to an octal text representation.

- Signatures:

  - `BIN2OCT(number, [places])`

- Examples:

  - BIN2OCT(10,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092993

- Source fetch status: failed after 4 attempts

- Summary: Converts a binary value to an octal text representation.

- Signatures:

  - `BIN2OCT(number, [places])`

- Examples:

  - BIN2OCT(10,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bin2oct-function-0a4e01ba-ac8d-4158-9b29-16c25c4c23fd
- Google Sheets: https://support.google.com/docs/answer/3092993
