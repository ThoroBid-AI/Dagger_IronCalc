# STEYX
## STEYX
## Purpose
Computes STEYX semantics for spreadsheet formulas.
## Syntax
- Excel: `STEYX(...)`
- Google Sheets: `STEYX(...)`
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
- Handler: `fn_steyx`
- File: `base/src/functions/statistical/correl.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab

- Summary: he STEYX function returns the standard error of the predicted y-value for each x in the regression. The standard error is a measure of the amount of error in the prediction of y for an individual x.

- Signatures:

  - `STEYX(known_y's, known_x's)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Known y Known x 2 6 3 5 9 11 1 7 8 5 7 4 5 4 Formula Description (Result) Result =STEYX(A3:A9,B3:B9) Standard error of the predicted y-value for each x in the regression (3.305719) 3.305719

- Notes: - Arguments can either be numbers or names, arrays, or references that contain numbers. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included. - Arguments that are error values or text that cannot be translated into numbers cause errors. - If known_y's and known_x's have a different number of data points, STEYX returns the #N/A error value. - If known_y's and known_x's are empty or have less than three data points, STEYX return…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094108

- Summary: Calculates the standard error of the predicted y-value for each x in the regression of a dataset. Sample Usage STEYX(A2:A100,B2:B100) Syntax STEYX(data_y, data_x) data_y - The range repre

- Signatures:

  - `STEYX(data_y, data_x)`

- Examples:

  - STEYX(A2:A100,B2:B100)

  - STEYX(data_y, data_x)

- Notes: - Any text encountered in the value arguments will be ignored.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab
- Google Sheets: https://support.google.com/docs/answer/3094108
