# FV

## FV

## Purpose
Calculates future value of annuity streams.

## Syntax
- Excel: `FV(rate, nper, pmt, [pv], [type])`
- Google Sheets: `FV(rate, nper, pmt, [pv], [type])`

## Behavior
- Uses constant-rate compounding and optional payment timing flag.

## Examples (expected outputs)
- `FV(0.05, 10, -100, 0, 0) -> 1257.79`

## Error Cases
- Invalid nper/rate/type inputs produce error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_fv`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3

- Source fetch status: failed after 4 attempts

- Summary: Calculates future value of annuity streams.

- Signatures:

  - `FV(rate, nper, pmt, [pv], [type])`

- Examples:

  - FV(0.05, 10, -100, 0, 0)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid nper/rate/type inputs produce error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093224

- Source fetch status: failed after 4 attempts

- Summary: Calculates future value of annuity streams.

- Signatures:

  - `FV(rate, nper, pmt, [pv], [type])`

- Examples:

  - FV(0.05, 10, -100, 0, 0)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid nper/rate/type inputs produce error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3
- Google Sheets: https://support.google.com/docs/answer/3093224
