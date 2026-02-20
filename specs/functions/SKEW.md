# SKEW
## SKEW
## Purpose
Return skewness statistic.
## Syntax
- Excel: `SKEW(values...)`
- Google Sheets: `SKEW(values...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SKEW({1,2,3}) -> 0`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_skew`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/skew-function-bdf49d86-b1ef-4804-a046-28eaea69c9fa

- Summary: The SKEW function returns the skewness of a distribution. Skewness characterizes the degree of asymmetry of a distribution around its mean. Positive skewness indicates a distribution with an asymmetric tail extending toward more positive values.

- Signatures:

  - `SKEW(number1, [number2], ...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 3 4 5 2 3 4 5 6 4 7 Formula Description Result =SKEW(A2:A11) Skewness of a distribution of the data set in A2:A11. 0.359543

- Notes: - Arguments can either be numbers or names, arrays, or references that contain numbers. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included. - Arguments that are error values or text that cannot be translated into numbers cause errors. - If there are fewer than three data points, or the sample standard deviation is zero, SKEW returns the #DIV/0! error value. - The equation for skewness is defined as:

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094101

- Summary: Calculates the skewness of a dataset, which describes the symmetry of that dataset about the mean. Sample Usage SKEW(1,2,3,4,5,6,7,8,9,10) SKEW(A2:A100) Syntax SKEW(value1, [value2, ...])

- Signatures:

  - `SKEW(value1, [value2, ...])`

- Examples:

  - SKEW(1,2,3,4,5,6,7,8,9,10)

  - SKEW(A2:A100)

  - SKEW(value1, [value2, ...])

- Notes: - Although SKEW is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, SKEW will return the #DIV/0! error. - Any text encountered in the value arguments will be ignored. - Positive skewness indicates a longer tail extending in the positive direction, to the right of the mean, while negative skewness indicates a longer tail in the negative direction, to the left. Skewness nearer to zero indicates more symmetrical distributions.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/skew-function-bdf49d86-b1ef-4804-a046-28eaea69c9fa
- Google Sheets: https://support.google.com/docs/answer/3094101
