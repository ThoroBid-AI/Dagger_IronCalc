# IMPORTHTML

## IMPORTHTML

## Purpose
Imports data from HTML tables or lists.

## Syntax
- Excel: `IMPORTHTML(url, query, index)`
- Google Sheets: `IMPORTHTML(url, query, index)`

## Behavior
- Parses DOM and extracts requested table/list block as array.

## Examples (expected outputs)
- `IMPORTHTML("https://example.com", "table", 1) -> table data`

## Error Cases
Invalid selector or network failures return errors.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importhtml`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importhtml`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Imports data from HTML tables or lists.

- Signatures:

  - `IMPORTHTML(url, query, index)`

- Examples:

  - IMPORTHTML("https://example.com", "table", 1)

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093339

- Source fetch status: failed after 4 attempts

- Summary: Imports data from HTML tables or lists.

- Signatures:

  - `IMPORTHTML(url, query, index)`

- Examples:

  - IMPORTHTML("https://example.com", "table", 1)

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093339
