# DOLLAR

## DOLLAR

## Purpose
Converts a number to currency-format text with a fixed decimal count.

## Syntax
- Excel: `DOLLAR(number, [decimals])`
- Google Sheets: `DOLLAR(number, [decimals])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DOLLAR(1234.567, 2) -> "$1,234.57"`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  1. `format number with currency symbol, decimals, negatives and locale`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dollar-function-a6cd05d9-9740-4ad3-a469-8109d18ff611

- Source fetch status: failed after 4 attempts

- Summary: DOLLAR(1234.567, 2)

- Signatures:

  - `DOLLAR(number, [decimals])`

- Examples:

  - DOLLAR(1234.567, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094071

- Source fetch status: failed after 4 attempts

- Summary: DOLLAR(1234.567, 2)

- Signatures:

  - `DOLLAR(number, [decimals])`

- Examples:

  - DOLLAR(1234.567, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dollar-function-a6cd05d9-9740-4ad3-a469-8109d18ff611
- Google Sheets: https://support.google.com/docs/answer/3094071
