# COLUMN

## COLUMN

## Purpose
Returns column number of a reference.

## Syntax
- Excel: `COLUMN([reference])`
- Google Sheets: `COLUMN([reference])`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `COLUMN(B5)` -> `2`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_column`
- File: `base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/column-function-44e8c754-711c-4df3-9da4-47a55042554b

- Source fetch status: failed after 4 attempts

- Summary: Returns column number of a reference.

- Signatures:

  - `COLUMN([reference])`

- Examples:

  - COLUMN(B5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093373

- Source fetch status: failed after 4 attempts

- Summary: Returns column number of a reference.

- Signatures:

  - `COLUMN([reference])`

- Examples:

  - COLUMN(B5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/column-function-44e8c754-711c-4df3-9da4-47a55042554b
- Google Sheets: https://support.google.com/docs/answer/3093373
