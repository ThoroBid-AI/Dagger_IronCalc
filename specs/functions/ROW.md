# ROW

## ROW

## Purpose
Returns row number of reference.

## Syntax
- Excel: `ROW([reference])`
- Google Sheets: `ROW([reference])`

## Behavior
Default returns current row when reference omitted.

## Examples (expected outputs)
- `ROW(A5)` -> `5`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_row`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d

- Summary: The ROW function in Excel returns the row number of a reference you enter in a formula. For example, =ROW(C10) returns row number 10. You can't use this function to insert or remove a row.

- Signatures:

  - `ROW([reference])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =ROW() Row in which the formula appears 2 =ROW(C10) Row of the reference 10

- Notes: =ROW(): Row in which the formula appears | 2 | =ROW(C10): Row of the reference | 10

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093316

- Summary: Returns the row number of a specified cell. Sample Usage ROW(A9) Syntax ROW([cell_reference]) cell_reference - [ OPTIONAL - The cell in which the formula is entered by default

- Signatures:

  - `ROW([cell_reference])`

- Examples:

  - ROW(A5)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d
- Google Sheets: https://support.google.com/docs/answer/3093316
