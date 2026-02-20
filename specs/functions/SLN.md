# SLN
## SLN
## Purpose
Computes SLN semantics for spreadsheet formulas.
## Syntax
- Excel: `SLN(...)`
- Google Sheets: `SLN(...)`
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
- Handler: `fn_sln`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8

- Summary: Returns the straight-line depreciation of an asset for one period.

- Signatures:

  - `SLN(cost, salvage, life)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description $30,000 Cost $7,500 Salvage value 10 Years of useful life Formula Description Result =SLN(A2, A3, A4) The depreciation allowance for each year. $2,250

- Notes: $30,000: Cost | $7,500: Salvage value | 10: Years of useful life | Formula: Description | Result

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093245

- Summary: The SLN function calculates the depreciation of an asset for one period using the straight-line method. Sample Usage SLN(100,50,10) SLN(A2,A3,A4) Syntax SLN(cost, salvage, life) cost

- Signatures:

  - `SLN(cost, salvage, life)`

- Examples:

  - SLN(100,50,10)

  - SLN(A2,A3,A4)

  - SLN(cost, salvage, life)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8
- Google Sheets: https://support.google.com/docs/answer/3093245
