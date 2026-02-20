# SUMX2MY2
## SUMX2MY2
## Purpose
Computes SUMX2MY2 semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMX2MY2(...)`
- Google Sheets: `SUMX2MY2(...)`
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
- Handler: `fn_sumx2my2`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumx2my2-function-9e599cc5-5399-48e9-a5e0-e37812dfa3e9

- Summary: The SUMX2MY2 function returns the sum of the difference of squares of corresponding values in two arrays.

- Signatures:

  - `SUMX2MY2(array_x, array_y)`

- Examples: Copy the example content in the following table (including the formula rows) and paste in cell A1 of a new Excel worksheet. If the formulas do not automatically show results, you can select then press F2 and press Enter. Adjust column widths as needed to see all of the data. Data First array Second array 2 6 3 5 9 11 1 7 8 5 7 4 5 4 Formula Description (Result) Result =SUMX2MY2(A2:A8,B2:B8) Sum of the difference of squares of the two arrays above (-55) -55 =SUMX2MY2({2, 3, 9, 1, 8, 7, 5}, {6, 5, 11, 7, 5, 4, 4}) Sum of the difference of squares of the two arrays constants (-55) -55

- Notes: - The arguments should be either > numbers or > names, arrays, or references that contain numbers. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored. However, cells with the value zero are included. - If array_x and array_y have a different number of values, the SUMX2MY2 function returns the #N/A error value. - The equation for the sum of the difference of squares is:

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094257

- Summary: Calculates the sum of the differences of the squares of values in two arrays. Sample Usage SUMX2MY2({1,2,3},{4,5,6}) SUMX2MY2(A2:A9,B2:B9) Syntax SUMX2MY2(array_x, array_y) array_x

- Signatures:

  - `SUMX2MY2(array_x, array_y)`

- Examples:

  - SUMX2MY2({1,2,3},{4,5,6})

  - SUMX2MY2(A2:A9,B2:B9)

  - SUMX2MY2(array_x, array_y)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumx2my2-function-9e599cc5-5399-48e9-a5e0-e37812dfa3e9
- Google Sheets: https://support.google.com/docs/answer/3094257
