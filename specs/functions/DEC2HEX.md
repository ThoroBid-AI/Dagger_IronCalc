# DEC2HEX

## DEC2HEX

## Purpose
Converts decimal to hexadecimal text.

## Syntax
- Excel: `DEC2HEX(number, [places])`
- Google Sheets: `DEC2HEX(number, [places])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DEC2HEX(255,2) -> FF`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_dec2hex`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dec2hex-function-6344ee8b-b6b5-4c6a-a672-f64666704619

- Source fetch status: failed after 4 attempts

- Summary: DEC2HEX(255,2)

- Signatures:

  - `DEC2HEX(number, [places])`

- Examples:

  - DEC2HEX(255,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093137

- Source fetch status: failed after 4 attempts

- Summary: DEC2HEX(255,2)

- Signatures:

  - `DEC2HEX(number, [places])`

- Examples:

  - DEC2HEX(255,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dec2hex-function-6344ee8b-b6b5-4c6a-a672-f64666704619
- Google Sheets: https://support.google.com/docs/answer/3093137
