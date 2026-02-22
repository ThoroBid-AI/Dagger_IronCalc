# PROPER

## PROPER

## Purpose
Converts text to proper case (title case).

## Syntax
- Excel: `PROPER(text)`
- Google Sheets: `PROPER(text)`

## Behavior
Capitalizes each word in text; other characters become lower-case.

## Examples (expected outputs)
- `PROPER("john smith")` -> `John Smith`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_proper`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94

- Source fetch status: not captured in this snapshot

- Summary: Converts text to proper case (title case).

- Signatures:

  - `PROPER(text)`

- Examples:

  - PROPER("john smith")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094133

- Source fetch status: not captured in this snapshot

- Summary: Converts text to proper case (title case).

- Signatures:

  - `PROPER(text)`

- Examples:

  - PROPER("john smith")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94
- Google Sheets: https://support.google.com/docs/answer/3094133
