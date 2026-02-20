# XIRR
## XIRR
## Purpose
Computes XIRR behavior for spreadsheet formulas.
## Syntax
- Excel: `XIRR(...)`
- Google Sheets: `XIRR(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_xirr`
- File: `base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d

- Summary: This article describes the formula syntax and usage of the XIRR function which returns the internal rate of return for a schedule of cash flows that is not necessarily periodic.

- Signatures:

  - `XIRR(values, dates, [guess])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Values Dates -10,000 1-Jan-08 2,750 1-Mar-08 4,250 30-Oct-08 3,250 15-Feb-09 2,750 1-Apr-09 Formula Description (Result) Result =XIRR(A3:A7, B3:B7, 0.1) The internal rate of return (0.373362535 or 37.34%) 37.34%

- Notes: - Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900. - Numbers in dates are truncated to integers. - XIRR expects at least one positive cash flow and one negative cash flow; otherwise, XIRR returns the #NUM! error value. - If any number in dates is not a valid date, XIRR returns the #VALUE! error value. - If any number in dates precedes the starting date, XIRR returns the #NUM! error value. - If values and dates contain a different number of values, XIRR returns…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093266

- Summary: Calculates the internal rate of return of an investment based on a specified series of potentially irregularly spaced cash flows. Sample Usage XIRR(B2:B25,C2:C25) XIRR({-4000,200,250,300},{DATE(201

- Signatures:

  - `XIRR(cashflow_amounts, cashflow_dates, [rate_guess])`

- Examples:

  - XIRR(B2:B25,C2:C25)

  - XIRR({-4000,200,250,300},{DATE(2012,01,01)

  - XIRR(cashflow_amounts, cashflow_dates, [rate_guess])

- Notes: - If the days specified in cashflow_dates are at a regular interval, use IRR instead. - Each cell in cashflow_amounts should be positive if it represents income from the perspective of the owner of the investment (e.g. coupons) or negative if it represents payments (e.g. loan repayment). - XNPV will return zero if discount is set to the result of XIRR using the same cash flow amounts and schedule.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d
- Google Sheets: https://support.google.com/docs/answer/3093266
