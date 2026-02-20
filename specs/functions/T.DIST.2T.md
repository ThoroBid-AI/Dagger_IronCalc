# T.DIST.2T
## T.DIST.2T
## Purpose
Computes T.DIST.2T semantics for spreadsheet formulas.
## Syntax
- Excel: `T.DIST.2T(...)`
- Google Sheets: `T.DIST.2T(...)`
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
- Proposed handler: `fn_t.dist.2t`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-dist-2t-function-198e9340-e360-4230-bd21-f52f22ff5c28

- Summary: Returns the two-tailed Student's t-distribution. The Student's t-distribution is used in the hypothesis testing of small sample data sets. Use this function in place of a table of critical values for the t-distribution.

- Signatures:

  - `T.DIST.2T(x,deg_freedom)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 1.959999998 Value at which to evaluate the distribution 60 Degrees of freedom Formula Description (Result) Result =T.DIST.2T(A2,A3) Two-tailed distribution (0.054645, or 5.46 percent) 5.46%

- Notes: - If any argument is nonnumeric, T.DIST.2T returns the #VALUE! error value. - If deg_freedom < 1, T.DIST.2T returns the #NUM! error value. - If x < 0, then T.DIST.2T returns the #NUM! error value.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368252

- Summary: The T.DIST.2T function returns the two tailed Student distribution for a value x.&nbsp;Along with T.DIST.RT, this function replaces TDIST and is equivalent to calling TDIST with the tails argument set

- Signatures:

  - `T.DIST.2T(x, degrees_freedom)`

  - `T.DIST.2T(1.96, 60)`

  - `T.DIST.2T(1, 2)`

- Examples: Result for A1=T.DIST.2T(1.96, 60) A B 1 0.054644929736529 2 Result for A1=T.DIST.2T(1, 2) A B 1 0.42264973081037 2

- Notes: - If deg_freedom is less than 1, returns an #NUM error. - If x is negative, returns an #NUM error. - Along with T.DIST.RT, this formula replaces the TDIST formula. This is equivalent to calling the TDIST formula with tails = 2.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-dist-2t-function-198e9340-e360-4230-bd21-f52f22ff5c28
- Google Sheets: https://support.google.com/docs/answer/9368252
