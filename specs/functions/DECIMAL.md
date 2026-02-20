# DECIMAL

## DECIMAL

## Purpose
Converts base-N text into decimal number.

## Syntax
- Excel: `DECIMAL(text, radix)`
- Google Sheets: `DECIMAL(number, radix)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DECIMAL("FF", 16) -> 255`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_decimal`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/decimal-function-ee554665-6176-46ef-82de-0a283658da2e

- Source fetch status: failed after 4 attempts

- Summary: DECIMAL("FF", 16)

- Signatures:

  - `DECIMAL(text, radix)`

- Examples:

  - DECIMAL("FF", 16)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116090

- Source fetch status: failed after 4 attempts

- Summary: DECIMAL("FF", 16)

- Signatures:

  - `DECIMAL(number, radix)`

- Examples:

  - DECIMAL("FF", 16)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/decimal-function-ee554665-6176-46ef-82de-0a283658da2e
- Google Sheets: https://support.google.com/docs/answer/9116090
