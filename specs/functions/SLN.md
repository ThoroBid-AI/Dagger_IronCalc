# SLN
## SLN
## Purpose
Returns the periodic straight-line depreciation amount.
## Syntax
- Excel: `SLN(cost, salvage_value, life)`
- Google Sheets: `SLN(cost, salvage_value, life)`
## Behavior
Returns a constant depreciation amount for each period: (cost - salvage_value) / life.
## Examples (expected outputs)
- `=SLN(30000, 0, 10)` -> `3000`
- `=SLN(5000, 500, 5)` -> `900`
## Error Cases
- Negative or zero life -> `#NUM!`.
- Missing/invalid numeric inputs -> `#VALUE!`
## Notes
Used for linear fixed depreciation schedules.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sln`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`
## Documentation (Microsoft)

- Source URL: https://support.microsoft.com/en-us/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8

- Summary: Returns the periodic straight-line depreciation amount.

- Signatures:

  - `SLN(cost, salvage_value, life)`

- Examples: `=SLN(30000, 0, 10)` -> `3000`

- Notes: Used for linear fixed depreciation schedules.

- Error behavior: #NUM! for zero/negative life; #VALUE! for invalid argument count or types.


## Documentation (Google Sheets)

- Source URL: https://support.google.com/docs/answer/3093245

- Summary: Returns the periodic straight-line depreciation amount.

- Signatures:

  - `SLN(cost, salvage, life)`

- Examples: `=SLN(30000, 0, 10)` -> `3000`

- Notes: Used for linear fixed depreciation schedules.

- Error behavior: #NUM! for zero/negative life; #VALUE! for invalid argument count or types.


## Sources
- Excel: https://support.microsoft.com/en-us/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8
- Google Sheets: https://support.google.com/docs/answer/3093245
