# LENB

## LENB

## Purpose
Returns byte length of a text string.

## Syntax
- Excel: `LENB(text)`
- Google Sheets: `LENB(text)`

## Behavior
- Counts bytes according to default encoding rules.

## Examples (expected outputs)
- `LENB("hello") -> 5`

## Error Cases
- Non-text values are coerced or return 0 by type policy.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_lenb`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns byte length of a text string.

- Signatures:

  - `LENB(text)`

- Examples:

  - LENB("hello")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values are coerced or return 0 by type policy.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367584

- Source fetch status: failed after 4 attempts

- Summary: Returns byte length of a text string.

- Signatures:

  - `LENB(text)`

- Examples:

  - LENB("hello")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values are coerced or return 0 by type policy.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367584
