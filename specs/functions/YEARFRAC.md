# YEARFRAC
## YEARFRAC
## Purpose
Computes YEARFRAC behavior for spreadsheet formulas.
## Syntax
- Excel: `YEARFRAC(...)`
- Google Sheets: `YEARFRAC(...)`
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
- Handler: `fn_yearfrac`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/yearfrac-function-3844141e-c76d-4143-82b6-208454ddc6a8

- Summary: This article describes the formula syntax and usage of the YEARFRAC function, which calculates the fraction of the year represented by the number of whole days between two dates (the start_date and the end_date).

- Signatures:

  - `YEARFRAC(start_date, end_date, [basis])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 1/1/2012 Start date 7/30/2012 End date Formula Description Result =YEARFRAC(A2,A3) Fraction of the year between 1/1/2012 and 7/30/12, omitting the Basis argument. 0.58055556 =YEARFRAC(A2,A3,1) Fraction between same dates, using the Actual/Actual basis argument. Because 2012 is a Leap year, it has a 366 day basis. 0.57650273 =YEARFRAC(A2,A3,3) Fraction between same dates, using the Actual/3…

- Notes: - Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2018 is serial number 43101 because it is 43,101 days after January 1, 1900. - All arguments are truncated to integers. - If start_date or end_date are not valid dates, YEARFRAC returns the #VALUE! error value. - If basis < 0 or if basis > 4, YEARFRAC returns the #NUM! error value.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092989

- Summary: Returns the number of years, including fractional years, between two dates using a specified day count convention. Sample Usage YEARFRAC(DATE(1969,7,16),DATE(1969,7,24),1) YEARFRAC(A2,A3) Syntax

- Signatures:

  - `YEARFRAC(start_date, end_date, [day_count_convention])`

- Examples:

  - YEARFRAC(start_date, end_date, [day_count_convention])

- Notes: - This function is mostly used in a financial setting, for calculation involving fixed-income securities. Because the most common calculations performed use the NASD standard calendar, this is the default behavior. However, for use in non-financial settings, option 1, Actual/Actual, is most likely the correct choice. - Ensure that the inputs to the function are either references to cells containing dates, functions which return date objects such as DATE, DATEVALUE or TO_DATE, or date serial numbers of the type returned by the N function. - YEARFRAC does not autoconvert number formats in the same way that Google Sheets does upon direct entry i…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/yearfrac-function-3844141e-c76d-4143-82b6-208454ddc6a8
- Google Sheets: https://support.google.com/docs/answer/3092989
