# ISERR

## ISERR

## Purpose
Returns TRUE if value is any error except #N/A.

## Syntax
- Excel: `ISERR(value)`
- Google Sheets: `ISERR(value)`

## Behavior
- Checks error type class and excludes NA-class errors.

## Examples (expected outputs)
- `ISERR(#DIV/0!) -> TRUE`

## Error Cases
- Non-error values return FALSE.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_iserr`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is any error except #N/A.

- Signatures:

  - `ISERR(value)`

- Examples:

  - ISERR(#DIV/0!)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-error values return FALSE.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093348

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is any error except #N/A.

- Signatures:

  - `ISERR(value)`

- Examples:

  - ISERR(#DIV/0!)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-error values return FALSE.



## Sources
- Excel: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665
- Google Sheets: https://support.google.com/docs/answer/3093348
