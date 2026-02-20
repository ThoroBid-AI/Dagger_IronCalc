# TTEST
## TTEST
## Purpose
Computes TTEST semantics for spreadsheet formulas.
## Syntax
- Excel: `TTEST(...)`
- Google Sheets: `TTEST(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_t_test`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/t_dist.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae

- Summary: Returns the probability associated with a Student's t-Test. Use T.TEST to determine whether two samples are likely to have come from the same two underlying populations that have the same mean. Results from the test shows if the difference is statistically significant or from chance.

- Signatures:

  - `TTEST(array1,array2,tails,type)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 1 Data 2 3 6 4 19 5 3 8 2 9 14 1 4 2 5 4 17 5 1 Formula Description (Result) Result =TTEST(A2:A10,B2:B10,2,1) Probability associated with a Student's paired t-Test, with a two-tailed distribution. Uses values in A2:A10 and B2:B10. 0.19602

- Notes: - If array1 and array2 have a different number of data points, and type = 1 (paired), TTEST returns the #N/A error value. - The tails and type arguments are truncated to integers. - If tails or type is nonnumeric, TTEST returns the #VALUE! error value. - If tails is any value other than 1 or 2, TTEST returns the #NUM! error value. - TTEST uses the data in array1 and array2 to compute a non-negative t-statistic. If tails=1, TTEST returns the probability of a higher value of the t-statistic under the assumption that array1 and array2 are samples from populations with the same mean. The value returned by TTEST when tails=2 is double that returne…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055837

- Summary: Returns the probability associated with t-test. Determines whether two samples are likely to have come from the same two underlying populations that have the same mean. Sample Usage T.TEST(A1:A4, B1

- Signatures:

  - `TTEST(...)`

- Examples:

  - TTEST(...)

- Notes: - tails and type must be numeric. - range1 and range2 must have the same number of data points. - T.TEST uses the data in range1 and range2 to compute a non-negative test. If tails is set to 1, T.TEST returns the probability of a higher value of the t-statistic under the assumption that range1 and range2 are samples from populations with the same mean. The value returned by T.TEST when tails is set to 2 is double that returned when tails is set to 1 and corresponds to the probability of a higher absolute value of the t-statistic under the "same population means" assumption. - You can use TTEST or T.TEST to perform this function.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae
- Google Sheets: https://support.google.com/docs/answer/6055837
