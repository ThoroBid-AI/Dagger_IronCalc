# T.INV
## T.INV
## Purpose
Computes T.INV semantics for spreadsheet formulas.
## Syntax
- Excel: `T.INV(...)`
- Google Sheets: `T.INV(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.inv`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/tinv-function-a7c85b9d-90f5-41fe-9ca5-1cd2f3e1ed7c

- Summary: Returns the two-tailed inverse of the Student's t-distribution.

- Signatures:

  - `T.INV(...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 0.05464 Probability associated with the Student's two-tailed t-distribution 60 Degrees of freedom Formula Description Result =TINV(A2,A3) The t-value of the Student's t-distribution based on the arguments in A2 and A3. 1.96

- Notes: - If either argument is nonnumeric, TINV returns the #VALUE! error value. - If probability <= 0 or if probability > 1, TINV returns the #NUM! error value. - If deg_freedom is not an integer, it is truncated. - If deg_freedom < 1, TINV returns the #NUM! error value. - TINV returns that value t, such that P(|X| > t) = probability where X is a random variable that follows the t-distribution and P(|X| > t) = P(X < -t or X > t). - A one-tailed t-value can be returned by replacing probability with 2*probability. For a probability of 0.05 and degrees of freedom of 10, the two-tailed value is calculated with TINV(0.05,10), which returns 2.28139. The…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/6055811

- Summary: The T.INV.2T function calculates the inverse of the two-tailed TDIST function. Sample Usage T.INV.2T(0.35, 1) T.INV.2T(A1, A2) Syntax T.INV.2T(probability, degrees_freedom) probability

- Signatures:

  - `T.INV(...)`

- Examples:
  - `=T.INV(1, 2)`,
  - `=T.INV(A1, B1)`,
  - `=T.INV(10, 20, 30)`,
- Notes: - T.INV.2T is to be used for the inverse of two-tailed TDIST functions. - T.INV.2T is synonymous with TINV. - To calculate the negative inverse of the one-tailed TDIST function, use T.INV. - Both arguments to T.INV.2T must be numeric or a destination cell whose value is numeric.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tinv-function-a7c85b9d-90f5-41fe-9ca5-1cd2f3e1ed7c
- Google Sheets: https://support.google.com/docs/answer/6055811
