# CEILING.PRECISE

## CEILING.PRECISE

## Purpose
Rounds a number up to nearest multiple of significance, always positive direction.

## Syntax
- Excel: `CEILING.PRECISE(number, [significance])`
- Google Sheets: `CEILING.PRECISE(number, [significance])`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CEILING.PRECISE(-2.3)` -> `-2`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_ceiling_precise`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ceiling-precise-function-f366a774-527a-4c92-ba49-af0a196e66cb

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CEILING.PRECISE(number, [significance])`

- Examples:

  - CEILING.PRECISE(-2.3)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061294

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CEILING.PRECISE(number, [significance])`

- Examples:

  - CEILING.PRECISE(-2.3)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ceiling-precise-function-f366a774-527a-4c92-ba49-af0a196e66cb
- Google Sheets: https://support.google.com/docs/answer/9061294
