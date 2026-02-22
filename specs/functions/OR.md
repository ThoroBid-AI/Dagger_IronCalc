# OR

## OR

## Purpose
Logical OR across arguments.

## Syntax
- Excel: `OR(logical1, [logical2], ...)`
- Google Sheets: `OR(logical1, [logical2], ...)`

## Behavior
Returns TRUE if any argument evaluates to TRUE.

## Examples (expected outputs)
- `OR(FALSE, TRUE)` -> `TRUE`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_or`
- File: `base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0

- Source fetch status: failed after 4 attempts

- Summary: Logical OR across arguments.

- Signatures:

  - `OR(logical1, [logical2], ...)`

- Examples:

  - OR(FALSE, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093306

- Source fetch status: failed after 4 attempts

- Summary: Logical OR across arguments.

- Signatures:

  - `OR(logical1, [logical2], ...)`

- Examples:

  - OR(FALSE, TRUE)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0
- Google Sheets: https://support.google.com/docs/answer/3093306
