# SHEET
## SHEET
## Purpose
Return worksheet index or name context.
## Syntax
- Excel: `SHEET([reference])`
- Google Sheets: `SHEET([reference])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SHEET() -> 1`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sheet`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sheet-function-44718b6f-8b87-47a1-a9d6-b701c06cff24

- Summary: Syntax: Sheet(value)

- Signatures:

  - `SHEET(value)`

- Examples: Copy the following entire table and paste it in cell A1 (and adjacent) of a new Excel worksheet. If you do not automatically see the results, select formula, press F2 and press Enter. Adjust column widths if needed to see everything. Formula Function (or failure) Result =SHEET(QSalesByRegion) Finds the number of the sheet called QSalesByRegion (having a scope that makes it available to the entire workbook). 2 =SHEET(Table1) Finds the sheet number containing the table named Table1... (who's scope makes it available to the entire workbook). 2 =SHEET(Hi_Temps) Returns the #NAME? error value because the sought name Hi_Temps is limited to the work…

- Notes: - SHEET locating/identification capability includes all worksheets (visible, hidden, or very hidden) in addition to all other sheet types (macro, chart, or dialog sheets). - If the value argument is not a valid reference, SHEET returns the #REF! error. For example, =SHEET(Sheet1!#REF) will return the #REF! error value. - If the value argument is not a valid sheet name, SHEET returns the #NA error value. For example, =SHEET(“badSheetName”) will return the #NA error value. - SHEET is not available in the Object Model (OM) because the Object Model already includes similar functionality.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=SHEET

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sheet-function-44718b6f-8b87-47a1-a9d6-b701c06cff24
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=SHEET
