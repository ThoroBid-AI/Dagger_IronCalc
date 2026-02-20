# ISERROR

## ISERROR

## Purpose
Returns TRUE if value is any error.

## Syntax
- Excel: `ISERROR(value)`
- Google Sheets: `ISERROR(value)`

## Behavior
- Detects generic error class values.

## Examples (expected outputs)
- `ISERROR(#N/A) -> TRUE`

## Error Cases
- Non-error values return FALSE.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_iserror`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is any error.

- Signatures:

  - `ISERROR(value)`

- Examples:

  - ISERROR(#N/A)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-error values return FALSE.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093349

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is any error.

- Signatures:

  - `ISERROR(value)`

- Examples:

  - ISERROR(#N/A)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-error values return FALSE.



## Sources
- Excel: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665
- Google Sheets: https://support.google.com/docs/answer/3093349
