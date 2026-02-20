# XNPV
## XNPV
## Purpose
Computes XNPV behavior for spreadsheet formulas.
## Syntax
- Excel: `XNPV(...)`
- Google Sheets: `XNPV(...)`
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
- Handler: `fn_xnpv`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7

- Summary: The XNPV function returns the net present value for a schedule of cash flows that is not necessarily periodic.

- Signatures:

  - `XNPV(rate, values, dates)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Values Dates -$10,000 1/1/2008 $2,750 3/1/2008 $4,250 10/30/2008 $3,250 2/15/2009 $2,750 4/1/2009 Formula Description Result =XNPV(.09, A2:A6, B2:B6) The net present value for an investment with the above cost and returns. The cash flows are discounted at 9 percent. $2,086.65

- Notes: - Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900. - Numbers in dates are truncated to integers. - If any argument is nonnumeric, XNPV returns the #VALUE! error value. - If any number in dates is not a valid date, XNPV returns the #VALUE! error value. - If any number in dates precedes the starting date, XNPV returns the #NUM! error value. - If values and dates contain a different number of values, XNPV returns the #NUM! error value. - XNPV is calculated as fol…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093268

- Summary: Calculates the net present value of an investment based on a specified series of potentially irregularly spaced cash flows and a discount rate. Sample Usage XNPV(A2,B2:B25,C2:C25) XNPV(0.08,{200,25

- Signatures:

  - `XNPV(discount, cashflow_amounts, cashflow_dates)`

- Examples:

  - XNPV(A2,B2:B25,C2:C25)

  - XNPV(0.08,{200,250,300},{DATE(2012,06,23)

  - XNPV(discount, cashflow_amounts, cashflow_dates)

- Notes: - XNPV is similar to PV except that XNPV allows variable-value cash flows and cash flow intervals. - If the days specified in cashflow_dates are at a regular interval, use NPV instead. - Each cell in cashflow_amounts should be positive if it represents income from the perspective of the owner of the investment (e.g. coupons) or negative if it represents payments (e.g. loan repayment). - XIRR under the same conditions calculates the internal rate of return for which the net present value is zero.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7
- Google Sheets: https://support.google.com/docs/answer/3093268
