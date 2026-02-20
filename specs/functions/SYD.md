# SYD
## SYD
## Purpose
Sum-of-years-digits depreciation calculation for an asset period.
## Syntax
- Excel: `SYD(cost, salvage, life, period)`
- Google Sheets: `SYD(cost, salvage, life, period)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- SYD(3000,1000,10,1) -> 266.67
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_syd`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27

- Summary: Returns the sum-of-years' digits depreciation of an asset for a specified period.

- Signatures:

  - `SYD(cost, salvage, life, per)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description $ 30,000.00 Initial cost $ 7,500.00 Salvage value 10 Lifespan in years Formula Description (Result) Result =SYD(A2,A3,A4,1) Yearly depreciation allowance for the first year (4,090.91) $4,090.91 =SYD(A2,A3,A4,10) Yearly depreciation allowance for the tenth year (409.09) $409.09

- Notes: SYD is calculated as follows:

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093261

- Summary: The SYD function calculates the depreciation of an asset for a specified period using the sum of years digits method. Sample Usage SYD(100,50,10,2) SYD(A2,A3,A4,A5) Syntax SYD(cost, salvage, life

- Signatures:

  - `SYD(cost, salvage, life, period)`

- Examples:

  - SYD(100,50,10,2)

  - SYD(A2,A3,A4,A5)

  - SYD(cost, salvage, life, period)

- Notes: - life and period must be measured in the same units.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27
- Google Sheets: https://support.google.com/docs/answer/3093261
