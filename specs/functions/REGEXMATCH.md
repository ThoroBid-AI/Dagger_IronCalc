# REGEXMATCH

## REGEXMATCH

## Purpose
Tests whether text matches regex pattern.

## Syntax
- Excel: `REGEXMATCH(text, regular_expression)`
- Google Sheets: `REGEXMATCH(text, regular_expression)`

## Behavior
Returns TRUE when a match exists.

## Examples (expected outputs)
- `REGEXMATCH("abc123","\d+")` -> `TRUE`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_regexmatch`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Tests whether text matches regex pattern.

- Signatures:

  - `REGEXMATCH(text, regular_expression)`

- Examples:

  - REGEXMATCH("abc123","\d+")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098292

- Source fetch status: failed after 4 attempts

- Summary: Tests whether text matches regex pattern.

- Signatures:

  - `REGEXMATCH(text, regular_expression)`

- Examples:

  - REGEXMATCH("abc123","\d+")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3098292
