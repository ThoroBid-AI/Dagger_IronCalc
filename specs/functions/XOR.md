# XOR
## XOR
## Purpose
Computes XOR behavior for spreadsheet formulas.
## Syntax
- Excel: `XOR(...)`
- Google Sheets: `XOR(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_xor`
- File: `base/src/functions/logical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/xor-function-1548d4c2-5e47-4f77-9a92-0533bba14f37

- Summary: Syntax: XOR(logical1, logical2,...)

- Signatures:

  - `XOR(logical1, [logical2],…)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. Formula Description Result =XOR(3>0,2<9) Because both of the two tests evaluates to TRUE, FALSE is returned. FALSE =XOR(3>12,4>6) Because all test results evaluate to FALSE, FALSE is returned. At least one of the test results must evaluate to TRUE to return TRUE. FALSE

- Notes: - The arguments must evaluate to logical values such as TRUE or FALSE, or in arrays or references that contain logical values. - If an array or reference argument contains text or empty cells, those values are ignored. - If the specified range contains no logical values, XOR returns the #VALUE! error value. - You can use an XOR array formula to see if a value occurs in an array. Note: If you have a current version of Microsoft 365, then you can simply enter the formula in the top-left-cell of the output range, then press ENTER to confirm the formula as a dynamic array formula. Otherwise, the formula must be entered as a legacy array formula b…

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116491

- Summary: The XOR function returns TRUE if an odd number of the provided arguments are logically true, and FALSE otherwise. Parts of a&nbsp;XOR formula XOR(logical_expression1, [logical_expression2, ...])

- Signatures:

  - `XOR(TRUE, FALSE, TRUE)`

  - `XOR(A2=TRUE, A3=FALSE)`

  - `XOR(A1:A10, B1:B10)`

  - `XOR(0, 1, 2, 3)`

- Examples: A B 1 Result Formula 2 TRUE =XOR(TRUE()) 3 FALSE =XOR(FALSE()) 4 FALSE =XOR(0) 5 TRUE =XOR(1) 6 TRUE =XOR(-3) A B C D 9 logical_expression1 logical_expression2 Result Formula 10 TRUE FALSE TRUE =XOR(A10,B10) 11 FALSE FALSE FALSE =XOR(A11,B11) 12 TRUE TRUE FALSE =XOR(A12,B12) 13 0 1 TRUE =XOR(A13,B13) 14 1 5 FALSE =XOR(A14,B14) A B 17 Result Formula 18 FALSE =XOR(A12,B13) 19 FALSE =XOR(B11,B12,B13) 20 TRUE =XOR(B11,B14)

- Notes: - The number 0 is logically false. All other numbers (including negative numbers) are logically true. - The XOR function accepts both logical value and range parameters. - Returns TRUE if an odd number of arguments are TRUE.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/xor-function-1548d4c2-5e47-4f77-9a92-0533bba14f37
- Google Sheets: https://support.google.com/docs/answer/9116491
