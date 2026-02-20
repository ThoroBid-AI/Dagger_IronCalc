# NPER

## NPER

## Purpose
Returns number of payment periods for a loan.

## Syntax
- Excel: `NPER(rate, pmt, pv, [fv], [type], [guess])`
- Google Sheets: `NPER(rate, pmt, pv, [fv], [type], [guess])`

## Behavior
Solves for number of periodic payments given rates and values.

## Examples (expected outputs)
- `NPER(0.05/12, -1000, 20000)` -> `23.45`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_nper`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NPER(rate, pmt, pv, [fv], [type], [guess])`

- Examples:

  - NPER(0.05/12, -1000, 20000)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093183

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NPER(rate, pmt, pv, [fv], [type], [guess])`

- Examples:

  - NPER(0.05/12, -1000, 20000)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815
- Google Sheets: https://support.google.com/docs/answer/3093183
