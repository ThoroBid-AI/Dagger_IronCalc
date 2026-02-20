# IMPORTXML

## IMPORTXML

## Purpose
Imports data from XML by XPath expressions.

## Syntax
- Excel: `IMPORTXML(url, xpath_query)`
- Google Sheets: `IMPORTXML(url, xpath_query)`

## Behavior
- Downloads XML and applies XPath to produce result array.

## Examples (expected outputs)
- `IMPORTXML("https://example.com/feed.xml", "//title") -> {"title"}`

## Error Cases
Invalid XML/XPath or fetch errors return error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importxml`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importxml`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Imports data from XML by XPath expressions.

- Signatures:

  - `IMPORTXML(url, xpath_query)`

- Examples:

  - IMPORTXML("https://example.com/feed.xml", "//title")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093342

- Source fetch status: failed after 4 attempts

- Summary: Imports data from XML by XPath expressions.

- Signatures:

  - `IMPORTXML(url, xpath_query)`

- Examples:

  - IMPORTXML("https://example.com/feed.xml", "//title")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093342
