# TBILLPRICE
## TBILLPRICE
## Purpose
Returns treasury bill price.
## Syntax
- Excel: `TBILLPRICE(settlement,maturity,discount)`
- Google Sheets: `TBILLPRICE(settlement,maturity,discount)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TBILLPRICE("2026-01-01","2026-07-01",0.05) -> 100
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tbillprice`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2

- Summary: The TBILLPRICE function returns the price per $100 face value for a Treasury bill.

- Signatures:

  - `TBILLPRICE(settlement, maturity, discount)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 3/31/2008 Settlement date 6/1/2008 Maturity date 9.0% Percent discount rate Formula Description Result =TBILLPRICE(A2,A3,A4) The price for the Treasury bill, using the terms in A2, A3, and A4. $ 98.45

- Notes: - Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900. - Settlement and maturity are truncated to integers. - If settlement or maturity is not a valid date, TBILLPRICE returns the #VALUE! error value. - If discount ≤ 0, TBILLPRICE returns the #NUM! error value. - If settlement > maturity, or if maturity is more than one year after settlement, TBILLPRICE returns the #NUM! error value. - TBILLPRICE is calculated as follows: where: - DSM = number of days from settlem…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093251

- Summary: Calculates the price of a US Treasury Bill based on discount rate. Sample Usage TBILLPRICE(DATE(2010,1,2), DATE(2010,12,31), .0125) TBILLPRICE(A2,B2,C2) Syntax TBILLPRICE(settlement, maturity, di

- Signatures:

  - `TBILLPRICE(settlement, maturity, discount)`

- Examples:

  - TBILLPRICE(DATE(2010,1,2)

  - TBILLPRICE(A2,B2,C2)

  - TBILLPRICE(settlement, maturity, discount)

- Notes: - settlement and maturity should be entered using DATE, TO_DATE or other date parsing functions rather than by entering text. - TBILLPRICE is equivalent to using PRICEDISC with US Treasury Bill conventions for the absent parameters. - maturity must be one year or less from the settlement date. - discount is a percentage and must be entered as a positive number from zero to one.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2
- Google Sheets: https://support.google.com/docs/answer/3093251
