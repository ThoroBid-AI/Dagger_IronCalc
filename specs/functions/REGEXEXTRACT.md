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

- Summary: This article shows you how REGEXEXTRACT function allows you to extract text from a string based on a supplied regular expression.

- Signatures:

  - `REGEXEXTRACT(text, pattern, [return_mode], [case_sensitivity])`

- Examples:

  - REGEXEXTRACT("abc123","\d+")

- Notes: text (required): The text or the reference to a cell containing the text you want to extract strings from. | pattern (required): The regular expression ("regex") that describes the pattern of text you want to extract. | return_mode: A number that specifies what strings you want to extract. By default, return mode is 0. The possible values are: 0: Return the first string that matches the pattern 1: Return all strings that match the pattern as an array 2: Return capturing groups from the first match as an array Note: Capturing groups are parts of a regex pattern surrounded by parentheses "(...)". They allow you to return separate parts of a sin…

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098244

- Summary: Extracts first substring matching regex.

- Signatures:

  - `REGEXEXTRACT(text, regular_expression)`

- Examples:

  - REGEXEXTRACT("My favorite number is 241, but my friend's is 17", "\d+")

  - REGEXEXTRACT(text, regular_expression)

  - REGEXEXTRACT("You can also extract multiple values from text.”, “You can also (\w+)

- Notes: - Google products use RE2 for regular expressions. Google Sheets supports RE2 except Unicode character class matching. Learn more on how to use RE2 expressions. - This function only works with text (not numbers) as input and returns text as output. If a number is desired as the output, try using the VALUE function in conjunction with this function. If numbers are used as input, convert them to text using the TEXT function.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/regexextract-function-4b96c140-9205-4b6e-9fbe-6aa9e783ff57
- Google Sheets: https://support.google.com/docs/answer/3098244
