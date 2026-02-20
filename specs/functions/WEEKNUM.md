# WEEKNUM
## WEEKNUM
## Purpose
Computes WEEKNUM behavior for spreadsheet formulas.
## Syntax
- Excel: `WEEKNUM(...)`
- Google Sheets: `WEEKNUM(...)`
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
- Handler: `fn_weeknum`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340

- Summary: Returns the week number of a specific date. For example, the week containing January 1 is the first week of the year, and is numbered week 1.

- Signatures:

  - `WEEKNUM(serial_number,[return_type])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 3/9/2012 Formula Description Result =WEEKNUM(A2) Number of the week in the year that 3/9/2012 occurs, based on weeks beginning on Sunday (default). 10 =WEEKNUM(A2,2) Number of the week in the year that 3/9/2012 occurs, based on a week beginning on Monday (the second argument, 2). 11

- Notes: 3/9/2012: | Formula: Description | Result | =WEEKNUM(A2): Number of the week in the year that 3/9/2012 occurs, based on weeks beginning on Sunday (default). | 10 | =WEEKNUM(A2,2): Number of the week in the year that 3/9/2012 occurs, based on a week beginning on Monday (the second argument, 2). | 11

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3294949

- Summary: Computes WEEKNUM behavior for spreadsheet formulas.

- Signatures:

  - `WEEKNUM(date, [type])`

- Examples:

  - WEEKNUM(DATE(1969, 7, 20)

  - WEEKNUM("12/09/1948", 2)

  - WEEKNUM("6/14/2002")

  - WEEKNUM(date, [type])

- Notes: - When inputting the date, it is best to use the DATE function, as text values may return errors. - Behind the scenes, there are two week numbering "systems" used for this function: - System 1 - The first week of the year is considered to be the week containing January 1, which is numbered week 1. - System 2 - The first week of the year is considered to be the week containing the first Thursday of the year, which is numbered as week 1. System 2 is the approach specified in ISO 8601, also known as the European system for numbering weeks. - For each type, the start day and end day of a week are defined as follows when counting week numbers: typ…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340
- Google Sheets: https://support.google.com/docs/answer/3294949
