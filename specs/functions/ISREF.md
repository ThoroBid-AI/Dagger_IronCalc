# ISREF

## ISREF

## Purpose
Returns TRUE if value is a reference.

## Syntax
- Excel: `ISREF(value)`
- Google Sheets: `ISREF(value)`

## Behavior
- Validates reference type and range validity.

## Examples (expected outputs)
- `ISREF(A1) -> TRUE`

## Error Cases
- Non-reference inputs return FALSE unless invalid reference error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_isref`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is a reference.

- Signatures:

  - `ISREF(value)`

- Examples:

  - ISREF(A1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-reference inputs return FALSE unless invalid reference error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093354

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is a reference.

- Signatures:

  - `ISREF(value)`

- Examples:

  - ISREF(A1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-reference inputs return FALSE unless invalid reference error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665
- Google Sheets: https://support.google.com/docs/answer/3093354
