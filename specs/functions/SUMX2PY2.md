# SUMX2PY2
## SUMX2PY2
## Purpose
Computes SUMX2PY2 semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMX2PY2(...)`
- Google Sheets: `SUMX2PY2(...)`
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
- Handler: `fn_sumx2py2`
- File: `base/src/functions/mathematical_sum.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumx2py2-function-826b60b4-0aa2-4e5e-81d2-be704d3d786f

- Summary: The SUMX2PY2 function returns the sum of the sum of squares of corresponding values in two arrays. The sum of the sum of squares is a common term in many statistical calculations.

- Signatures:

  - `SUMX2PY2(array_x, array_y)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data First array Second array 2 6 3 5 9 11 1 7 8 5 7 4 5 4 Formula Description (Result) Result =SUMX2PY2(A3:A9,B3:B9) Sum of the sum of squares of the two arrays above (521) 521 =SUMX2PY2({2,3,9,1,8,7,5}, {6,5,11,7,5,4,4}) Sum of the sum of squares of the two arrays constants (521) 521

- Notes: - The arguments should be either numbers or names, arrays, or references that contain numbers. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included. - If array_x and array_y have a different number of values, SUMX2PY2 returns the #N/A error value. - The equation for the sum of the sum of squares is:

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094260

- Summary: Calculates the sum of the sums of the squares of values in two arrays. Sample Usage SUMX2PY2({1,2,3},{4,5,6}) SUMX2PY2(A2:A9,B2:B9) Syntax SUMX2PY2(array_x, array_y) array_x - T

- Signatures:

  - `SUMX2PY2(array_x, array_y)`

- Examples:

  - SUMX2PY2({1,2,3},{4,5,6})

  - SUMX2PY2(A2:A9,B2:B9)

  - SUMX2PY2(array_x, array_y)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumx2py2-function-826b60b4-0aa2-4e5e-81d2-be704d3d786f
- Google Sheets: https://support.google.com/docs/answer/3094260
