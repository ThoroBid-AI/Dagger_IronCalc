# SECH
## SECH
## Purpose
Return hyperbolic secant of value.
## Syntax
- Excel: `SECH(number)`
- Google Sheets: `SECH(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SECH(0) -> 1`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sech`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sech-function-e05a789f-5ff7-4d7f-984a-5edb9b09556f

- Summary: Syntax: SECH(number)

- Signatures:

  - `SECH(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =SECH(45) The hyperbolic secant of a 45 degree angle. 5.73E-20 =SECH(30) The hyperbolic secant of a 30 degree angle. 1.87E-13 Top of Page

- Notes: - The absolute value of number must be less than 2^27. - If the angle is in degrees, either multiply the angle by PI()/180 or use the RADIANS function to covert the angle to radians. - If number is outside of its constraints, SECH returns the #NUM! error value. - If number is a non-numeric value, SECH returns the #VALUE! error values.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116560

- Summary: The SECH function returns the hyperbolic secant of an angle. Parts of a SECH formula SECH(value) Part Description va

- Signatures:

  - `SECH(A1)`

  - `SECH(1)`

  - `SECH(value)`

  - `SECH(-1)`

- Examples: A B 1 Formula Result 2 =SECH(1) 0.6480542737 3 =SECH(-1) 0.6480542737 4 =SECH(4) 0.03661899347

- Notes: value: Any real value to calculate the hyperbolic secant of. | 1: Formula | Result | 2: =SECH(1) | 0.6480542737 | 3: =SECH(-1) | 0.6480542737

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sech-function-e05a789f-5ff7-4d7f-984a-5edb9b09556f
- Google Sheets: https://support.google.com/docs/answer/9116560
