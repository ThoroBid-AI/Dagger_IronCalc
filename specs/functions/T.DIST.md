# T.DIST
## T.DIST
## Purpose
Computes T.DIST semantics for spreadsheet formulas.
## Syntax
- Excel: `T.DIST(...)`
- Google Sheets: `T.DIST(...)`
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
- Proposed handler: `fn_t.dist`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tdist-function-630a7695-4021-4853-9468-4a1f9dcdd192

- Summary: Returns the Percentage Points (probability) for the Student t-distribution where a numeric value (x) is a calculated value of t for which the Percentage Points are to be computed.

- Signatures:

  - `T.DIST(...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 1.959999998 Value at which to evaluate the distribution 60 Degrees of freedom Formula Description (Result) Result =TDIST(A2,A3,2) Two-tailed distribution (0.054644930, or 5.46 percent) 5.46% =TDIST(A2,A3,1) One-tailed distribution (0.027322465 or 2.73 percent) 2.73% Top of Page

- Notes: - If any argument is non-numeric, TDIST returns the #VALUE! error value. - If Deg_freedom < 1, TDIST returns the #NUM! error value. - The Deg_freedom and Tails arguments are truncated to integers. - If Tails is any value other than 1 or 2, TDIST returns the #NUM! error value. - If x < 0, then TDIST returns the #NUM! error value. - If Tails = 1, TDIST is calculated as TDIST = P( X>x ), where X is a random variable that follows the t-distribution. If Tails = 2, TDIST is calculated as TDIST = P(|X| > x) = P(X > x or X < -x). - Since x < 0 is not allowed, to use TDIST when x < 0, note that TDIST(-x,df,1) = 1 – TDIST(x,df,1) = P(X > -x) and TDIST(…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3295914

- Summary: Calculates the probability for Student's t-distribution with a given input (x). Sample Usage TDIST(A2, 30, 1) TDIST(0.5, 1, 2) Syntax TDIST(x, degrees_freedom, tails) x - The input to the t-di

- Signatures:

  - `T.DIST(...)`

- Examples:

  - T.DIST(...)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tdist-function-630a7695-4021-4853-9468-4a1f9dcdd192
- Google Sheets: https://support.google.com/docs/answer/3295914
