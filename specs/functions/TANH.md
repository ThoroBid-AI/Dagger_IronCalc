# TANH
## TANH
## Purpose
Returns hyperbolic tangent.
## Syntax
- Excel: `TANH(number)`
- Google Sheets: `TANH(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- TANH(0) -> 0
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_tanh`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tanh-function-017222f0-a0c3-4f69-9787-b3202295dc6c

- Summary: Returns the hyperbolic tangent of a number.

- Signatures:

  - `TANH(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description (Result) Result =TANH(-2) Hyperbolic tangent of -2 (-0.96403) -0.964028 =TANH(0) Hyperbolic tangent of 0 (0) 0 =TANH(0.5) Hyperbolic tangent of 0.5 (0.462117) 0.462117

- Notes: =TANH(-2): Hyperbolic tangent of -2 (-0.96403) | -0.964028 | =TANH(0): Hyperbolic tangent of 0 (0) | 0 | =TANH(0.5): Hyperbolic tangent of 0.5 (0.462117) | 0.462117

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093755

- Summary: The TANH function returns the hyperbolic tangent of any real number. Sample Usage TANH(A2) TANH(1) Syntax TANH(value) value - Any real value to calculate the hyperbolic tangent of.

- Signatures:

  - `TANH(value)`

- Examples:

  - TANH(A2)

  - TANH(1)

  - TANH(value)

- Notes: - Google Sheets does not support imaginary or complex numbers, so these are not valid inputs or outputs from hyperbolic functions.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tanh-function-017222f0-a0c3-4f69-9787-b3202295dc6c
- Google Sheets: https://support.google.com/docs/answer/3093755
