# CEILING.MATH

## CEILING.MATH

## Purpose
Rounds up toward zero-aware ceiling behavior with optional mode.

## Syntax
- Excel: `CEILING.MATH(number, [significance], [mode])`
- Google Sheets: `CEILING.MATH(number, [significance], [mode])`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CEILING.MATH(-2.3, 0.5)` -> `-2`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_ceiling_math`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ceiling-math-function-80f95d2f-b499-4eee-9f16-f795a8e306c8

- Source fetch status: failed after 4 attempts

- Summary: Rounds up toward zero-aware ceiling behavior with optional mode.

- Signatures:

  - `CEILING.MATH(number, [significance], [mode])`

- Examples:

  - CEILING.MATH(-2.3, 0.5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061515

- Source fetch status: failed after 4 attempts

- Summary: Rounds up toward zero-aware ceiling behavior with optional mode.

- Signatures:

  - `CEILING.MATH(number, [significance], [mode])`

- Examples:

  - CEILING.MATH(-2.3, 0.5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ceiling-math-function-80f95d2f-b499-4eee-9f16-f795a8e306c8
- Google Sheets: https://support.google.com/docs/answer/9061515
