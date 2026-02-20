# TBILLEQ
## TBILLEQ
## Purpose
Returns treasury bill discount-equivalent yield.
## Syntax
- Excel: `TBILLEQ(settlement, maturity, discount)`
- Google Sheets: `TBILLEQ(settlement, maturity, discount)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TBILLEQ("2026-01-01","2026-07-01",0.05) -> 0.06
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tbilleq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c

- Summary: Returns treasury bill discount-equivalent yield.

- Signatures:

  - `TBILLEQ(settlement, maturity, discount)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 3/31/2008 Settlement date 6/1/2008 Maturity date 9.14% Percent discount rate Formula Description Result =TBILLEQ(A2,A3,A4) The bond equivalent yield, for the Treasury bill using the terms in A2, A3, and A4 (0.09415, or 9.42%). 9.42%

- Notes: - Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900. - Settlement and maturity are truncated to integers. - If settlement or maturity is not a valid date, TBILLEQ returns the #VALUE! error value. - If discount ≤ 0, TBILLEQ returns the #NUM! error value. - If settlement > maturity, or if maturity is more than one year after settlement, TBILLEQ returns the #NUM! error value. - TBILLEQ is calculated as TBILLEQ = (365 x rate)/(360-(rate x DSM)), where DSM is the num…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093249

- Summary: Calculates the equivalent annualized rate of return of a US Treasury Bill based on discount rate. Sample Usage TBILLEQ(DATE(2010,1,2), DATE(2010,12,31), .09) TBILLEQ(A2,B2,C2) Syntax TBILLEQ(sett

- Signatures:

  - `TBILLEQ(settlement, maturity, discount)`

- Examples:

  - TBILLEQ(DATE(2010,1,2)

  - TBILLEQ(A2,B2,C2)

  - TBILLEQ(settlement, maturity, discount)

- Notes: - settlement and maturity should be entered using DATE, TO_DATE or other date parsing functions rather than by entering text.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c
- Google Sheets: https://support.google.com/docs/answer/3093249
