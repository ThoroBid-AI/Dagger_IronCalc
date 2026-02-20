# CONCAT

## CONCAT

## Purpose
Joins text strings without separators.

## Syntax
- Excel: `CONCAT(text1, [text2], ...)`
- Google Sheets: `CONCAT(text1, [text2], ...)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CONCAT("A","B")` -> `AB`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_concat`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CONCAT(text1, [text2], ...)`

- Examples:

  - CONCAT("A","B")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093592

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CONCAT(text1, [text2], ...)`

- Examples:

  - CONCAT("A","B")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2
- Google Sheets: https://support.google.com/docs/answer/3093592
