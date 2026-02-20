# FILTERXML

## FILTERXML

## Purpose
Parses XML text and returns queried content using a path expression.

## Syntax
- Excel: `FILTERXML(xml, xpath)`
- Google Sheets: `FILTERXML(xml, xpath)`

## Behavior
- XML parser evaluates XPath-like path over a static XML string and returns textual/value extraction.

## Examples (expected outputs)
- `FILTERXML("<a><b>1</b></a>", "//b") -> 1`

## Error Cases
- Invalid XML, invalid path, or unsupported expressions return parse/runtime errors.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_filterxml`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/filterxml-function-4df72efc-11ec-4951-86f5-c1374812f5b7

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FILTERXML(xml, xpath)`

- Examples:

  - FILTERXML("<a><b>1</b></a>", "//b")

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid XML, invalid path, or unsupported expressions return parse/runtime errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=FILTERXML

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/filterxml-function-4df72efc-11ec-4951-86f5-c1374812f5b7
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=FILTERXML
