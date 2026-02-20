# CELL

## CELL

## Purpose
Returns metadata for a cell using a type keyword.

## Syntax
- Excel: `CELL(type_num, [reference])`
- Google Sheets: `CELL(info_type, reference)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CELL("type", A1)` -> `"v"`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_cell`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cell-function-51bd39a5-f338-4dbe-a33f-955d67c2b2cf

- Source fetch status: failed after 4 attempts

- Summary: Returns metadata for a cell using a type keyword.

- Signatures:

  - `CELL(type_num, [reference])`

- Examples:

  - CELL("type", A1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267071

- Source fetch status: failed after 4 attempts

- Summary: Returns metadata for a cell using a type keyword.

- Signatures:

  - `CELL(info_type, reference)`

- Examples:

  - CELL("type", A1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cell-function-51bd39a5-f338-4dbe-a33f-955d67c2b2cf
- Google Sheets: https://support.google.com/docs/answer/3267071
