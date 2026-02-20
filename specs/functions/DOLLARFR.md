# DOLLARFR

## DOLLARFR

## Purpose
Converts a decimal number to dollar-fractions format.

## Syntax
- Excel: `DOLLARFR(decimal_dollar, fraction)`
- Google Sheets: `DOLLARFR(decimal_dollar, fraction)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DOLLARFR(1.5,16) -> 1.8`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dollarfr`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495

- Source fetch status: failed after 4 attempts

- Summary: DOLLARFR(1.5,16)

- Signatures:

  - `DOLLARFR(decimal_dollar, fraction)`

- Examples:

  - DOLLARFR(1.5,16)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093217

- Source fetch status: failed after 4 attempts

- Summary: DOLLARFR(1.5,16)

- Signatures:

  - `DOLLARFR(decimal_dollar, fraction)`

- Examples:

  - DOLLARFR(1.5,16)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495
- Google Sheets: https://support.google.com/docs/answer/3093217
