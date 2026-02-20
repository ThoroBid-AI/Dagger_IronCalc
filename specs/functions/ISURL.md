# ISURL

## ISURL

## Purpose
Checks whether text resembles a URL.

## Syntax
- Excel: `ISURL(value)`
- Google Sheets: `ISURL(value)`

## Behavior
- Validates URL-like structure (scheme/host/path) without dereferencing.

## Examples (expected outputs)
- `ISURL("https://example.com") -> TRUE`

## Error Cases
- Non-text values return FALSE.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isurl`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Checks whether text resembles a URL.

- Signatures:

  - `ISURL(value)`

- Examples:

  - ISURL("https://example.com")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values return FALSE.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3256501

- Source fetch status: failed after 4 attempts

- Summary: Checks whether text resembles a URL.

- Signatures:

  - `ISURL(value)`

- Examples:

  - ISURL("https://example.com")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values return FALSE.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3256501
