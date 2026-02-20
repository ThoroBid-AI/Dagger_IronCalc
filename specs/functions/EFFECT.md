# EFFECT

## EFFECT

## Purpose
Converts nominal interest rate to effective annual rate.

## Syntax
- Excel: `EFFECT(nominal_rate, npery)`
- Google Sheets: `EFFECT(nominal_rate, npery)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EFFECT(0.05, 12) -> 0.0512`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_effect`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `EFFECT(nominal_rate, npery)`

- Examples:

  - EFFECT(0.05, 12)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093223

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `EFFECT(nominal_rate, npery)`

- Examples:

  - EFFECT(0.05, 12)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4
- Google Sheets: https://support.google.com/docs/answer/3093223
