# ISBLANK

## ISBLANK

## Purpose
Checks whether a reference is empty.

## Syntax
- Excel: `ISBLANK(value)`
- Google Sheets: `ISBLANK(value)`

## Behavior
- Returns TRUE if input represents an empty cell/range value.

## Examples (expected outputs)
- `ISBLANK("") -> TRUE`

## Error Cases
- Unsupported references return #REF! behavior.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_isblank`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665

- Source fetch status: failed after 4 attempts

- Summary: Checks whether a reference is empty.

- Signatures:

  - `ISBLANK(value)`

- Examples:

  - ISBLANK("")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Unsupported references return #REF! behavior.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093290

- Source fetch status: failed after 4 attempts

- Summary: Checks whether a reference is empty.

- Signatures:

  - `ISBLANK(value)`

- Examples:

  - ISBLANK("")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Unsupported references return #REF! behavior.



## Sources
- Excel: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665
- Google Sheets: https://support.google.com/docs/answer/3093290
