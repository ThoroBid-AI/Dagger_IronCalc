# WEBSERVICE
## WEBSERVICE
## Purpose
Fetches content from a URL.
## Syntax
- Excel: `WEBSERVICE(url)`
- Google Sheets: `WEBSERVICE(url)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- WEBSERVICE("https://...") -> response text
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/integration.rs`
- Proposed handler: `fn_webservice`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/webservice-function-0546a35a-ecc6-4739-aed7-c0b7ce1562c4

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible behavior required.

- Signatures:

  - `WEBSERVICE(url)`

- Examples:

  - WEBSERVICE("https://...")

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=WEBSERVICE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/webservice-function-0546a35a-ecc6-4739-aed7-c0b7ce1562c4
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=WEBSERVICE
