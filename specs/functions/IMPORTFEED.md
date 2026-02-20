# IMPORTFEED

## IMPORTFEED

## Purpose
Imports a feed (e.g., RSS/ATOM) into table form.

## Syntax
- Excel: `IMPORTFEED(url, [query], [headers], [num_items], [sort], [sort_ascending])`
- Google Sheets: `IMPORTFEED(url, [query], [headers], [num_items], [sort], [sort_ascending])`

## Behavior
- Fetches and transforms feed format into tabular arrays.

## Examples (expected outputs)
- `IMPORTFEED("https://example.com/feed") -> data table`

## Error Cases
Malformed feed URLs and connectivity issues return errors.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importfeed`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importfeed`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Imports a feed (e.g., RSS/ATOM) into table form.

- Signatures:

  - `IMPORTFEED(url, [query], [headers], [num_items], [sort], [sort_ascending])`

- Examples:

  - IMPORTFEED("https://example.com/feed")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093337

- Source fetch status: failed after 4 attempts

- Summary: Imports a feed (e.g., RSS/ATOM) into table form.

- Signatures:

  - `IMPORTFEED(url, [query], [headers], [num_items], [sort], [sort_ascending])`

- Examples:

  - IMPORTFEED("https://example.com/feed")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093337
