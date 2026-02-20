# DEC2BIN

## DEC2BIN

## Purpose
Converts decimal to binary text.

## Syntax
- Excel: `DEC2BIN(number, [places])`
- Google Sheets: `DEC2BIN(number, [places])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DEC2BIN(255, 8) -> 11111111`

## Error Cases
- Number out of range returns error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_dec2bin`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dec2bin-function-0f63dd0e-5d1a-42d8-b511-5bf5c6d43838

- Source fetch status: failed after 4 attempts

- Summary: DEC2BIN(255, 8)

- Signatures:

  - `DEC2BIN(number, [places])`

- Examples:

  - DEC2BIN(255, 8)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Number out of range returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092997

- Source fetch status: failed after 4 attempts

- Summary: DEC2BIN(255, 8)

- Signatures:

  - `DEC2BIN(number, [places])`

- Examples:

  - DEC2BIN(255, 8)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Number out of range returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dec2bin-function-0f63dd0e-5d1a-42d8-b511-5bf5c6d43838
- Google Sheets: https://support.google.com/docs/answer/3092997
