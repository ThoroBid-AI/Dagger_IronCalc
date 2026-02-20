# TRIMMEAN
## TRIMMEAN
## Purpose
Computes TRIMMEAN semantics for spreadsheet formulas.
## Syntax
- Excel: `TRIMMEAN(...)`
- Google Sheets: `TRIMMEAN(...)`
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
- Proposed handler: `fn_trimmean`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/trimmean-function-d90c9878-a119-4746-88fa-63d988f511d3

- Summary: Returns the mean of the interior of a data set. TRIMMEAN calculates the mean taken by excluding a percentage of data points from the top and bottom tails of a data set.

- Signatures:

  - `TRIMMEAN(array, percent)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 4 5 6 7 2 3 4 5 1 2 3 Formula Description Result =TRIMMEAN(A2:A12,0.2) Mean of the interior of the data set contained in A2:A12, with 20 percent excluded from calculation. 3.778

- Notes: - If percent < 0 or percent > 1, TRIMMEAN returns the #NUM! error value. - TRIMMEAN rounds the number of excluded data points down to the nearest multiple of 2. If percent = 0.1, 10 percent of 30 data points equals 3 points. For symmetry, TRIMMEAN excludes a single value from the top and bottom of the data set.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094061

- Summary: Calculates the mean of a dataset excluding some proportion of data from the high and low ends of the dataset. Sample Usage TRIMMEAN(A2:A100,0.1) TRIMMEAN({1,1,2,3,5,8,13,21,34,55},0.05) Syntax TR

- Signatures:

  - `TRIMMEAN(data, exclude_proportion)`

- Examples:

  - TRIMMEAN(A2:A100,0.1)

  - TRIMMEAN({1,1,2,3,5,8,13,21,34,55},0.05)

  - TRIMMEAN(data, exclude_proportion)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trimmean-function-d90c9878-a119-4746-88fa-63d988f511d3
- Google Sheets: https://support.google.com/docs/answer/3094061
