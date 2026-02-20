# T.TEST
## T.TEST
## Purpose
Computes T.TEST semantics for spreadsheet formulas.
## Syntax
- Excel: `T.TEST(...)`
- Google Sheets: `T.TEST(...)`
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
- Proposed handler: `fn_t.test`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae

- Summary: Returns the probability associated with a Student's t-Test. Use T.TEST to determine whether two samples are likely to have come from the same two underlying populations that have the same mean. Results from the test shows if the difference is statistically significant or from chance.

- Signatures:

  - `T.TEST(...)`

- Examples:

  - T.TEST(...)

- Notes: - If array1 and array2 have a different number of data points, and type = 1 (paired), TTEST returns the #N/A error value. - The tails and type arguments are truncated to integers. - If tails or type is nonnumeric, TTEST returns the #VALUE! error value. - If tails is any value other than 1 or 2, TTEST returns the #NUM! error value. - TTEST uses the data in array1 and array2 to compute a non-negative t-statistic. If tails=1, TTEST returns the probability of a higher value of the t-statistic under the assumption that array1 and array2 are samples from populations with the same mean. The value returned by TTEST when tails=2 is double that returne…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055837

- Summary: Returns the probability associated with t-test. Determines whether two samples are likely to have come from the same two underlying populations that have the same mean. Sample Usage T.TEST(A1:A4, B1

- Signatures:

  - `T.TEST(range1, range2, tails, type)`

- Examples:

  - T.TEST(range1, range2, tails, type)

- Notes: - tails and type must be numeric. - range1 and range2 must have the same number of data points. - T.TEST uses the data in range1 and range2 to compute a non-negative test. If tails is set to 1, T.TEST returns the probability of a higher value of the t-statistic under the assumption that range1 and range2 are samples from populations with the same mean. The value returned by T.TEST when tails is set to 2 is double that returned when tails is set to 1 and corresponds to the probability of a higher absolute value of the t-statistic under the "same population means" assumption. - You can use TTEST or T.TEST to perform this function.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae
- Google Sheets: https://support.google.com/docs/answer/6055837
