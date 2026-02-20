# SUMIFS
## SUMIFS
## Purpose
Computes SUMIFS semantics for spreadsheet formulas.
## Syntax
- Excel: `SUMIFS(...)`
- Google Sheets: `SUMIFS(...)`
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
- Handler: `fn_sumifs`
- File: `base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b

- Summary: How to use the SUMIFS function in Excel, one of Excel’s math and trig functions, to add arguments that meet multiple criteria.

- Signatures:

  - `SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`

  - `SUMIFS(A2:A9,B2:B9,"=A*",C2:C9,"Tom")`

  - `SUMIFS(A2:A9,B2:B9,"<>Bananas",C2:C9,"Tom")`

- Examples: To use these examples in Excel, drag to select the data in the table, right-click the selection, and pick Copy. In a new worksheet, right-click cell A1 and pick Match Destination Formatting under Paste Options. Quantity Sold Product Salesperson 5 Apples Tom 4 Apples Sarah 15 Artichokes Tom 3 Artichokes Sarah 22 Bananas Tom 12 Bananas Sarah 10 Carrots Tom 33 Carrots Sarah Formula Description =SUMIFS(A2:A9, B2:B9, "=A*", C2:C9, "Tom") Adds the number of products that begin with A and were sold by Tom. It uses the wildcard character * in Criteria1, "=A*" to look for matching product names in Criteria_range1 B2:B9, and looks for the name "Tom" in…

- Notes: Sum_range (required): The range of cells to sum. | Criteria_range1 (required): The range that is tested using Criteria1. Criteria_range1 and Criteria1 set up a search pair whereby a range is searched for specific criteria. Once items in the range are found, their corresponding values in Sum_range are added. | Criteria1 (required): The criteria that defines which cells in Criteria_range1 will be added. For example, criteria can be entered as 32, ">32", B4, "apples", or "32". | Criteria_range2, criteria2, … (optional): Additional ranges and their associated criteria. You can enter up to 127 range/criteria pairs.

- Error behavior: Problem Description 0 (Zero) is shown instead of the expected result. Make sure Criteria1,2 are in quotation marks if you are testing for text values, like a person's name. The result is incorrect when Sum_range has TRUE or FALSE values. TRUE and FALSE values for Sum_range are evaluated differently, which may cause unexpected results when they're added. Cells in Sum_range that contain TRUE evaluate to 1. Those that contain FALSE evaluate to 0 (zero).



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3238496

- Summary: Returns the sum of a range depending on multiple criteria. SUMIFS for BigQuery Returns a conditional sum of a data column depending on multiple criteria.

- Signatures:

  - `SUMIFS(sum_column, criteria_column1, criterion1, criteria_column2, criterion2)`

- Examples:

  - SUMIFS(table_name!inventory, table_name!fruits, "Apple", table_name!price, ">5")

  - SUMIFS(sum_column, criteria_column1, criterion1, criteria_column2, criterion2)

  - SUMIFS(A1:A10, B1:B10, ">20")

  - SUMIFS(A1:A10, B1:B10, ">20", C1:C10, "<30")

  - SUMIFS(C1:C100, E1:E100, "Yes")

  - SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, criterion2, ...])

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b
- Google Sheets: https://support.google.com/docs/answer/3238496
