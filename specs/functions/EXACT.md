# EXACT

## EXACT

## Purpose
Checks if two text values are identical including case.

## Syntax
- Excel: `EXACT(text1, text2)`
- Google Sheets: `EXACT(text1, text2)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EXACT("A","a") -> FALSE`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_exact`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/exact-function-d3087698-fc15-4a15-9631-12575cf29926

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `EXACT(text1, text2)`

- Examples:

  - EXACT("A","a")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094073

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `EXACT(text1, text2)`

- Examples:

  - EXACT("A","a")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/exact-function-d3087698-fc15-4a15-9631-12575cf29926
- Google Sheets: https://support.google.com/docs/answer/3094073
