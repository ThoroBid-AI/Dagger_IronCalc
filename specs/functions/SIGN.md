# SIGN
## SIGN
## Purpose
Computes SIGN semantics for spreadsheet formulas.
## Syntax
- Excel: `SIGN(...)`
- Google Sheets: `SIGN(...)`
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
- Handler: `fn_sign`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sign-function-109c932d-fcdc-4023-91f1-2dd0e916a1d8

- Summary: The SIGN function determines the sign of a number. IT returns 1 if the number is positive, zero (0) if the number is 0, and -1 if the number is negative.

- Signatures:

  - `SIGN(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =SIGN(10) Sign of a positive number. 1 =SIGN(4-4) Sign of the result of 4 minus 4 (zero). 0 =SIGN(-0.00001) Sign of a negative number. -1

- Notes: =SIGN(10): Sign of a positive number. | 1 | =SIGN(4-4): Sign of the result of 4 minus 4 (zero). | 0 | =SIGN(-0.00001): Sign of a negative number. | -1

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093513

- Summary: Given an input number, returns `-1` if it is negative, `1` if positive, and `0` if it is zero. Sample Usage SIGN(-42) SIGN(A2) Syntax SIGN(value) value - The value whose sign will be ev

- Signatures:

  - `SIGN(value)`

- Examples:

  - SIGN(-42)

  - SIGN(A2)

  - SIGN(value)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sign-function-109c932d-fcdc-4023-91f1-2dd0e916a1d8
- Google Sheets: https://support.google.com/docs/answer/3093513
