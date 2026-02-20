# SQRT
## SQRT
## Purpose
Return square root.
## Syntax
- Excel: `SQRT(number)`
- Google Sheets: `SQRT(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SQRT(9) -> 3`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sqrt`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf

- Summary: Returns a positive square root.

- Signatures:

  - `SQRT(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data -16 Formula Description Result =SQRT(16) Square root of 16. 4 =SQRT(A2) Square root of -16. Because the number is negative, the #NUM! error message is returned. #NUM! =SQRT(ABS(A2)) Avoiding the #NUM! error message by first using the ABS function to find the absolute value of -16 and then finding the square root. 4

- Notes: -16: | Formula: Description | Result | =SQRT(16): Square root of 16. | 4 | =SQRT(A2): Square root of -16. Because the number is negative, the #NUM! error message is returned. | #NUM!

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093577

- Summary: Returns the positive square root of a positive number. Sample Usage SQRT(9) SQRT(A2) Syntax SQRT(value) value - The number for which to calculate the positive square root.

- Signatures:

  - `SQRT(value)`

- Examples:

  - SQRT(9)

  - SQRT(A2)

  - SQRT(value)

  - sqrt(Math.pow(k.width/2,2)

- Notes: - To find the negative root of value, simply multiply the result of the SQRT function call by -1.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf
- Google Sheets: https://support.google.com/docs/answer/3093577
