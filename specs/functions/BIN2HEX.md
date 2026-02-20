# BIN2HEX

## BIN2HEX

## Purpose
Converts a binary number to hexadecimal representation.

## Syntax
- Excel: `BIN2HEX(number, [places])`
- Google Sheets: `BIN2HEX(number, [places])`

## Behavior
- Converts binary text to hex string with optional minimum width.
- Padding/truncation follows host conversion rules.

## Examples (expected outputs)
- `BIN2HEX("1111")` -> `F`

## Error Cases
- Invalid binary input or unsupported precision returns error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bin2hex`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bin2hex-function-0375e507-f5e5-4077-9af8-28d84f9f41cc

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BIN2HEX(number, [places])`

- Examples:

  - BIN2HEX("1111")

- Notes: See source link when network access is restored.

- Error behavior: Invalid binary input or unsupported precision returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093133

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BIN2HEX(number, [places])`

- Examples:

  - BIN2HEX("1111")

- Notes: See source link when network access is restored.

- Error behavior: Invalid binary input or unsupported precision returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bin2hex-function-0375e507-f5e5-4077-9af8-28d84f9f41cc
- Google Sheets: https://support.google.com/docs/answer/3093133
