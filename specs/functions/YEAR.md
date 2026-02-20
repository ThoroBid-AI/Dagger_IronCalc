# YEAR
## YEAR
## Purpose
Computes YEAR behavior for spreadsheet formulas.
## Syntax
- Excel: `YEAR(...)`
- Google Sheets: `YEAR(...)`
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
- Handler: `fn_year`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9

- Summary: Returns the year corresponding to a date. The year is returned as an integer in the range 1900-9999. Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date is Hijri, the returned values for the YEAR, MONTH and DAY functions will be values associated with the equivalent Gregorian date.

- Signatures:

  - `YEAR(serial_number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Date 7/5/2023 7/5/2025 Formula Description (Result) Result =YEAR(A3) Year of the date in cell A3 (2008) 2023 =YEAR(A4) Year of the date in cell A4 (2010) 2025

- Notes: Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 45658 because it is 45,657 days after January 1, 1900. Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date is Hijri, the returned values for the YEAR, MONTH and DAY functions will be values associated with the equivalent Gregorian date.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093061

- Summary: Returns the year specified by a given date. Sample Usage YEAR(DATE(1969,7,20)) YEAR(A2) YEAR(40909) Syntax YEAR(date) date - The date from which to calculate the ye

- Signatures:

  - `YEAR(date)`

- Examples:

  - YEAR(date)

- Notes: - Ensure that the input to the function is either a reference to a cell containing a date, a function which returns a date object such as DATE, DATEVALUE or TO_DATE, or a date serial number of the type returned by the N function. Google Sheets represents dates and times as numbers; while conversion is automatic when a human-readable date is entered into a cell, functions only accept literal dates in numeric format. - YEAR does not autoconvert number formats in the same way that Google Sheets does upon direct entry into cells. Therefore, YEAR(10/10/2000) is interpreted as YEAR(0.005), the quotient of 10 divided by 10 divided by 2000.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9
- Google Sheets: https://support.google.com/docs/answer/3093061
