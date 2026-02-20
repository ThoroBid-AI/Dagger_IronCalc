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

- Summary: Syntax: RRI(nper, pv, fv)

- Signatures:

  - `RRI(nper, pv, fv)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =RRI(96,10000,11000) Returns an equivalent interest rate for the growth of an investment of $10,000 with a future value of $11,000, for 8 years (0.012, or 1.2%). 0.0009933 Top of Page

- Notes: - If argument values are not valid, RRI returns the #NUM! error value. - If arguments are not using valid data types, RRI returns the #VALUE! error value.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368238

- Summary: The RRI function returns the interest rate needed for an investment to reach a specific value within a given number of periods. Parts of a RRI function RRI(number_of_periods, present_value, future_v

- Signatures:

  - `RRI(number_of_periods, present_value, future_value)`

  - `RRI(10.5, 10, 3)`

  - `RRI(3, 2, 4)`

  - `RRI(1, 10, 0)`

- Examples: RRI Formula -0.1083343751 =RRI(10.5, 10, 3) 0.2599210499 =RRI(3, 2, 4) -1 =RRI(1, 10, 0)

- Notes: - All values must be positive. Number_of_periods and present_value must be greater than 0. - If future_value is 0, the rate returned is -1 (-100%).

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4
- Google Sheets: https://support.google.com/docs/answer/9368238
