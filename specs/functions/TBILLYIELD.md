# TBILLYIELD
## TBILLYIELD
## Purpose
Returns treasury bill annual yield.
## Syntax
- Excel: `TBILLYIELD(settlement,maturity,price)`
- Google Sheets: `TBILLYIELD(settlement,maturity,price)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TBILLYIELD("2026-01-01","2026-07-01",98) -> 0.055
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tbillyield`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba

- Summary: The TBILLYIELD function returns the yield for a Treasury bill.

- Signatures:

  - `TBILLYIELD(settlement, maturity, pr)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 3/31/2008 Settlement date 6/1/2008 Maturity date $98.45 Price per $100 face value Formula Description Result =TBILLYIELD(A2,A3,A4) The yield for the Treasury bill using the terms in A2, A3, and A4 (0.0914, or 9.14%). 9.14%

- Notes: - Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900. - Settlement and maturity are truncated to integers. - If settlement or maturity is not a valid date, TBILLYIELD returns the #VALUE! error value. - If pr ≤ 0, TBILLYIELD returns the #NUM! error value. - If settlement ≥ maturity, or if maturity is more than one year after settlement, TBILLYIELD returns the #NUM! error value. - TBILLYIELD is calculated as follows: where: - DSM = number of days from settlement to…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093264

- Summary: Calculates the yield of a US Treasury Bill based on price. Sample Usage TBILLYIELD(DATE(2010,1,2), DATE(2010,12,31), 98.45) TBILLYIELD(A2,B2,C2) Syntax TBILLYIELD(settlement, maturity, price)

- Signatures:

  - `TBILLYIELD(settlement, maturity, price)`

- Examples:

  - TBILLYIELD(DATE(2010,1,2)

  - TBILLYIELD(A2,B2,C2)

  - TBILLYIELD(settlement, maturity, price)

- Notes: - TBILLYIELD requires the maturity date to be no more than a year after the settlement date. - settlement and maturity should be entered using DATE, TO_DATE or other date parsing functions rather than by entering text. - TBILLYIELD is equivalent to using YIELDDISC with US Treasury Bill conventions for the absent parameters.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba
- Google Sheets: https://support.google.com/docs/answer/3093264
