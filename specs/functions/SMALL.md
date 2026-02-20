# SMALL
## SMALL
## Purpose
Computes SMALL semantics for spreadsheet formulas.
## Syntax
- Excel: `SMALL(...)`
- Google Sheets: `SMALL(...)`
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
- Handler: `fn_small`
- File: `base/src/functions/statistical/count_and_average.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/small-function-17da8222-7c82-42b2-961b-14c45384df07

- Summary: Returns the k-th smallest value in a data set. Use this function to return values with a particular relative standing in a data set. For example, this function can give you first, second, and third place in a race.

- Signatures:

  - `SMALL(array, k)`

- Examples: Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 1 Data 2 3 1 4 4 5 8 2 3 3 7 4 12 6 54 4 8 7 23 Formula Description (Result) Result =SMALL(A2:A10,4) 4th smallest number in first column (4) 4 =SMALL(B2:B10,2) 2nd smallest number in the second column (3) 3

- Notes: - If array is empty, SMALL returns the #NUM! error value. - If k ≤ 0 or if k exceeds the number of data points, SMALL returns the #NUM! error value. - If n is the number of data points in array, SMALL(array,1) equals the smallest value, and SMALL(array,n) equals the largest value.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094050

- Summary: Returns the nth smallest element from a data set, where n is user-defined. Sample Usage SMALL(A2:B100,4) SMALL(A2:B100,C2) Syntax SMALL(data, n) data - The array or range contai

- Signatures:

  - `SMALL(data, n)`

- Examples:

  - SMALL(A2:B100,4)

  - SMALL(A2:B100,C2)

  - SMALL(data, n)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/small-function-17da8222-7c82-42b2-961b-14c45384df07
- Google Sheets: https://support.google.com/docs/answer/3094050
