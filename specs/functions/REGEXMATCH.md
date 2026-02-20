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

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - REGEXMATCH("abc123","\d+")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098292

- Summary: Tests whether text matches regex pattern.

- Signatures:

  - `REGEXMATCH(text, regular_expression)`

- Examples:

  - REGEXMATCH("Spreadsheets", "S.r")

  - REGEXMATCH(text, regular_expression)

- Notes: - Google products use RE2 for regular expressions. Google Sheets supports RE2 except Unicode character class matching. Learn how to use RE2 expressions. - This function only works with text (not numbers) as input and returns a logical value, i.e. TRUE or FALSE, as output. If numbers are used as input, convert them to text using the TEXT function.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3098292
