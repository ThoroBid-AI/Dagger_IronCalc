# REPLACEB

## REPLACEB

## Purpose
Byte-length variant of REPLACE.

## Syntax
- Excel: `REPLACEB(old_text, start_num, num_chars, new_text)`
- Google Sheets: `REPLACEB(old_text, start_num, num_chars, new_text)`

## Behavior
Uses byte counts instead of character counts.

## Examples (expected outputs)
- `REPLACEB("abcdef",2,2,"ZZ")` -> `aZZef`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_replaceb`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - REPLACEB("abcdef",2,2,"ZZ")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367752

- Summary: The REPLACEB function replaces part of a text string, based on a number of bytes, with a different text string. Parts of a REPLACEB function REPLACEB(text, position, num_bytes, new_text)

- Signatures:

  - `REPLACEB(text, position, num_bytes, new_text)`

  - `REPLACEB(A2, 2, 3,"new")`

  - `REPLACEB(A4, 2, 3,"new")`

- Examples: A B C 1 Input Formula Output 2 Aeñds =REPLACEB(A2, 2, 3,"new") Anews 3 Aeñds =REPLACE(A3, 2, 3,"new") Anews 4 熊本=熊本 =REPLACEB(A4, 2, 3,"new") 熊new熊本 5 熊本=熊本 =REPLACE(A5, 2, 3,"new") 熊new本

- Notes: - REPLACEB returns the same value as REPLACE if the input `text` has only single byte characters - This function returns text as the output. If a number is desired, try using the VALUE function in conjunction with this function.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367752
