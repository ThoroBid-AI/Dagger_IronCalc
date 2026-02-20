# ROMAN

## ROMAN

## Purpose
Converts number to Roman numeral.

## Syntax
- Excel: `ROMAN(number, [form])`
- Google Sheets: `ROMAN(number, [form])`

## Behavior
Converts Arabic number to Roman numeric string with optional compact form.

## Examples (expected outputs)
- `ROMAN(1987)` -> `MCMLXXXVII`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_roman`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/roman-function-d6b0b99e-de46-4704-a518-b45a0f8b56f5

- Source fetch status: failed after 4 attempts

- Summary: Converts number to Roman numeral.

- Signatures:

  - `ROMAN(number, [form])`

- Examples:

  - ROMAN(1987)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094153

- Source fetch status: failed after 4 attempts

- Summary: Converts number to Roman numeral.

- Signatures:

  - `ROMAN(number, [form])`

- Examples:

  - ROMAN(1987)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/roman-function-d6b0b99e-de46-4704-a518-b45a0f8b56f5
- Google Sheets: https://support.google.com/docs/answer/3094153
