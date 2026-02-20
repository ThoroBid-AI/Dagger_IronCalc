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

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - RIGHTB("hello",3)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367697

- Summary: The RIGHTB function returns the right portion of a string up to a certain number of bytes. Parts of a RIGHTB function RIGHTB(string, num_of_bytes) Part Description

- Signatures:

  - `RIGHTB(string, num_of_bytes)`

  - `RIGHTB(A2, 2)`

  - `RIGHTB(A4, 2)`

- Examples: A B C 1 Input Formula Output 2 Aeñ =RIGHTB(A2, 2) eñ 3 Aeñ =RIGHT(A3,2) eñ 4 熊本 =RIGHTB(A4, 2) 本 5 熊本 =RIGHT(A5,2) 熊本

- Notes: - RIGHTB returns the same value as RIGHT if the input string has only single byte characters - num_of_bytes must be greater than or equal to zero. - If num_of_bytes is greater than the length of text in bytes, RIGHTB returns all of text. - If num_of_bytes is omitted, it is assumed to be 1.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367697
