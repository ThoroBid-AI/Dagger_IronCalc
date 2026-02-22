# PMT

## PMT

## Purpose
Returns periodic loan payment.

## Syntax
- Excel: `PMT(rate, nper, pv, [fv], [type])`
- Google Sheets: `PMT(rate, nper, pv, [fv], [type])`

## Behavior
Calculates payment amount using amortization formula.

## Examples (expected outputs)
- `PMT(0.05/12, 60, 10000)` -> `-188.71`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_pmt`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441

- Source fetch status: failed after 4 attempts

- Summary: Returns periodic loan payment.

- Signatures:

  - `PMT(rate, nper, pv, [fv], [type])`

- Examples:

  - PMT(0.05/12, 60, 10000)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093185

- Source fetch status: failed after 4 attempts

- Summary: Returns periodic loan payment.

- Signatures:

  - `PMT(rate, nper, pv, [fv], [type])`

- Examples:

  - PMT(0.05/12, 60, 10000)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441
- Google Sheets: https://support.google.com/docs/answer/3093185
