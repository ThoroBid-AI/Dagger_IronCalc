# IMAGE

## IMAGE

## Purpose
Returns an image function reference from a URL or local source.

## Syntax
- Excel: `IMAGE(url, [mode], [height], [width], [top], [left], [bottom], [right])`
- Google Sheets: `IMAGE(url, [mode], [height], [width], [top], [left], [bottom], [right])`

## Behavior
- Represents image placement instruction in spreadsheet UIs; not a numeric transform function.

## Examples (expected outputs)
- `IMAGE("https://example.com/logo.png") -> image://https://example.com/logo.png`

## Error Cases
Invalid source URL/path should raise a value/runtime error in rendering mode.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/information.rs`
- Proposed handler: `fn_image`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_image`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/image-function-7e112975-5e52-4f2a-b9da-1d913d51f5d5

- Source fetch status: failed after 4 attempts

- Summary: Returns an image function reference from a URL or local source.

- Signatures:

  - `IMAGE(url, [mode], [height], [width], [top], [left], [bottom], [right])`

- Examples:

  - IMAGE("https://example.com/logo.png")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093333

- Source fetch status: failed after 4 attempts

- Summary: Returns an image function reference from a URL or local source.

- Signatures:

  - `IMAGE(url, [mode], [height], [width], [top], [left], [bottom], [right])`

- Examples:

  - IMAGE("https://example.com/logo.png")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/image-function-7e112975-5e52-4f2a-b9da-1d913d51f5d5
- Google Sheets: https://support.google.com/docs/answer/3093333
