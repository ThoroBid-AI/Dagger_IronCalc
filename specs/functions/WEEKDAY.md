# WEEKDAY
## WEEKDAY
## Purpose
Computes WEEKDAY behavior for spreadsheet formulas.
## Syntax
- Excel: `WEEKDAY(...)`
- Google Sheets: `WEEKDAY(...)`
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
- Handler: `fn_weekday`
- File: `base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a

- Summary: Returns the day of the week corresponding to a date. The day is given as an integer, ranging from 1 (Sunday) to 7 (Saturday), by default.

- Signatures:

  - `WEEKDAY(serial_number,[return_type])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 2/14/2008 Formula Description (Result) Result =WEEKDAY(A2) Day of the week, with numbers 1 (Sunday) through 7 (Saturday) (5) 5 =WEEKDAY(A2, 2) Day of the week, with numbers 1 (Monday) through 7 (Sunday) (4) 4 =WEEKDAY(A2, 3) Day of the week, with numbers 0 (Monday) through 6 (Sunday) (3) 3

- Notes: 2/14/2008: | Formula: Description (Result) | Result | =WEEKDAY(A2): Day of the week, with numbers 1 (Sunday) through 7 (Saturday) (5) | 5 | =WEEKDAY(A2, 2): Day of the week, with numbers 1 (Monday) through 7 (Sunday) (4) | 4

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092985

- Summary: Returns a number representing the day of the week of the date provided. Sample Usage WEEKDAY(DATE(1969,7,20)) WEEKDAY(A2) WEEKDAY(40909) WEEKDAY(40909,3) Syntax WEEKDAY(date, [typ

- Signatures:

  - `WEEKDAY(date, [type])`

- Examples:

  - WEEKDAY(date, [type])

- Notes: - Ensure that the input to the function is either a reference to a cell containing a date, a function which returns a date object such as DATE, DATEVALUE or TO_DATE, or a date serial number of the type returned by the N function. Google Sheets represents dates internally as numbers for ease of use in calculation, and while this conversion is done automatically when a date in the form of a string is input into a cell, this function does not perform this conversion. - WEEKDAY does not autoconvert number formats in the same way that Google Sheets does upon direct entry into cells. Therefore, WEEKDAY(10/10/2000) is interpreted as WEEKDAY(0.0005),…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a
- Google Sheets: https://support.google.com/docs/answer/3092985
