# VDB
## VDB
## Purpose
Depreciation by declining-balance method with period schedules.
## Syntax
- Excel: `VDB(cost, salvage, life, start_period, end_period, factor, [no_switch])`
- Google Sheets: `VDB(cost, salvage, life, start_period, end_period, factor, [no_switch])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- VDB(2400,300,10,0,1,1.5,TRUE) -> value
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_vdb`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/vdb-function-dde4e207-f3fa-488d-91d2-66d55e861d73

- Source fetch status: failed after 4 attempts

- Summary: Depreciation by declining-balance method with period schedules.

- Signatures:

  - `VDB(cost, salvage, life, start_period, end_period, factor, [no_switch])`

- Examples: `=VDB(1,2,3)` -> `0`

  - VDB(2400,300,10,0,1,1.5,TRUE)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9199424

- Source fetch status: failed after 4 attempts

- Summary: Depreciation by declining-balance method with period schedules.

- Signatures:

  - `VDB(cost, salvage, life, start_period, end_period, factor, [no_switch])`

- Examples: `=VDB(1,2,3)` -> `0`

  - VDB(2400,300,10,0,1,1.5,TRUE)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/vdb-function-dde4e207-f3fa-488d-91d2-66d55e861d73
- Google Sheets: https://support.google.com/docs/answer/9199424
