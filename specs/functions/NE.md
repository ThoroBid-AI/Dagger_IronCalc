# NE

## NE

## Purpose
Tests whether two values are not equal.

## Syntax
- Excel: `NE(a, b)`
- Google Sheets: `NE(a, b)`

## Behavior
Returns TRUE when values differ, FALSE when they are equal.

## Examples (expected outputs)
- `NE(1,2)` -> `TRUE`
- `NE("A","A")` -> `FALSE`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_ne`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NE(a, b)`

- Examples:

  - NE(1,2)

  - NE("A","A")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093981

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NE(a, b)`

- Examples:

  - NE(1,2)

  - NE("A","A")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093981
