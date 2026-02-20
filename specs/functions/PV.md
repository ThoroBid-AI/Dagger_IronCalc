# PV

## PV

## Purpose
Returns present value of an investment.

## Syntax
- Excel: `PV(rate, nper, pmt, [fv], [type])`
- Google Sheets: `PV(rate, nper, pmt, [fv], [type])`

## Behavior
Discounts future payments and optional future value to current value.

## Examples (expected outputs)
- `PV(0.05/12, 60, -100, 0)` -> positive amount

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_pv`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd

- Source fetch status: failed after 4 attempts

- Summary: Returns present value of an investment.

- Signatures:

  - `PV(rate, nper, pmt, [fv], [type])`

- Examples:

  - PV(0.05/12, 60, -100, 0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093243

- Source fetch status: failed after 4 attempts

- Summary: Returns present value of an investment.

- Signatures:

  - `PV(rate, nper, pmt, [fv], [type])`

- Examples:

  - PV(0.05/12, 60, -100, 0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd
- Google Sheets: https://support.google.com/docs/answer/3093243
