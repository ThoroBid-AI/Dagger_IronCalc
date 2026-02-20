# SEC
## SEC
## Purpose
Return secant of angle.
## Syntax
- Excel: `SEC(number)`
- Google Sheets: `SEC(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SEC(0) -> 1`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sec`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sec-function-ff224717-9c87-4170-9b58-d069ced6d5f7

- Summary: Syntax: SEC(number)

- Signatures:

  - `SEC(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =SEC(45) Returns the secant of a 45 degree angle. 1.90359 =SEC(30) Returns the secant of a 30 degree angle. 6.48292 Top of Page

- Notes: - The absolute value of number must be less than 2^27. - If the angle is in degrees, either multiply the angle by PI()/180 or use the RADIANS function to covert the angle to radians. - If number is outside of its constraints, SEC returns the #NUM! error value. - If number is a non-numeric value, SEC returns the #VALUE! error values.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116395

- Summary: The SEC function returns the secant of an angle measured in radians. Parts of a SEC formula SEC(angle) Part Description

- Signatures:

  - `SEC(3.14)`

  - `SEC(A1)`

  - `SEC(angle)`

  - `SEC(1)`

- Examples: A B 1 Formula Result 2 =SEC(1) 1.850815718 3 =SEC(-1) 1.850815718 4 =SEC(4) -1.529885656 5 =SEC(0) 1

- Notes: angle: The angle to find the secant of, measured in radians. | 1: Formula | Result | 2: =SEC(1) | 1.850815718 | 3: =SEC(-1) | 1.850815718

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sec-function-ff224717-9c87-4170-9b58-d069ced6d5f7
- Google Sheets: https://support.google.com/docs/answer/9116395
