# ISNA

## ISNA

## Purpose
Checks if value is #N/A error.

## Syntax
- Excel: `ISNA(value)`
- Google Sheets: `ISNA(value)`

## Behavior
- Returns TRUE only for #N/A variant and FALSE otherwise.

## Examples (expected outputs)
- `ISNA(#N/A) -> TRUE`

## Error Cases
- Non-errors return FALSE.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_isna`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665

- Source fetch status: failed after 4 attempts

- Summary: Checks if value is #N/A error.

- Signatures:

  - `ISNA(value)`

- Examples:

  - ISNA(#N/A)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-errors return FALSE.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093293

- Source fetch status: failed after 4 attempts

- Summary: Checks if value is #N/A error.

- Signatures:

  - `ISNA(value)`

- Examples:

  - ISNA(#N/A)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-errors return FALSE.



## Sources
- Excel: https://support.microsoft.com/en-us/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665
- Google Sheets: https://support.google.com/docs/answer/3093293
