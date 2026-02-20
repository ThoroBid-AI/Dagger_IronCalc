# T.INV.2T
## T.INV.2T
## Purpose
Computes T.INV.2T semantics for spreadsheet formulas.
## Syntax
- Excel: `T.INV.2T(...)`
- Google Sheets: `T.INV.2T(...)`
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
- Proposed handler: `fn_t.inv.2t`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-inv-2t-function-ce72ea19-ec6c-4be7-bed2-b9baf2264f17

- Summary: Returns the two-tailed inverse of the Student's t-distribution.

- Signatures:

  - `T.INV.2T(probability,deg_freedom)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 0.546449 Probability associated with the two-tailed Student's t-distribution 60 Degrees of freedom Formula Description (Result) Result =T.INV.2T(A2,A3) T-value of the Student's t-distribution for the terms above (0.606533076) 0.606533

- Notes: - If either argument is nonnumeric, T.INV.2T returns the #VALUE! error value. - If probability <= 0 or if probability > 1, T.INV.2T returns the #NUM! error value. - If deg_freedom is not an integer, it is truncated. - If deg_freedom < 1, T.INV.2T returns the #NUM! error value. - T.INV.2T returns that value t, such that P(|X| > t) = probability where X is a random variable that follows the t-distribution and P(|X| > t) = P(X < -t or X > t). - A one-tailed t-value can be returned by replacing probability with 2*probability. For a probability of 0.05 and degrees of freedom of 10, the two-tailed value is calculated with T.INV.2T(0.05,10), which r…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055811

- Summary: The T.INV.2T function calculates the inverse of the two-tailed TDIST function. Sample Usage T.INV.2T(0.35, 1) T.INV.2T(A1, A2) Syntax T.INV.2T(probability, degrees_freedom) probability

- Signatures:

  - `T.INV.2T(probability, degrees_freedom)`

- Examples:

  - T.INV.2T(probability, degrees_freedom)

- Notes: - T.INV.2T is to be used for the inverse of two-tailed TDIST functions. - T.INV.2T is synonymous with TINV. - To calculate the negative inverse of the one-tailed TDIST function, use T.INV. - Both arguments to T.INV.2T must be numeric or a destination cell whose value is numeric.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-inv-2t-function-ce72ea19-ec6c-4be7-bed2-b9baf2264f17
- Google Sheets: https://support.google.com/docs/answer/6055811
