# SINH
## SINH
## Purpose
Computes SINH semantics for spreadsheet formulas.
## Syntax
- Excel: `SINH(...)`
- Google Sheets: `SINH(...)`
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
- Handler: `fn_sinh`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7

- Summary: Returns the hyperbolic sine of a number.

- Signatures:

  - `SINH(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description R esult =2.868*SINH(0.0342*1.03) Probability of obtaining a result of less than 1.03 seconds. 0.1010491

- Notes: =2.868*SINH(0.0342*1.03): Probability of obtaining a result of less than 1.03 seconds. | 0.1010491

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093517

- Summary: The SINH function returns the hyperbolic sine of any real number. Sample Usage SINH(A2) SINH(1) Syntax SINH(value) value - Any real value to calculate the hyperbolic sine of.

- Signatures:

  - `SINH(value)`

- Examples:

  - SINH(A2)

  - SINH(1)

  - SINH(value)

- Notes: - Google Sheets does not support imaginary or complex numbers, so these are not valid inputs or outputs from hyperbolic functions.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7
- Google Sheets: https://support.google.com/docs/answer/3093517
