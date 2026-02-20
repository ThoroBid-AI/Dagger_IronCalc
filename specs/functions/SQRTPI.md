# SQRTPI
## SQRTPI
## Purpose
Computes SQRTPI semantics for spreadsheet formulas.
## Syntax
- Excel: `SQRTPI(...)`
- Google Sheets: `SQRTPI(...)`
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
- Handler: `fn_sqrtpi`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sqrtpi-function-1fb4e63f-9b51-46d6-ad68-b3e7a8b519b4

- Summary: Returns the square root of (number * pi).

- Signatures:

  - `SQRTPI(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description (Result) R esult =SQRTPI(1) Square root of pi. 1.772454 =SQRTPI(2) Square root of 2 * pi. 2.506628

- Notes: =SQRTPI(1): Square root of pi. | 1.772454 | =SQRTPI(2): Square root of 2 * pi. | 2.506628

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093579

- Summary: Returns the positive square root of the product of Pi and the given positive number. Sample Usage SQRTPI(9) SQRTPI(A2) Syntax SQRTPI(value) value - The number which will be mult

- Signatures:

  - `SQRTPI(value)`

- Examples:

  - SQRTPI(9)

  - SQRTPI(A2)

  - SQRTPI(value)

- Notes: - To find the negative root of value * Pi, simply multiply the result of the SQRTPI function call by -1. - SQRTPI is used for certain types of analysis or as a component to other functions (e.g. an estimation of the Gamma function) and is rarely used by itself.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sqrtpi-function-1fb4e63f-9b51-46d6-ad68-b3e7a8b519b4
- Google Sheets: https://support.google.com/docs/answer/3093579
