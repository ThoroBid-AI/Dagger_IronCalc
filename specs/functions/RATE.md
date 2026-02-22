# RATE

## RATE

## Purpose
Returns interest rate per period for an annuity.

## Syntax
- Excel: `RATE(nper, pmt, pv, [fv], [type], [guess])`
- Google Sheets: `RATE(nper, pmt, pv, [fv], [type], [guess])`

## Behavior
Solves for periodic rate using iterative method.

## Examples (expected outputs)
- `RATE(10,-1000,10000,0,0,0.1)` -> `-0.053`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rate`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce

- Source fetch status: failed after 4 attempts

- Summary: Returns interest rate per period for an annuity.

- Signatures:

  - `RATE(nper, pmt, pv, [fv], [type], [guess])`

- Examples:

  - RATE(10,-1000,10000,0,0,0.1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093257

- Source fetch status: failed after 4 attempts

- Summary: Returns interest rate per period for an annuity.

- Signatures:

  - `RATE(nper, pmt, pv, [fv], [type], [guess])`

- Examples:

  - RATE(10,-1000,10000,0,0,0.1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce
- Google Sheets: https://support.google.com/docs/answer/3093257
