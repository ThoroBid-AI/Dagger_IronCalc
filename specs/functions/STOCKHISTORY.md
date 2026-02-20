# STOCKHISTORY
## STOCKHISTORY
## Purpose
Computes STOCKHISTORY semantics for spreadsheet formulas.
## Syntax
- Excel: `STOCKHISTORY(...)`
- Google Sheets: `STOCKHISTORY(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_stockhistory`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stockhistory-function-1ac8b5b3-5f62-4d94-8ab8-7504ec7239a8

- Summary: Computes STOCKHISTORY semantics for spreadsheet formulas.

- Signatures:

  - `STOCKHISTORY("XNAS:MSFT", "1/1/2022", "3/1/2022", 2, 0, 3)`

  - `STOCKHISTORY(stock, start_date, [end_date], [interval], [headers], [property0], [property1], [property2], [property3], [property4], [property5])`

- Examples:

  - STOCKHISTORY(stock, start_date, [end_date], [interval], [headers], [property0], [property1], [property2], [property3], [property4], [property5])

  - STOCKHISTORY("XNAS:MSFT", "1/1/2022", "3/1/2022", 2, 0, 3)

- Notes: - The STOCKHISTORY function does not stamp a format on the cells that it spills into. If you delete the formula, the cells that it filled have the General format. - When you enter the property arguments, you type a number for each property 0 through 5, in the order you want to see them. The value you enter for each property corresponds to the property number. For example, to include Date, Open, and Close, enter 0,2,1. These properties are defined as follows: Value Property Definition 0 Date If interval is daily or weekly, the first valid trading day in the period. If interval is monthly, the first day of the month, regardless of if it was a t…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=STOCKHISTORY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stockhistory-function-1ac8b5b3-5f62-4d94-8ab8-7504ec7239a8
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=STOCKHISTORY
