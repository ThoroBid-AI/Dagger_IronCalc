# RIGHTB

## RIGHTB

## Purpose
Byte-length variant of RIGHT.

## Syntax
- Excel: `RIGHTB(text, [num_bytes])`
- Google Sheets: `RIGHTB(text, [num_bytes])`

## Behavior
Uses byte count and supports multibyte text variants.

## Examples (expected outputs)
- `RIGHTB("hello",3)` -> `llo`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_rightb`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Byte-length variant of RIGHT.

- Signatures:

  - `RIGHTB(text, [num_bytes])`

- Examples:

  - RIGHTB("hello",3)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367697

- Source fetch status: failed after 4 attempts

- Summary: Byte-length variant of RIGHT.

- Signatures:

  - `RIGHTB(text, [num_bytes])`

- Examples:

  - RIGHTB("hello",3)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367697
