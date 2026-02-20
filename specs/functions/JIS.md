# JIS

## JIS

## Purpose
Converts text to Japanese Industrial Standards character set representation.

## Syntax
- Excel: `JIS(text)`
- Google Sheets: `JIS(text)`

## Behavior
- Character set conversion helper with deterministic encoding behavior.

## Examples (expected outputs)
- `JIS("abc") -> "abc"`

## Error Cases
- Unrepresentable values may return conversion error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_jis`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/jis-function-b72fb1a7-ba52-448a-b7d3-d2610868b7e2

- Source fetch status: failed after 4 attempts

- Summary: JIS("abc")

- Signatures:

  - `JIS(text)`

- Examples:

  - JIS("abc")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Unrepresentable values may return conversion error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=JIS

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/jis-function-b72fb1a7-ba52-448a-b7d3-d2610868b7e2
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=JIS
