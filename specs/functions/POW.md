# POW

## POW

## Purpose
Raises base to a power.

## Syntax
- Excel: `POW(number, power)`
- Google Sheets: `POW(number, power)`

## Behavior
Equivalent to exponentiation operator.

## Examples (expected outputs)
- `POW(2,3)` -> `8`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_pow`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `POW(number, power)`

- Examples:

  - POW(2,3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093603

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `POW(number, power)`

- Examples:

  - POW(2,3)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093603
