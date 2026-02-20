# SHEETS
## SHEETS
## Purpose
Return number/list of sheets.
## Syntax
- Excel: `SHEETS([reference])`
- Google Sheets: `SHEETS([reference])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SHEETS() -> 1`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sheets`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sheets-function-770515eb-e1e8-45ce-8066-b557e5e4b80b

- Summary: Syntax: SHEETS(reference)

- Signatures:

  - `SHEETS(reference)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =SHEETS() Because there is no Reference argument specified, the total number of sheets in the workbook is returned (3). 3 =SHEETS(My3DRef) Returns the number of sheets in a 3D reference with the defined name My3DRef, which includes Sheet2 and Sheet3 (2). 2 Top of Page

- Notes: - SHEETS includes all worksheets (visible, hidden, or very hidden) in addition to all other sheet types (macro, chart, or dialog sheets). - If reference is not a valid value, SHEETS returns the #REF! error value. - SHEETS is not available in the Object Model (OM) because the Object Model already includes similar functionality.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=SHEETS

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sheets-function-770515eb-e1e8-45ce-8066-b557e5e4b80b
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=SHEETS
