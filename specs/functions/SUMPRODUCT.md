# SUMPRODUCT
## SUMPRODUCT
## Purpose
Computes SUMPRODUCT semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMPRODUCT(...)`
- Google Sheets: `SUMPRODUCT(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_sumproduct`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e

- Summary: How to use the SUMPRODUCT function in Excel, one of Excel’s math and trig functions, using multiplication, addition, subtraction, and/or division to return the sum of the products of corresponding ranges or arrays.

- Signatures:

  - `SUMPRODUCT(array1, [array2], [array3], ...)`

- Examples: To create the formula using our sample list above, type =SUMPRODUCT(C2:C5,D2:D5) and press Enter. Each cell in column C is multiplied by its corresponding cell in the same row in column D, and the results are added up. The total amount for the groceries is $78.97. To write a longer formula that gives you the same result, type =C2*D2+C3*D3+C4*D4+C5*D5 and press Enter. After pressing Enter, the result is the same: $78.97. Cell C2 is multiplied by D2, and its result is added to the result of cell C3 times cell D3 and so on.

- Notes: - The array arguments must have the same dimensions. If they do not, SUMPRODUCT returns the #VALUE! error value. For example, =SUMPRODUCT(C2:C10,D2:D5) will return an error since the ranges aren't the same size. - SUMPRODUCT treats non-numeric array entries as if they were zeros. - For best performance, SUMPRODUCT should not be used with full column references. Consider =SUMPRODUCT(A:A,B:B), here the function will multiply the 1,048,576 cells in column A by the 1,048,576 cells in column B before adding them.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094294

- Summary: The SUMPRODUCT function calculates the sum of the products of corresponding entries in 2 equally sized arrays or ranges. Sample Usage SUMPRODUCT(A2:C5,D2:F5) SUMPRODUCT({1,2,3,4},{5,6,7,8}) Syntax

- Signatures:

  - `SUMPRODUCT(array1, [array2, ...])`

- Examples:

  - SUMPRODUCT(A2:C5,D2:F5)

  - SUMPRODUCT({1,2,3,4},{5,6,7,8})

  - SUMPRODUCT(array1, [array2, ...])

- Notes: - Matrix multiplication, MMULT, can also be accomplished using a combination of TRANSPOSE and SUMPRODUCT functions.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e
- Google Sheets: https://support.google.com/docs/answer/3094294
