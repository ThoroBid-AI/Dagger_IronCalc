# SUBTOTAL
## SUBTOTAL
## Purpose
Computes SUBTOTAL semantics for spreadsheet formulas.
## Syntax
- Excel: `SUBTOTAL(...)`
- Google Sheets: `SUBTOTAL(...)`
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
- Handler: `fn_subtotal`
- File: `base/src/functions/subtotal.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939

- Summary: How to use the SUBTOTAL function in Excel to return a subtotal in a list or database.

- Signatures:

  - `SUBTOTAL(function_num,ref1,[ref2],...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 120 10 150 23 Formula Description Result =SUBTOTAL(9,A2:A5) The sum of the subtotal of the cells A2:A5, using 9 as the first argument. 303 =SUBTOTAL(1,A2:A5) The average of the subtotal of the cells A2:A5, using 1 as the first argument. 75.75 Notes The SUBTOTAL function always requires a numeric argument (1 through 11, 101 through 111) as its first argument. This numeric argument is applied to the sub…

- Notes: - If there are other subtotals within ref1, ref2,… (or nested subtotals), these nested subtotals are ignored to avoid double counting. - For the function_num constants from 1 to 11, the SUBTOTAL function includes the values of rows hidden by the Hide Rows command under the Hide & Unhide submenu of the Format command in the Cells group on the Home tab in the Excel desktop application. Use these constants when you want to subtotal hidden and nonhidden numbers in a list. For the function_Num constants from 101 to 111, the SUBTOTAL function ignores values of rows hidden by the Hide Rows command. Use these constants when you want to subtotal only…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093649

- Summary: Returns a subtotal for a vertical range of cells using a specified aggregation function. Sample Usage SUBTOTAL(1,A2:A5,B2:B8) Syntax SUBTOTAL(function_code, range1, [range2, ...]) functio

- Signatures:

  - `SUBTOTAL(function_code, range1, [range2, ...])`

- Examples:

  - SUBTOTAL(1,A2:A5,B2:B8)

  - SUBTOTAL(function_code, range1, [range2, ...])

- Notes: - Cells that are hidden due to autofilter criteria are never included in SUBTOTAL, irrespective of the function_code used. - Cells within any of the specified range arguments that contain SUBTOTAL calls are ignored to prevent double-counting. - SUBTOTAL can be used to created dynamic dashboards by having the function code argument refer to another cell. When combined with list-based data validation, this cell can become a drop-down list that instantly updates the entire dashboard. - SUBTOTAL can be used for quick analysis of different subsets of data by building a subtotal dashboard above a filtered region. Each time the filter criteria chang…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939
- Google Sheets: https://support.google.com/docs/answer/3093649
