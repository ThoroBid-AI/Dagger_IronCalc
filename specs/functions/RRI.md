# RRI

## RRI

## Purpose
Returns equivalent periodic interest rate for an investment.

## Syntax
- Excel: `RRI(nper, pv, fv)`
- Google Sheets: `RRI(nper, pv, fv)`

## Behavior
Derives growth rate per period from present to future value.

## Examples (expected outputs)
- `RRI(10,100,200)` -> `0.0718`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rri`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4

- Source fetch status: failed after 4 attempts

- Summary: Returns equivalent periodic interest rate for an investment.

- Signatures:

  - `RRI(nper, pv, fv)`

- Examples:

  - RRI(10,100,200)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368238

- Source fetch status: failed after 4 attempts

- Summary: Returns equivalent periodic interest rate for an investment.

- Signatures:

  - `RRI(nper, pv, fv)`

- Examples:

  - RRI(10,100,200)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4
- Google Sheets: https://support.google.com/docs/answer/9368238
