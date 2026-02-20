# SIN
## SIN
## Purpose
Computes SIN semantics for spreadsheet formulas.
## Syntax
- Excel: `SIN(...)`
- Google Sheets: `SIN(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sin`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602

- Summary: Returns the sine of the given angle.

- Signatures:

  - `SIN(number)`

- Examples: Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =SIN(PI()) Sine of pi radians (0, approximately). 0.0 =SIN(PI()/2) Sine of pi/2 radians. 1.0 =SIN(30*PI()/180) Sine of 30 degrees. 0.5 =SIN(RADIANS(30)) Sine of 30 degrees. 0.5

- Notes: =SIN(PI()): Sine of pi radians (0, approximately). | 0.0 | =SIN(PI()/2): Sine of pi/2 radians. | 1.0 | =SIN(30*PI()/180): Sine of 30 degrees. | 0.5 | =SIN(RADIANS(30)): Sine of 30 degrees. | 0.5

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093447

- Summary: The SIN function returns the sine of an angle provided in radians. Sample Usage SIN(PI()) SIN(1) SIN(A2) Syntax SIN(angle) angle - The angle to find the sine of, in

- Signatures:

  - `SIN(angle)`

- Examples:

  - SIN(PI()

  - SIN(1)

  - SIN(A2)

  - SIN(angle)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602
- Google Sheets: https://support.google.com/docs/answer/3093447
