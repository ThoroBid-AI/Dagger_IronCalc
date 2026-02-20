# STDEV.S
## STDEV.S
## Purpose
Computes STDEV.S semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEV.S(...)`
- Google Sheets: `STDEV.S(...)`
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
- Proposed handler: `fn_stdev.s`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23

- Summary: Syntax: STDEV.S(number1,[number2],...)

- Signatures:

  - `STDEV.S(number1,[number2],...)`

- Examples: Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. (Do not copy the cell containing the word "Data".) For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Strength 1345 1301 1368 1322 1310 1370 1318 1350 1303 1299 Formula Description Result =STDEV.S(A2:A11) Standard deviation of breaking strength. 27.46391572

- Notes: - STDEV.S assumes that its arguments are a sample of the population. If your data represents the entire population, then compute the standard deviation using STDEV.P. - The standard deviation is calculated using the "n-1" method. - Arguments can either be numbers or names, arrays, or references that contain numbers. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - If an argument is an array or reference, only numbers in that array or reference are counted. Empty cells, logical values, text, or error values in the array or reference are ignored. - Arguments that are error val…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094054

- Summary: The STDEV function calculates the standard deviation based on a sample. STDEV for BigQuery Calculates the sample standard deviation of a data column. S

- Signatures:

  - `STDEV.S(...)`

- Examples:

  - STDEV.S(...)

- Notes: - Although STDEV is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, STDEV will return the #DIV/0! error. - STDEV will return an error if any of the value arguments include text. If any of the value arguments reference a cell that contains text, those cells are ignored. To calculate standard deviation while interpreting text values as 0, use STDEVA. - STDEV calculates standard deviation for a sample. To calculate standard deviation across an entire population, use STDEVP. - STDEV is equivale…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23
- Google Sheets: https://support.google.com/docs/answer/3094054
