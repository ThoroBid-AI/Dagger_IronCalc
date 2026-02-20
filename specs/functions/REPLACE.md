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



- Source URL: https://support.microsoft.com/en-us/office/

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - REPLACE("abcdef",2,3,"ZZ")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098247

- Summary: Replaces part of text by position.

- Signatures:

  - `REPLACE(text, position, length, new_text)`

- Examples:

  - replace(/\-([a-z])

  - replace(RegExp("(^|[\\s]+)

  - replace(/([?&](continue|followup)

  - REPLACE("Spreadsheets", 1, 6, "Bed")

  - REPLACE(text, position, length, new_text)

  - replace(/"/g,""")

  - replace(/'/g,"'")

  - replace(/\+/g," ")

  - replace(Gha,function(f,h)

  - replace(/&([^;]+)

- Notes: - This function returns text as the output. If a number is desired, try using the VALUE function in conjunction with this function.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3098247
