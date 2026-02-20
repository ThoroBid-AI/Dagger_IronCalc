# BIN2DEC

## BIN2DEC

## Purpose
Converts a binary text representation to decimal.

## Syntax
- Excel: `BIN2DEC(number)`
- Google Sheets: `BIN2DEC(number)`

## Behavior
- Accepts up to 10-bit signed two’s-complement binary text in many host modes.
- Returns decimal integer string conversion.

## Examples (expected outputs)
- `BIN2DEC("1010")` -> `10`

## Error Cases
- Non-binary characters or out-of-range bit-width return an error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bin2dec`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bin2dec-function-63905b57-b3a0-453d-99f4-647bb519cd6c

- Source fetch status: failed after 4 attempts

- Summary: Converts a binary text representation to decimal.

- Signatures:

  - `BIN2DEC(number)`

- Examples:

  - BIN2DEC("1010")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-binary characters or out-of-range bit-width return an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092991

- Source fetch status: failed after 4 attempts

- Summary: Converts a binary text representation to decimal.

- Signatures:

  - `BIN2DEC(number)`

- Examples:

  - BIN2DEC("1010")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-binary characters or out-of-range bit-width return an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bin2dec-function-63905b57-b3a0-453d-99f4-647bb519cd6c
- Google Sheets: https://support.google.com/docs/answer/3092991
