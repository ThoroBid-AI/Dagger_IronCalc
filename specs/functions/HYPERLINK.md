# HYPERLINK

## HYPERLINK

## Purpose
Returns a hyperlink formula value linking display text to a target URL.

## Syntax
- Excel: `HYPERLINK(link_location, [friendly_name])`
- Google Sheets: `HYPERLINK(url, [label])`

## Behavior
- Represents link metadata and optional display label; evaluation is backend neutral in pure compute engines.

## Examples (expected outputs)
- `HYPERLINK("https://example.com", "Open") -> "Open"`

## Error Cases
Invalid URL/text arguments return a value error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/information.rs`
- Proposed handler: `fn_hyperlink`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_hyperlink`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hyperlink-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f

- Source fetch status: not captured in this snapshot

- Summary: Returns a hyperlink formula value linking display text to a target URL.

- Signatures:

  - `HYPERLINK(link_location, [friendly_name])`

- Examples:

  - HYPERLINK("https://example.com", "Open")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093313

- Source fetch status: not captured in this snapshot

- Summary: Returns a hyperlink formula value linking display text to a target URL.

- Signatures:

  - `HYPERLINK(url, [label])`

- Examples:

  - HYPERLINK("https://example.com", "Open")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hyperlink-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f
- Google Sheets: https://support.google.com/docs/answer/3093313
