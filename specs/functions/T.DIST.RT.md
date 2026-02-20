# T.DIST.RT
## T.DIST.RT
## Purpose
Computes T.DIST.RT semantics for spreadsheet formulas.
## Syntax
- Excel: `T.DIST.RT(...)`
- Google Sheets: `T.DIST.RT(...)`
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
- Proposed handler: `fn_t.dist.rt`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-dist-rt-function-20a30020-86f9-4b35-af1f-7ef6ae683eda

- Summary: Returns the right-tailed Student's t-distribution. The t-distribution is used in the hypothesis testing of small sample data sets. Use this function in place of a table of critical values for the t-distribution.

- Signatures:

  - `T.DIST.RT(x,deg_freedom)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 1.959999998 Value at which to evaluate the distribution 60 Degrees of freedom Formula Description (Result) Result =T.DIST.RT(A2,A3) Right-tailed distribution (0.027322, or 2.73 percent) 0.027322

- Notes: - If any argument is nonnumeric, T.DIST.RT returns the #VALUE! error value. - If deg_freedom < 1, T.DIST.RT returns the #NUM! error value.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9369017

- Summary: Returns the right tailed Student distribution for a value x.&nbsp;Along with T.DIST.2T, this function replaces TDIST and is equivalent to calling TDIST with the tails argument set to 1. Parts of a T.

- Signatures:

  - `T.DIST.RT(1.96, 60)`

  - `T.DIST.RT(-1.98, 2)`

- Examples: Result for A1=T.DIST.RT(1.96, 60) A B 1 0.027322464868265 2 Result for A1=T.DIST.RT(-1.98, 2) A B 1 0.9068737480782105 2

- Notes: - If deg_freedom is less than 1, returns an #NUM error. - This formula along with T.DIST.2T replace the TDIST formula. T.DIST.RT is equivalent to calling the TDIST formula with tails = 1.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-dist-rt-function-20a30020-86f9-4b35-af1f-7ef6ae683eda
- Google Sheets: https://support.google.com/docs/answer/9369017
