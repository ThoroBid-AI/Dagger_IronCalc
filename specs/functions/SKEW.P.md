# SKEW.P
## SKEW.P
## Purpose
Computes SKEW.P semantics for spreadsheet formulas.
## Syntax
- Excel: `SKEW.P(...)`
- Google Sheets: `SKEW.P(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_skew.p`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/skew-p-function-76530a5c-99b9-48a1-8392-26632d542fcb

- Summary: Syntax: SKEW.P(number1, number2,...)

- Signatures:

  - `SKEW.P(number 1, [number 2],…)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Population Data Set 3 4 5 2 3 4 5 6 4 7 Formula Description Result =SKEW.P(A2:A11) Skewness of a distribution based on the population of the data set in A2:A11 (0.303193). 0.303193 Top of Page

- Notes: - Arguments can either be numbers or names, arrays, or references that contain numbers. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero (0) are included. - SKEW.P uses the standard deviation of an entire population, not a sample. - If arguments are values that are not valid, SKEW.P returns the #NUM! error value. - If arguments use data types that are not valid, SKEW.P returns the #VALUE! error value. - If there are fewer than three da…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368569

- Summary: The SKEW.P function calculates the skewness of a dataset that represents the entire population. Skewness describes the symmetry of that dataset about the mean. Parts of a SKEW.P function SKEW.P(valu

- Signatures:

  - `SKEW.P(value1, value2)`

  - `SKEW.P(A2:A9)`

  - `SKEW.P(A2:A9, 30, 40)`

- Examples: A B 1 value 2 2 3 5 4 8 5 13 6 10 7 18 8 23 9 26 10 11 12 Result Formula 13 0.2763070768 =SKEW.P(A2:A9) 14 0.4621754338 =SKEW.P(A2:A9, 30, 40)

- Notes: - Although SKEW.P is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, SKEW.P will return the #DIV/0! error. - Any text encountered in the value arguments will be ignored. - Positive skewness indicates a longer tail extending in the positive direction, to the right of the mean, while negative skewness indicates a longer tail in the negative direction, to the left. Skewness nearer to zero indicates more symmetrical distributions.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/skew-p-function-76530a5c-99b9-48a1-8392-26632d542fcb
- Google Sheets: https://support.google.com/docs/answer/9368569
