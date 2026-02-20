# STANDARDIZE
## STANDARDIZE
## Purpose
Computes STANDARDIZE semantics for spreadsheet formulas.
## Syntax
- Excel: `STANDARDIZE(...)`
- Google Sheets: `STANDARDIZE(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_standardize`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standardize.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/standardize-function-81d66554-2d54-40ec-ba83-6437108ee775

- Summary: The STANDARDIZE function returns a normalized value from a distribution characterized by mean and standard_dev.

- Signatures:

  - `STANDARDIZE(x, mean, standard_dev)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 42 Value to normalize. 40 Arithmetic mean of the distribution. 1.5 Standard deviation of the distribution. Formula Description Result =STANDARDIZE(A2,A3,A4) Normalized value of 42, using 40 as the arithmetic mean and 1.5 as the standard deviation. 1.33333333

- Notes: - If standard_dev ≤ 0, STANDARDIZE returns the #NUM! error value. - The equation for the normalized value is:

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094102

- Summary: Calculates the normalized equivalent of a random variable given mean and standard deviation of the distribution. Sample Usage STANDARDIZE(96,80,6.7) STANDARDIZE(A2,A3,A4) Syntax STANDARDIZE(value

- Signatures:

  - `STANDARDIZE(value, mean, standard_deviation)`

- Examples:

  - STANDARDIZE(96,80,6.7)

  - STANDARDIZE(A2,A3,A4)

  - STANDARDIZE(value, mean, standard_deviation)

- Notes: - For a given dataset, mean can be calculated using AVERAGE or its related functions and standard_deviation can be calculated using STDEV or its related functions.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/standardize-function-81d66554-2d54-40ec-ba83-6437108ee775
- Google Sheets: https://support.google.com/docs/answer/3094102
