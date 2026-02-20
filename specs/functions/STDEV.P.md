# STDEV.P
## STDEV.P
## Purpose
Computes STDEV.P semantics for spreadsheet formulas.
## Syntax
- Excel: `STDEV.P(...)`
- Google Sheets: `STDEV.P(...)`
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
- Proposed handler: `fn_stdev.p`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195

- Summary: The STDEVP function calculates standard deviation based on the entire population given as arguments. The standard deviation is a measure of how widely values are dispersed from the average value (the mean).

- Signatures:

  - `STDEV.P(...)`

- Examples:

  - STDEV.P(...)

- Notes: - STDEVP assumes that its arguments are the entire population. If your data represents a sample of the population, then compute the standard deviation using STDEV. - For large sample sizes, STDEV and STDEVP return approximately equal values. - The standard deviation is calculated using the "n" method. - Arguments can either be numbers or names, arrays, or references that contain numbers. - Logical values, and text representations of numbers that you type directly into the list of arguments are counted. - If an argument is an array or reference, only numbers in that array or reference are counted. Empty cells, logical values, text, or error va…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094105

- Summary: Calculates the standard deviation based on an entire population. STDEVP for BigQuery Calculates the population standard deviation of a data column.

- Signatures:

  - `STDEV.P(...)`

- Examples:

  - STDEV.P(...)

- Notes: - Although STDEVP is specified as taking a maximum of 30 arguments, Google Sheets supports an arbitrary number of arguments for this function. - If the total number of values supplied as value arguments is not at least two, STDEVP will return the #DIV/0! error. - STDEVP will return an error if any of the value arguments include text. To calculate standard deviation while interpreting text values as 0, use STDEVPA. - STDEVP calculates standard deviation for an entire population. To calculate standard deviation across a sample, use STDEV. - STDEVP is equivalent to the square root of the variance, or SQRT(VARP(...)) using the same dataset.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195
- Google Sheets: https://support.google.com/docs/answer/3094105
