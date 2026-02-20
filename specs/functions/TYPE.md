# TYPE
## TYPE
## Purpose
Computes TYPE semantics for spreadsheet formulas.
## Syntax
- Excel: `TYPE(...)`
- Google Sheets: `TYPE(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_type`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/type-function-45b4e688-4bc3-48b3-a105-ffa892995899

- Summary: Returns the type of value. Use TYPE when the behavior of another function depends on the type of value in a particular cell.

- Signatures:

  - `TYPE(value)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Smith Formula Description Result =TYPE(A2) Returns the type of the value in A2. The Text type is indicated by 2. 2 =TYPE("Mr. "&A2) Returns the type of "Mr. Smith, which is Text. 2 =TYPE(2+A2) Returns the type of the formula in C6, which returns 16, the type for the error message #VALUE! The error message #VALUE! is shown in C7. 16 =(2+A2) The error value returned by the formula =(2+A2), which is used…

- Notes: - TYPE is most useful when you are using functions that can accept different types of data, such as ARGUMENT and INPUT. Use TYPE to find out what type of data is returned by a function or formula. - You cannot use TYPE to determine whether a cell contains a formula. TYPE only determines the type of the resulting, or displayed, value. If value is a cell reference to a cell that contains a formula, TYPE returns the type of the formula's resulting value.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267375

- Summary: Returns a number associated with the type of data passed into the function. Sample Usage TYPE(C4) TYPE({1;2;3;4;5}) Syntax TYPE(value) value - The data whose type is to be determined.

- Signatures:

  - `TYPE(value)`

- Examples:

  - TYPE(C4)

  - TYPE({1;2;3;4;5})

  - TYPE(value)

- Notes: - This function returns the following numbers: - 1: if value is a number - 2: if value is text - 4: if value is boolean - 16: if value is an error - 64: if value is an array - 128: for any other type of cell. For example, in-cell images and sparklines. - The function cannot determine whether or not a cell or range of cells is using a formula, only returning the type of value being displayed in the cells.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/type-function-45b4e688-4bc3-48b3-a105-ffa892995899
- Google Sheets: https://support.google.com/docs/answer/3267375
