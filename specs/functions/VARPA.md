# VARPA
## VARPA
## Purpose
Computes VARPA behavior for spreadsheet formulas.
## Syntax
- Excel: `VARPA(...)`
- Google Sheets: `VARPA(...)`
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
- Handler: `fn_varpa`
- File: `base/src/functions/statistical/variance.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96

- Summary: The VARPA function calculates variance based on the entire population.

- Signatures:

  - `VARPA(value1, [value2], ...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Strength 1345 1301 1368 1322 1310 1370 1318 1350 1303 1299 Formula Description Result =VARPA(A2:A11) Variance of breaking strengths for all the tools, assuming that only 10 tools are produced (entire population). 678.84 =VAR(A2:A11) This example uses the VAR function, which assumes a sample of the population, and returns a different result. 754.27

- Notes: - VARPA assumes that its arguments are the entire population. If your data represents a sample of the population, you must compute the variance by using VARA. - Arguments can be the following: numbers; names, arrays, or references that contain numbers; text representations of numbers; or logical values, such as TRUE and FALSE, in a reference. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - Arguments that contain TRUE evaluate as 1; arguments that contain text or FALSE evaluate as 0 (zero). - If an argument is an array or reference, only values in that array or reference are…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094065

- Summary: Calculates the variance based on an entire population, setting text to the value `0`. Sample Usage VARPA(1,2,3,4,5,6,7,8,9,10) VARPA(A2:A100) Syntax VARPA(value1, [value2, ...]) value1

- Signatures:

  - `VARPA(value1, [value2, ...])`

- Examples:

  - VARPA(1,2,3,4,5,6,7,8,9,10)

  - VARPA(A2:A100)

  - VARPA(value1, [value2, ...])

- Notes: - Although VARPA is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, VARPA will return the #NUM! error. - VARPA sets each text value encountered to 0 for the purpose of calculation. To return an error upon encountering text, use VARP. - VARPA calculates variance for an entire population. To calculate variance across a sample, use VARA. - VARPA takes the sum of the squares of each value's deviation from the mean and divides by the number of such values. This differs from the calculation of va…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96
- Google Sheets: https://support.google.com/docs/answer/3094065
