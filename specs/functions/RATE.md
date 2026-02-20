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
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce

- Summary: Returns the interest rate per period of an annuity. RATE is calculated by iteration and can have zero or more solutions. If the successive results of RATE do not converge to within 0.0000001 after 20 iterations, RATE returns the #NUM! error value. Make sure that you are consistent about the units you use for specifying guess and nper.

- Signatures:

  - `RATE(nper, pmt, pv, [fv], [type], [guess])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 4 Years of the loan -200 Monthly payment 8000 Amount of the loan Formula Description Result =RATE(A2*12, A3, A4) Monthly rate of the loan with the terms entered as arguments in A2:A4. 1% =RATE(A2*12, A3, A4)*12 Annual rate of the loan with the same terms. 9.24%

- Notes: Make sure that you are consistent about the units you use for specifying guess and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for guess and 4*12 for nper. If you make annual payments on the same loan, use 12% for guess and 4 for nper.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093257

- Summary: Calculates the interest rate of an annuity investment based on constant-amount periodic payments and the assumption of a constant interest rate. Sample Usage RATE(12,-100,400,0,0,0.1) RATE(A2,B2,C2

- Signatures:

  - `RATE(number_of_periods, payment_per_period, present_value, [future_value, end_or_beginning, rate_guess])`

- Examples:

  - RATE(12,-100,400,0,0,0.1)

  - RATE(A2,B2,C2,D2,1,0.08)

  - RATE(number_of_periods, payment_per_period, present_value, [future_value, end_or_beginning, rate_guess])

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce
- Google Sheets: https://support.google.com/docs/answer/3093257
