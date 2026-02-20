# SUM
## SUM
## Purpose
Computes SUM semantics for spreadsheet formulas.
## Syntax
- Excel: `SUM(...)`
- Google Sheets: `SUM(...)`
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
- Handler: `fn_sum`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89

- Summary: How to use the SUM function in Excel to add individual values, cell references, ranges, or a mix of all three.

- Signatures:

  - `SUM(number1,[number2],...)`

- Examples:

  - SUM(A2:A10)

  - SUM(A2:A10, C2:C10)

  - SUM(number1,[number2],...)

  - SUM(A1,A2,A3,B1,B2,B3)

  - SUM(A1:A3,B1:B3)

  - SUM(A6:C6)

- Notes: number1 Required: The first number you want to add. The number can be like 4, a cell reference like B6, or a cell range like B2:B8. | number2-255 Optional: This is the second number you want to add. You can specify up to 255 numbers in this way.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3093669

- Summary: Returns the sum of a series of numbers and/or cells. SUM for BigQuery Returns the sum of a data column. Sample Usage =SU

- Signatures:

  - `SUM(column)`

- Examples:
  - `=SUM(1, 2)`,
  - `=SUM(A1, B1)`,
  - `=SUM(10, 20, 30)`,
- Notes: - If only a single number for value1 is supplied, SUM returns value1. - Although SUM is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89
- Google Sheets: https://support.google.com/docs/answer/3093669
