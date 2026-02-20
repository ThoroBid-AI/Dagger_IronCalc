# SERIESSUM
## SERIESSUM
## Purpose
Sum terms of a power series.
## Syntax
- Excel: `SERIESSUM(x, n, m, coefficients)`
- Google Sheets: `SERIESSUM(x, n, m, coefficients)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SERIESSUM(1,1,1,{1,2}) -> 3`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_seriessum`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/seriessum-function-a3ab25b5-1093-4f5b-b084-96c49087f637

- Source fetch status: not captured in this snapshot

- Summary: Sum terms of a power series.

- Signatures:

  - `SERIESSUM(x, n, m, coefficients)`

- Examples:

  - SERIESSUM(1,1,1,{1,2})

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093444

- Source fetch status: not captured in this snapshot

- Summary: Sum terms of a power series.

- Signatures:

  - `SERIESSUM(x, n, m, coefficients)`

- Examples:

  - SERIESSUM(1,1,1,{1,2})

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/seriessum-function-a3ab25b5-1093-4f5b-b084-96c49087f637
- Google Sheets: https://support.google.com/docs/answer/3093444
