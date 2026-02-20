# DOLLARDE

## DOLLARDE

## Purpose
Converts a fractional dollar price to decimal representation.

## Syntax
- Excel: `DOLLARDE(fractional_dollar, fraction)`
- Google Sheets: `DOLLARDE(fractional_dollar, fraction)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DOLLARDE(1,8) -> 1.375`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_dollarde`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427

- Source fetch status: failed after 4 attempts

- Summary: DOLLARDE(1,8)

- Signatures:

  - `DOLLARDE(fractional_dollar, fraction)`

- Examples:

  - DOLLARDE(1,8)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093167

- Source fetch status: failed after 4 attempts

- Summary: DOLLARDE(1,8)

- Signatures:

  - `DOLLARDE(fractional_dollar, fraction)`

- Examples:

  - DOLLARDE(1,8)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427
- Google Sheets: https://support.google.com/docs/answer/3093167
