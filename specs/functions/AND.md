# AND

## AND

## Purpose
Returns TRUE if all arguments evaluate to TRUE.

## Syntax
- Excel: `AND(logical1, [logical2], ...)`
- Google Sheets: `AND(logical1, [logical2], ...)`

## Behavior
- All arguments are evaluated as booleans using standard truthy rules.
- If any argument is FALSE, result is FALSE.

## Examples (expected outputs)
- `AND(TRUE, 1>0, 2=2)` -> `TRUE`
- `AND(TRUE, FALSE)` -> `FALSE`

## Error Cases
- Errors in any argument propagate unless host-specific short-circuit rules suppress them for non-boolean inputs.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_and`
- File: `base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if all arguments evaluate to TRUE.

- Signatures:

  - `AND(logical1, [logical2], ...)`

- Examples:

  - AND(TRUE, 1>0, 2=2)

  - AND(TRUE, FALSE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Errors in any argument propagate unless host-specific short-circuit rules suppress them for non-boolean inputs.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093301

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if all arguments evaluate to TRUE.

- Signatures:

  - `AND(logical1, [logical2], ...)`

- Examples:

  - AND(TRUE, 1>0, 2=2)

  - AND(TRUE, FALSE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Errors in any argument propagate unless host-specific short-circuit rules suppress them for non-boolean inputs.



## Sources
- Excel: https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9
- Google Sheets: https://support.google.com/docs/answer/3093301
