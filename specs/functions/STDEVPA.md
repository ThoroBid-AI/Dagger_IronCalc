# STDEVPA
## STDEVPA
## Purpose
Computes STDEVPA semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEVPA(...)`
- Google Sheets: `STDEVPA(...)`
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
- Handler: `fn_stdevpa`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c

- Summary: Syntax: STDEVPA(value1, [value2], ...)

- Signatures:

  - `STDEVPA(value1, [value2], ...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Strength 1345 1301 1368 1322 1310 1370 1318 1350 1303 1299 Formula Description (Result) Result =STDEVPA(A3:A12) Standard deviation of breaking strength, assuming only 10 tools are produced (26.05455814) 26.05456

- Notes: - STDEVPA assumes that its arguments are the entire population. If your data represents a sample of the population, you must compute the standard deviation by using STDEVA. - For large sample sizes, STDEVA and STDEVPA return approximately equal values. - The standard deviation is calculated using the "n" method. - Arguments can be the following: numbers; names, arrays, or references that contain numbers; text representations of numbers; or logical values, such as TRUE and FALSE, in a reference. - Text representations of numbers that you type directly into the list of arguments are counted. - Arguments that contain TRUE evaluate as 1; argument…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094058

- Summary: Calculates the standard deviation based on an entire population, setting text to the value `0`. Sample Usage STDEVPA(1,2,3,4,5,6,7,8,9,10) STDEVPA(A2:A100) Syntax STDEVPA(value1, [value2, ...])

- Signatures:

  - `STDEVPA(value1, [value2, ...])`

- Examples:

  - STDEVPA(1,2,3,4,5,6,7,8,9,10)

  - STDEVPA(A2:A100)

  - STDEVPA(value1, [value2, ...])

- Notes: - Although STDEVPA is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, STDEVPA will return the #DIV/0! error. - STDEVPA sets each text value encountered to 0 for the purpose of calculation. To return an error upon encountering text, use STDEVP. - STDEVPA calculates standard deviation for an entire population. To calculate standard deviation across a sample, use STDEV. - STDEVPA is equivalent to the square root of the variance, or SQRT(VARPA(...)) using the same dataset.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c
- Google Sheets: https://support.google.com/docs/answer/3094058
