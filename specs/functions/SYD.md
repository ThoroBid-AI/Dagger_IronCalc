# SYD
## SYD
## Purpose
Sum-of-years-digits depreciation calculation for an asset period.
## Syntax
- Excel: `SYD(cost, salvage, life, period)`
- Google Sheets: `SYD(cost, salvage, life, period)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- SYD(3000,1000,10,1) -> 266.67
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_syd`
- File: `base/src/functions/financial.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27

- Source fetch status: failed after 4 attempts

- Summary: Sum-of-years-digits depreciation calculation for an asset period.

- Signatures:

  - `SYD(cost, salvage, life, period)`

- Examples:

  - SYD(3000,1000,10,1)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093261

- Source fetch status: failed after 4 attempts

- Summary: Sum-of-years-digits depreciation calculation for an asset period.

- Signatures:

  - `SYD(cost, salvage, life, period)`

- Examples:

  - SYD(3000,1000,10,1)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27
- Google Sheets: https://support.google.com/docs/answer/3093261
