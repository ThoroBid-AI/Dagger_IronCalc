# REPLACE

## REPLACE

## Purpose
Replaces part of text by position.

## Syntax
- Excel: `REPLACE(old_text, start_num, num_chars, new_text)`
- Google Sheets: `REPLACE(old_text, start_num, num_chars, new_text)`

## Behavior
Returns resulting text after segment replacement.

## Examples (expected outputs)
- `REPLACE("abcdef",2,3,"ZZ")` -> `aZZf`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_replace`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a
- Source fetch status: not captured in this snapshot
- Summary: Replaces part of text by position.

- Signatures:

  - `REPLACE(old_text, start_num, num_chars, new_text)`

- Examples:

  - REPLACE("abcdef",2,3,"ZZ")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098247

- Source fetch status: not captured in this snapshot

- Summary: Replaces part of text by position.

- Signatures:

  - `REPLACE(old_text, start_num, num_chars, new_text)`

- Examples:

  - REPLACE("abcdef",2,3,"ZZ")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a
- Google Sheets: https://support.google.com/docs/answer/3098247
