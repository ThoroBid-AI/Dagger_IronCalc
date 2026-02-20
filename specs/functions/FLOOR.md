# FLOOR

## FLOOR

## Purpose
Rounds a number down to nearest multiple of significance.

## Syntax
- Excel: `FLOOR(number, [significance], [mode])`
- Google Sheets: `FLOOR(number, [significance], [mode])`

## Behavior
- Uses significance and optional mode for negative numbers and host-compatible behavior.

## Examples (expected outputs)
- `FLOOR(12.7, 1) -> 12`
- `FLOOR(-12.7, 1) -> -13`

## Error Cases
- Invalid significance or unsupported mode returns error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_floor`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/floor-function-14bb497c-24f2-4e04-b327-b0b4de5a8886

- Source fetch status: failed after 4 attempts

- Summary: Rounds a number down to nearest multiple of significance.

- Signatures:

  - `FLOOR(number, [significance], [mode])`

- Examples:

  - FLOOR(12.7, 1)

  - FLOOR(-12.7, 1)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid significance or unsupported mode returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093487

- Source fetch status: failed after 4 attempts

- Summary: Rounds a number down to nearest multiple of significance.

- Signatures:

  - `FLOOR(number, [significance], [mode])`

- Examples:

  - FLOOR(12.7, 1)

  - FLOOR(-12.7, 1)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid significance or unsupported mode returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/floor-function-14bb497c-24f2-4e04-b327-b0b4de5a8886
- Google Sheets: https://support.google.com/docs/answer/3093487
