# T
## T
## Purpose
Returns text argument as text or empty string.
## Syntax
- Excel: `T(value)`
- Google Sheets: `T(value)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- T("x") -> ""
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_t`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-function-fb83aeec-45e7-4924-af95-53e073541228

- Summary: Returns the text referred to by value.

- Signatures:

  - `T(value)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Rainfall 19 TRUE Formula Description (Result) Result =T(A2) Because the first value is text, the text is returned (Rainfall) Rainfall =T(A3) Because the second value is a number, empty text is returned () =T(A4) Because the third value is a logical value, empty text is returned ()

- Notes: - If value is or refers to text, T returns value. If value does not refer to text, T returns "" (empty text). - You do not generally need to use the T function in a formula because Microsoft Excel automatically converts values as necessary. This function is provided for compatibility with other spreadsheet programs.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094138

- Summary: Returns text argument as text or empty string.

- Signatures:

  - `T(value)`

- Examples:

  - T(a,b)

  - T(a.i,"gb_9a")

  - T(a.i,"gb_Xd")

  - T(a.i,"gb_8c")

  - T(a.i,"gb_cd")

  - T(a,"gb_S")

  - T(this.i,"gb_5a")

  - T(a.v,"gb_Me")

  - T(this.H()

  - T(a.V,"gb_S")

- Notes: - This function is rarely necessary as Google Sheets automatically converts between most formats appropriately. It is provided primarily for compatibility with formulas used in other spreadsheet packages.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-function-fb83aeec-45e7-4924-af95-53e073541228
- Google Sheets: https://support.google.com/docs/answer/3094138
