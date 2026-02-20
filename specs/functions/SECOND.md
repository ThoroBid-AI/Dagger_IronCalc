# SECOND
## SECOND
## Purpose
Return second component of time.
## Syntax
- Excel: `SECOND(serial_number)`
- Google Sheets: `SECOND(serial_number)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SECOND("00:00:59") -> 59`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_second`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1

- Summary: Returns the seconds of a time value. The second is given as an integer in the range 0 (zero) to 59.

- Signatures:

  - `SECOND(serial_number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Time 4:48:18 PM 4:48 PM Formula Description Result =SECOND(A3) Seconds in the first time (18) 18 =SECOND(A4) Seconds in the second time (0) 0

- Notes: Time: | 4:48:18 PM: | 4:48 PM: | Formula: Description | Result

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093054

- Summary: Return second component of time.

- Signatures:

  - `SECOND(time)`

- Examples:

  - SECOND("00:00:59")

- Notes: - Ensure that the input to the function is either a reference to a cell containing a date/time, a function which returns a date/time object such as TIME, or a date serial number of the type returned by the N function. Google Sheets represents dates and times as numbers; while conversion is automatic when a human-readable date is entered into a cell, functions only accept literal dates in numeric format. - SECOND does not autoconvert number formats in the same way that Google Sheets does upon direct entry into cells. Therefore, SECOND(12:00:00) will return an error. - SECOND returns the intuitive understanding of seconds, and is useful primari…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1
- Google Sheets: https://support.google.com/docs/answer/3093054
