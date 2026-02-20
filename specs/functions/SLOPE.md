# SLOPE
## SLOPE
## Purpose
Computes SLOPE semantics for spreadsheet formulas.
## Syntax
- Excel: `SLOPE(...)`
- Google Sheets: `SLOPE(...)`
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
- Handler: `fn_slope`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9

- Summary: Returns the slope of the linear regression line through data points in known_y's and known_x's. The slope is the vertical distance divided by the horizontal distance between any two points on the line, which is the rate of change along the regression line.

- Signatures:

  - `SLOPE(known_y's, known_x's)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Known y Known x 1/2/1900 6 1/3/1900 5 1/9/1900 11 1/1/1900 7 1/8/1900 5 1/7/1900 4 1/5/1900 4 Formula Description Result =SLOPE(A3:A9,B3:B9) Slope of the linear regression line through the data points in A3:A9 and B3:B9. 0.305556

- Notes: - The arguments must be either numbers or names, arrays, or references that contain numbers. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included. - If known_y's and known_x's are empty or have a different number of data points, SLOPE returns the #N/A error value. - The equation for the slope of the regression line is: where x and y are the sample means AVERAGE(known_x’s) and AVERAGE(known_y’s). - The underlying algorithm used in the SLOPE and INTERCEPT functions is different than the underlying algorithm used in the LINEST function. The di…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094048

- Summary: Calculates the slope of the line resulting from linear regression of a dataset. Sample Usage SLOPE(A2:A100,B2:B100) Syntax SLOPE(data_y, data_x) data_y - The range representing the array

- Signatures:

  - `SLOPE(data_y, data_x)`

- Examples:

  - SLOPE(A2:A100,B2:B100)

  - SLOPE(data_y, data_x)

- Notes: - Any text encountered in the value arguments will be ignored.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9
- Google Sheets: https://support.google.com/docs/answer/3094048
