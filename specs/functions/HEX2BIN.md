# HEX2BIN

## HEX2BIN

## Purpose
Converts a hexadecimal number to binary format.

## Syntax
- Excel: `HEX2BIN(number, [places])`
- Google Sheets: `HEX2BIN(number, [places])`

## Behavior
- Converts hex digits to binary and applies optional zero-padding.

## Examples (expected outputs)
- `HEX2BIN("1A") -> "11010"`

## Error Cases
- Invalid hex digits or overflow return errors.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_hex2bin`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hex2bin-function-a13aafaa-5737-4920-8424-643e581828c1

- Source fetch status: failed after 4 attempts

- Summary: Converts a hexadecimal number to binary format.

- Signatures:

  - `HEX2BIN(number, [places])`

- Examples:

  - HEX2BIN("1A")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid hex digits or overflow return errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093139

- Source fetch status: failed after 4 attempts

- Summary: Converts a hexadecimal number to binary format.

- Signatures:

  - `HEX2BIN(number, [places])`

- Examples:

  - HEX2BIN("1A")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid hex digits or overflow return errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hex2bin-function-a13aafaa-5737-4920-8424-643e581828c1
- Google Sheets: https://support.google.com/docs/answer/3093139
