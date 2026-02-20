# SUMSQ
## SUMSQ
## Purpose
Computes SUMSQ semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMSQ(...)`
- Google Sheets: `SUMSQ(...)`
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
- Handler: `fn_sumsq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumsq-function-e3313c02-51cc-4963-aae6-31442d9ec307

- Summary: This article describes the formula syntax and usage of the SUMSQ function in Microsoft Excel.

- Signatures:

  - `SUMSQ(number1, [number2], ...)`

- Examples: Copy the following example content and paste it in cell A1 of a new Excel worksheet. The formula cell may automatically show the numeric result. Otherwise select it, press F2, and press Enter. Formula Description (Result) Result =SUMSQ(3, 4) Sum of the squares of 3 and 4 (25) 25

- Notes: - Arguments can be > numbers > names, arrays, or references containing numbers. - The count includes numbers, logical values, and text representations of numbers typed into the list. - If an argument is an array or reference, only numbers in that array or reference are counted. This function will ignore empty cells, logical values, text, or error values in the array or reference. - Errors will occur from > arguments that are error values > text that cannot be translated into numbers

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093714

- Summary: Returns the sum of the squares of a series of numbers and/or cells. Sample Usage SUMSQ(A2:A100) SUMSQ(1,2,3,4,5) SUMSQ(1,2,A2:A50) Syntax SUMSQ(value1, [value2, ...])

- Signatures:

  - `SUMSQ(value1, [value2, ...])`

- Examples:

  - SUMSQ(A2:A100)

  - SUMSQ(1,2,3,4,5)

  - SUMSQ(1,2,A2:A50)

  - SUMSQ(value1, [value2, ...])

- Notes: - If only a single number for value1 is supplied, SUMSQ returns value1 squared. - Although SUMSQ is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumsq-function-e3313c02-51cc-4963-aae6-31442d9ec307
- Google Sheets: https://support.google.com/docs/answer/3093714
