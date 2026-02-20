# IMPORTDATA

## IMPORTDATA

## Purpose
Imports data from a URL-delivered CSV or TSV.

## Syntax
- Excel: `IMPORTDATA(url, [delimiter], [separator])`
- Google Sheets: `IMPORTDATA(url)`

## Behavior
- Retrieves remote file content and parses into tabular array.

## Examples (expected outputs)
- `IMPORTDATA("https://example.com/data.csv") -> table`

## Error Cases
Network or URL errors return fetch/runtime error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importdata`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importdata`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Imports data from a URL-delivered CSV or TSV.

- Signatures:

  - `IMPORTDATA(url, [delimiter], [separator])`

- Examples:

  - IMPORTDATA("https://example.com/data.csv")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093335

- Source fetch status: failed after 4 attempts

- Summary: Imports data from a URL-delivered CSV or TSV.

- Signatures:

  - `IMPORTDATA(url)`

- Examples:

  - IMPORTDATA("https://example.com/data.csv")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093335
