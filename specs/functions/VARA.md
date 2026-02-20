# VARA
## VARA
## Purpose
Computes VARA behavior for spreadsheet formulas.
## Syntax
- Excel: `VARA(...)`
- Google Sheets: `VARA(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_vara`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07

- Summary: Estimates variance based on a sample.

- Signatures:

  - `VARA(value1, [value2], ...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Strength 1345 1301 1368 1322 1310 1370 1318 1350 1303 1299 Formula Description R esult =VARA(A2:A11) Estimates the variance for the breaking strength of the tools being tested. VARA assumes a population sample. 754.26667

- Notes: - VARA assumes that its arguments are a sample of the population. If your data represents the entire population, you must compute the variance by using VARPA. - Arguments can be the following: numbers; names, arrays, or references that contain numbers; text representations of numbers; or logical values, such as TRUE and FALSE, in a reference. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - Arguments that contain TRUE evaluate as 1; arguments that contain text or FALSE evaluate as 0 (zero). - If an argument is an array or reference, only values in that array or reference are…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094064

- Summary: Calculates the variance based on a sample, setting text to the value `0`. Sample Usage VARA(1,2,3,4,5,6,7,8,9,10) VARA(A2:A100) Syntax VARA(value1, [value2, ...]) value1 - The f

- Signatures:

  - `VARA(value1, [value2, ...])`

- Examples:

  - VARA(1,2,3,4,5,6,7,8,9,10)

  - VARA(A2:A100)

  - VARA(value1, [value2, ...])

- Notes: - Although VARA is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, VARA will return the #DIV/0! error. - VARA sets each text value encountered to 0 for the purpose of calculation. To return an error upon encountering text, use VAR. - VARA calculates variance for a sample. To calculate variance across an entire population, use VARPA. - VARA takes the sum of the squares of each value's deviation from the mean and divides by the number of such values minus one. This differs from the calculatio…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07
- Google Sheets: https://support.google.com/docs/answer/3094064
