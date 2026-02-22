# SUMXMY2
## SUMXMY2
## Purpose
Computes SUMXMY2 semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMXMY2(...)`
- Google Sheets: `SUMXMY2(...)`
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
- Handler: `fn_sumxmy2`
- File: `base/src/functions/mathematical_sum.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumxmy2-function-9d144ac1-4d79-43de-b524-e2ecee23b299

- Summary: Returns the sum of squares of differences of corresponding values in two arrays.

- Signatures:

  - `SUMXMY2(array_x, array_y)`

- Examples: Copy the example content in the following table and paste it in cell A1 of a new Excel worksheet. If the formula does not automatically show results, select them, press F2, then press Enter. You may prefer to adjust column widths to more easily see all the data. Data First array Second array 2 6 3 5 9 11 1 7 8 5 7 4 5 4 Formula Description (Result) Result =SUMXMY2(A3:A9,B3:B9) Sum of squares of differences of the two arrays above (79) 79 =SUMXMY2({2, 3, 9, 1, 8, 7, 5}, {6, 5, 11, 7, 5, 4, 4}) Sum of squares of differences of the two arrays constants (79) 79

- Notes: - The arguments should be either > numbers or > names, arrays, or references that contain numbers - If an array or reference argument contains text, logical values, or empty cells, those values are ignored. However, cells with the value zero are included. - If array_x and array_y do not have the same number of values, SUMXMY2 returns the #N/A error value. - The equation for the sum of squared differences is:

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094298

- Summary: Calculates the sum of the squares of differences of values in two arrays. Sample Usage SUMXMY2({1,2,3},{4,5,6}) SUMXMY2(A2:A9,B2:B9) Syntax SUMXMY2(array_x, array_y) array_x - T

- Signatures:

  - `SUMXMY2(array_x, array_y)`

- Examples:

  - SUMXMY2({1,2,3},{4,5,6})

  - SUMXMY2(A2:A9,B2:B9)

  - SUMXMY2(array_x, array_y)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumxmy2-function-9d144ac1-4d79-43de-b524-e2ecee23b299
- Google Sheets: https://support.google.com/docs/answer/3094298
