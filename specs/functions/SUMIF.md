# SUMIF
## SUMIF
## Purpose
Computes SUMIF semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMIF(...)`
- Google Sheets: `SUMIF(...)`
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
- Handler: `fn_sumif`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b

- Summary: How to use the SUMIF function in Excel to add the values in a range that meet criteria that you specify.

- Signatures:

  - `SUMIF(range, criteria, [sum_range])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Property Value Commission Data $100,000 $7,000 $250,000 $200,000 $14,000 $300,000 $21,000 $400,000 $28,000 Formula Description Result =SUMIF(A2:A5,">160000",B2:B5) Sum of the commissions for property values over $160,000. $63,000 =SUMIF(A2:A5,">160000") Sum of the property values over $160,000. $900,000 =SUMIF(A2:A5,300000,B2:B5) Sum of the commissions for property values equal to $300,000. $21,000 =SUMIF(…

- Notes: $100,000: $7,000 | $250,000 | $200,000: $14,000 | $300,000: $21,000 | $400,000: $28,000

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3093583

- Summary: Returns a conditional sum across a range. Examples Make a copy

- Signatures:

  - `SUMIF(criteria_column, criterion, sum_column)`

- Examples:
  - `=SUMIF(1, 2)`,
  - `=SUMIF(A1, B1)`,
  - `=SUMIF(10, 20, 30)`,
- Notes: - SUMIF can only perform conditional sums with a single criterion. To use multiple criteria, use the database function DSUM.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b
- Google Sheets: https://support.google.com/docs/answer/3093583
