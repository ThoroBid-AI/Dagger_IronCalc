# COMBIN

## COMBIN

## Purpose
Returns number of combinations (n choose k).

## Syntax
- Excel: `COMBIN(number, number_chosen)`
- Google Sheets: `COMBIN(number, number_chosen)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `COMBIN(5,2)` -> `10`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_combin`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/combin-function-12a3f276-0a21-423a-8de6-06990aaf638a

- Source fetch status: failed after 4 attempts

- Summary: Returns number of combinations (n choose k).

- Signatures:

  - `COMBIN(number, number_chosen)`

- Examples:

  - COMBIN(5,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093400

- Source fetch status: failed after 4 attempts

- Summary: Returns number of combinations (n choose k).

- Signatures:

  - `COMBIN(number, number_chosen)`

- Examples:

  - COMBIN(5,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/combin-function-12a3f276-0a21-423a-8de6-06990aaf638a
- Google Sheets: https://support.google.com/docs/answer/3093400
