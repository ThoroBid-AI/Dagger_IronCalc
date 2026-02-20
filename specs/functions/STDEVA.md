# STDEVA
## STDEVA
## Purpose
Computes STDEVA semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEVA(...)`
- Google Sheets: `STDEVA(...)`
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
- Handler: `fn_stdeva`
- File: `base/src/functions/statistical/standard_dev.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d

- Summary: Syntax: STDEVA(value1, [value2], ...)

- Signatures:

  - `STDEVA(value1, [value2], ...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Strength 1345 1301 1368 1322 1310 1370 1318 1350 1303 1299 Formula Description (Result) Result =STDEVA(A3:A12) Standard deviation of breaking strength for all the tools (27.46391572) 27.46391572

- Notes: - STDEVA assumes that its arguments are a sample of the population. If your data represents the entire population, you must compute the standard deviation using STDEVPA. - The standard deviation is calculated using the "n-1" method. - Arguments can be the following: numbers; names, arrays, or references that contain numbers; text representations of numbers; or logical values, such as TRUE and FALSE, in a reference. - Arguments that contain TRUE evaluate as 1; arguments that contain text or FALSE evaluate as 0 (zero). - If an argument is an array or reference, only values in that array or reference are used. Empty cells and text values in the…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094055

- Summary: Calculates the standard deviation based on a sample, setting text to the value `0`. Sample Usage STDEVA(1,2,3,4,5,6,7,8,9,10) STDEVA(A2:A100) Syntax STDEVA(value1, [value2, ...]) value

- Signatures:

  - `STDEVA(value1, [value2, ...])`

- Examples:

  - STDEVA(1,2,3,4,5,6,7,8,9,10)

  - STDEVA(A2:A100)

  - STDEVA(value1, [value2, ...])

- Notes: - Although STDEVA is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, STDEVA will return the #DIV/0! error. - STDEVA sets each text value encountered to 0 for the purpose of calculation. - STDEVA calculates standard deviation for a sample. To calculate standard deviation across an entire population, use STDEVPA. - STDEVA is equivalent to the square root of the variance, or SQRT(VARA(...)) using the same dataset.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d
- Google Sheets: https://support.google.com/docs/answer/3094055
