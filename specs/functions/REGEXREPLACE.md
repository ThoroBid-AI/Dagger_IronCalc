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

- Summary: Replaces text based on regex match.

- Signatures:

  - `REGEXREPLACE(text, pattern, replacement, [occurrence], [case_sensitivity])`

- Examples:

  - REGEXREPLACE("abc123","\d+","")

- Notes: text (required): The text or the reference to a cell containing the text you want to replace strings within. | pattern (required): The regular expression ("regex") that describes the pattern of text you want to replace. | replacement (required): The text you want to replace instances of pattern. | occurrence: Specifies which instance of the pattern you want to replace. By default, occurrence is 0, which replaces all instances. A negative number replaces that instance, searching from the end.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098245

- Summary: Replaces text based on regex match.

- Signatures:

  - `REGEXREPLACE(text, regular_expression, replacement)`

- Examples:

  - REGEXREPLACE("Spreadsheets", "S.*d", "Bed")

  - REGEXREPLACE(text, regular_expression, replacement)

- Notes: - Google products use RE2 for regular expressions. Google Sheets supports RE2 except Unicode character class matching. Learn more on how to use RE2 expressions. - This function only works with text (not numbers) as input and returns text as output. If a number is desired as the output, try using the VALUE function in conjunction with this function. If numbers are used as input, convert them to text using the TEXT function.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/regexreplace-function-9c030bb2-5e47-4efc-bad5-4582d7100897
- Google Sheets: https://support.google.com/docs/answer/3098245
