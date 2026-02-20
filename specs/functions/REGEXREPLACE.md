# REGEXREPLACE

## REGEXREPLACE

## Purpose
Replaces text based on regex match.

## Syntax
- Excel: `REGEXREPLACE(text, regular_expression, replacement)`
- Google Sheets: `REGEXREPLACE(text, regular_expression, replacement)`

## Behavior
Substitutes first/all matches according to replacement text.

## Examples (expected outputs)
- `REGEXREPLACE("abc123","\d+","")` -> `abc`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_regexreplace`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/regexreplace-function-9c030bb2-5e47-4efc-bad5-4582d7100897

- Source fetch status: failed after 4 attempts

- Summary: Replaces text based on regex match.

- Signatures:

  - `REGEXREPLACE(text, regular_expression, replacement)`

- Examples:

  - REGEXREPLACE("abc123","\d+","")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098245

- Source fetch status: failed after 4 attempts

- Summary: Replaces text based on regex match.

- Signatures:

  - `REGEXREPLACE(text, regular_expression, replacement)`

- Examples:

  - REGEXREPLACE("abc123","\d+","")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/regexreplace-function-9c030bb2-5e47-4efc-bad5-4582d7100897
- Google Sheets: https://support.google.com/docs/answer/3098245
