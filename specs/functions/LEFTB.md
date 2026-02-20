# LEFTB

## LEFTB

## Purpose
Returns leftmost bytes from a text string.

## Syntax
- Excel: `LEFTB(text, [num_bytes])`
- Google Sheets: `LEFTB(text, [num_bytes])`

## Behavior
- Uses byte-length semantics for multi-byte encodings.

## Examples (expected outputs)
- `LEFTB("hello", 2) -> "he"`

## Error Cases
- Invalid count returns error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_leftb`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: LEFTB("hello", 2)

- Signatures:

  - `LEFTB(text, [num_bytes])`

- Examples:

  - LEFTB("hello", 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid count returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367470

- Source fetch status: failed after 4 attempts

- Summary: LEFTB("hello", 2)

- Signatures:

  - `LEFTB(text, [num_bytes])`

- Examples:

  - LEFTB("hello", 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid count returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367470
