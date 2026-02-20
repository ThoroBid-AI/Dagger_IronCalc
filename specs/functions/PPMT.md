# PPMT

## PPMT

## Purpose
Returns payment for a loan interest and principal with constant payments.

## Syntax
- Excel: `PPMT(rate, per, nper, pv, [fv], [type])`
- Google Sheets: `PPMT(rate, per, nper, pv, [fv], [type])`

## Behavior
Computes principal portion of payment at period `per`.

## Examples (expected outputs)
- `PPMT(0.08/12,1,36,10000,0,0)` -> negative number

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_ppmt`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b

- Source fetch status: failed after 4 attempts

- Summary: Returns payment for a loan interest and principal with constant payments.

- Signatures:

  - `PPMT(rate, per, nper, pv, [fv], [type])`

- Examples:

  - PPMT(0.08/12,1,36,10000,0,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093187

- Source fetch status: failed after 4 attempts

- Summary: Returns payment for a loan interest and principal with constant payments.

- Signatures:

  - `PPMT(rate, per, nper, pv, [fv], [type])`

- Examples:

  - PPMT(0.08/12,1,36,10000,0,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b
- Google Sheets: https://support.google.com/docs/answer/3093187
