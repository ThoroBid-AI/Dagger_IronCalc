# SCAN
## SCAN
## Purpose
Scan/reduce across array values using a reducer.
## Syntax
- Excel: `SCAN(initial_value, array, lambda)`
- Google Sheets: `SCAN(initial_value, array, lambda)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SCAN(0,{1,2,3},LAMBDA(a,b,a+b)) -> {0,1,3,6}
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_scan`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29

- Source fetch status: failed after 4 attempts

- Summary: Scan/reduce across array values using a reducer.

- Signatures:

  - `SCAN(initial_value, array, lambda)`

- Examples:

  - SCAN(0,{1,2,3},LAMBDA(a,b,a+b)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12569094

- Source fetch status: failed after 4 attempts

- Summary: Scan/reduce across array values using a reducer.

- Signatures:

  - `SCAN(initial_value, array, lambda)`

- Examples:

  - SCAN(0,{1,2,3},LAMBDA(a,b,a+b)

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29
- Google Sheets: https://support.google.com/docs/answer/12569094
