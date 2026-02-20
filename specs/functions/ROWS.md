# ROWS

## ROWS

## Purpose
Returns count of rows in range.

## Syntax
- Excel: `ROWS(array)`
- Google Sheets: `ROWS(array)`

## Behavior
Counts rows in array or range.

## Examples (expected outputs)
- `ROWS({{1,2},{3,4}})` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rows`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597

- Summary: Syntax: ROWS(array)

- Signatures:

  - `ROWS(array)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =ROWS(C1:E4) Number of rows in the reference 4 =ROWS({1,2,3;4,5,6}) Number of rows in the array constant 2

- Notes: =ROWS(C1:E4): Number of rows in the reference | 4 | =ROWS({1,2,3;4,5,6}): Number of rows in the array constant | 2

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093382

- Summary: Returns the number of rows in a specified array or range. ROWS for BigQuery Returns the number of rows in a data column. Sample Usage

- Signatures:

  - `ROWS(column)`

- Examples:

  - ROWS({{1,2},{3,4}})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597
- Google Sheets: https://support.google.com/docs/answer/3093382
