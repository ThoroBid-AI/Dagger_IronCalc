# TAN
## TAN
## Purpose
Returns tangent of angle.
## Syntax
- Excel: `TAN(number)`
- Google Sheets: `TAN(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TAN(0) -> 0
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tan`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tan-function-08851a40-179f-4052-b789-d7f699447401

- Summary: Returns the tangent of the given angle. This requires the values to be a number. If your argument is in degrees, multiply it by PI()/180 or use the RADIANS function to convert it to radians.

- Signatures:

  - `TAN(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description (Result) Result =TAN(0.785) Tangent of 0.785 radians (0.99920) 0.99920 =TAN(45*PI()/180) Tangent of 45 degrees (1) 1 =TAN(RADIANS(45)) Tangent of 45 degrees (1) 1

- Notes: =TAN(0.785): Tangent of 0.785 radians (0.99920) | 0.99920 | =TAN(45*PI()/180): Tangent of 45 degrees (1) | 1 | =TAN(RADIANS(45)): Tangent of 45 degrees (1) | 1

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093586

- Summary: The TAN function returns the tangent of an angle provided in radians. Sample Usage TAN(PI()) TAN(A2) TAN(1) Syntax TAN(angle) angle - The angle to find the tangent

- Signatures:

  - `TAN(angle)`

- Examples:

  - TAN(PI()

  - TAN(A2)

  - TAN(1)

  - TAN(angle)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tan-function-08851a40-179f-4052-b789-d7f699447401
- Google Sheets: https://support.google.com/docs/answer/3093586
