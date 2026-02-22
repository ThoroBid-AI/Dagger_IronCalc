# CONCATENATE

## CONCATENATE

## Purpose
Joins text arguments into a single text.

## Syntax
- Excel: `CONCATENATE(text1, [text2], ...)`
- Google Sheets: `CONCATENATE(text1, [text2], ...)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CONCATENATE("A","B")` -> `AB`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_concatenate`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d

- Source fetch status: failed after 4 attempts

- Summary: Joins text arguments into a single text.

- Signatures:

  - `CONCATENATE(text1, [text2], ...)`

- Examples:

  - CONCATENATE("A","B")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094123

- Source fetch status: failed after 4 attempts

- Summary: Joins text arguments into a single text.

- Signatures:

  - `CONCATENATE(text1, [text2], ...)`

- Examples:

  - CONCATENATE("A","B")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d
- Google Sheets: https://support.google.com/docs/answer/3094123
