# NOT

## NOT

## Purpose
Logical negation.

## Syntax
- Excel: `NOT(logical)`
- Google Sheets: `NOT(logical)`

## Behavior
Returns TRUE when input is FALSE and FALSE when input is TRUE.

## Examples (expected outputs)
- `NOT(TRUE)` -> `FALSE`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_not`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NOT(logical)`

- Examples:

  - NOT(TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093305

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NOT(logical)`

- Examples:

  - NOT(TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77
- Google Sheets: https://support.google.com/docs/answer/3093305
