# REGEXEXTRACT

## REGEXEXTRACT

## Purpose
Extracts first substring matching regex.

## Syntax
- Excel: `REGEXEXTRACT(text, regular_expression)`
- Google Sheets: `REGEXEXTRACT(text, regular_expression)`

## Behavior
Returns first match string; errors if no match.

## Examples (expected outputs)
- `REGEXEXTRACT("abc123","\d+")` -> `123`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_regexextract`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/regexextract-function-4b96c140-9205-4b6e-9fbe-6aa9e783ff57

- Source fetch status: failed after 4 attempts

- Summary: Extracts first substring matching regex.

- Signatures:

  - `REGEXEXTRACT(text, regular_expression)`

- Examples:

  - REGEXEXTRACT("abc123","\d+")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098244

- Source fetch status: failed after 4 attempts

- Summary: Extracts first substring matching regex.

- Signatures:

  - `REGEXEXTRACT(text, regular_expression)`

- Examples:

  - REGEXEXTRACT("abc123","\d+")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/regexextract-function-4b96c140-9205-4b6e-9fbe-6aa9e783ff57
- Google Sheets: https://support.google.com/docs/answer/3098244
