# HEX2OCT

## HEX2OCT

## Purpose
Converts a hexadecimal number to an octal number.

## Syntax
- Excel: `HEX2OCT(number, [places])`
- Google Sheets: `HEX2OCT(number, [places])`

## Behavior
- Converts each hex digit to octal representation and applies optional zero padding.

## Examples (expected outputs)
- `HEX2OCT("1A") -> "032"`

## Error Cases
Invalid hex input or overflow returns a function/domain error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_hex2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_hex2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hex2oct-function-54d52808-5d19-4bd0-8a63-1096a5d11912

- Source fetch status: failed after 4 attempts

- Summary: Converts a hexadecimal number to an octal number.

- Signatures:

  - `HEX2OCT(number, [places])`

- Examples:

  - HEX2OCT("1A")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093142

- Source fetch status: failed after 4 attempts

- Summary: Converts a hexadecimal number to an octal number.

- Signatures:

  - `HEX2OCT(number, [places])`

- Examples:

  - HEX2OCT("1A")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hex2oct-function-54d52808-5d19-4bd0-8a63-1096a5d11912
- Google Sheets: https://support.google.com/docs/answer/3093142
