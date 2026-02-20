# SLOPE
## SLOPE
## Purpose
Returns the slope of the linear regression line through known data points.
## Syntax
- Excel: `SLOPE(known_ys, known_xs)`
- Google Sheets: `SLOPE(known_ys, known_xs)`
## Behavior
Computes covariance of y and x divided by variance of x using deterministic numeric arithmetic.
## Examples (expected outputs)
- `=SLOPE({2,4,6}, {1,2,3})` -> `2`
- `=SLOPE({5,7,9}, {1,2,3})` -> `2`
## Error Cases
- Mismatched range sizes -> `#N/A`.
- Zero variance in x -> `#DIV/0!`.
## Notes
Equivalent to LINEST slope for simple linear regression.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_slope`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs`
## Documentation (Microsoft)

- Source URL: https://support.microsoft.com/en-us/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9

- Summary: Returns the slope of the linear regression line through known data points.

- Signatures:

  - `SLOPE(known_ys, known_xs)`

- Examples: `=SLOPE({2,4,6}, {1,2,3})` -> `2`

- Notes: Equivalent to LINEST slope for simple linear regression.

- Error behavior: #DIV/0! when x variance is zero; #N/A for size mismatches.


## Documentation (Google Sheets)

- Source URL: https://support.google.com/docs/answer/3094048

- Summary: Returns the slope of the linear regression line through known data points.

- Signatures:

  - `SLOPE(known_y, known_x)`

- Examples: `=SLOPE({2,4,6}, {1,2,3})` -> `2`

- Notes: Equivalent to LINEST slope for simple linear regression.

- Error behavior: #DIV/0! when x variance is zero; #N/A for size mismatches.


## Sources
- Excel: https://support.microsoft.com/en-us/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9
- Google Sheets: https://support.google.com/docs/answer/3094048
