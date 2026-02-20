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

- Source fetch status: failed after 4 attempts

- Summary: Byte-length variant of REPLACE.

- Signatures:

  - `REPLACEB(old_text, start_num, num_chars, new_text)`

- Examples:

  - REPLACEB("abcdef",2,2,"ZZ")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367752

- Source fetch status: failed after 4 attempts

- Summary: Byte-length variant of REPLACE.

- Signatures:

  - `REPLACEB(old_text, start_num, num_chars, new_text)`

- Examples:

  - REPLACEB("abcdef",2,2,"ZZ")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367752
