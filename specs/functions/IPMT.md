# IPMT

## IPMT

## Purpose
Returns interest payment for a specific period.

## Syntax
- Excel: `IPMT(rate, per, nper, pv, [fv], [type])`
- Google Sheets: `IPMT(rate, per, nper, pv, [fv], [type])`

## Behavior
- Computes interest component of a payment with period index and schedule flags.

## Examples (expected outputs)
- `IPMT(0.08/12, 1, 12, -1000) -> -6.22`

## Error Cases
- Invalid period or sign combinations return error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_ipmt`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f

- Source fetch status: failed after 4 attempts

- Summary: Returns interest payment for a specific period.

- Signatures:

  - `IPMT(rate, per, nper, pv, [fv], [type])`

- Examples:

  - IPMT(0.08/12, 1, 12, -1000)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid period or sign combinations return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093175

- Source fetch status: failed after 4 attempts

- Summary: Returns interest payment for a specific period.

- Signatures:

  - `IPMT(rate, per, nper, pv, [fv], [type])`

- Examples:

  - IPMT(0.08/12, 1, 12, -1000)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid period or sign combinations return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f
- Google Sheets: https://support.google.com/docs/answer/3093175
