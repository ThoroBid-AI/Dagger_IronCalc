# SERIESSUM
## SERIESSUM
## Purpose
Sum terms of a power series.
## Syntax
- Excel: `SERIESSUM(x, n, m, coefficients)`
- Google Sheets: `SERIESSUM(x, n, m, coefficients)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SERIESSUM(1,1,1,{1,2}) -> 3`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_seriessum`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/seriessum-function-a3ab25b5-1093-4f5b-b084-96c49087f637

- Summary: Returns the sum of a power series based on a formula.

- Signatures:

  - `SERIESSUM(x, n, m, coefficients)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Coefficients as numbers Coefficients as formulae 0.785398163 =PI()/4 1 1 -0.5 =-1/FACT(2) 0.041666667 =1/FACT(4) -0.001388889 =-1/FACT(6) Formula Description (Result) Result =SERIESSUM(A3,0,2,A4:A7) Approximation to the cosine of Pi/4 radians, or 45 degrees (0.707103) 0.707103

- Notes: Coefficients as numbers: Coefficients as formulae | 0.785398163: =PI()/4 | 1: 1 | -0.5: =-1/FACT(2)

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093444

- Summary: Given parameters x, n, m, and a, returns the power series sum a1xn + a2x(n+m) + ... + aix(n+(i-1)m), where i is the number of entries in range `a`. &nbsp; Sample Usage

- Signatures:

  - `SERIESSUM(x, n, m, a)`

- Examples:

  - SERIESSUM(1,0,1,{FACT(0)

  - SERIESSUM(A2,0,2,B2:B10)

  - SERIESSUM(x, n, m, a)

- Notes: - Power series may be used to approximate various constants and functions, including e (Euler's number), logarithms, integrals, trigonometric functions, etc. However, this function is usually used for custom user-defined models.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/seriessum-function-a3ab25b5-1093-4f5b-b084-96c49087f637
- Google Sheets: https://support.google.com/docs/answer/3093444
