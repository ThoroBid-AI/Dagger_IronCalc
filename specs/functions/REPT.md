# REPT

## REPT

## Purpose
Repeats text a number of times.

## Syntax
- Excel: `REPT(text, number_times)`
- Google Sheets: `REPT(text, number_times)`

## Behavior
Concatenates repeated text segments.

## Examples (expected outputs)
- `REPT("A",3)` -> `AAA`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rept`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rept-function-04c4d778-e712-43b4-9c15-d656582bb061

- Source fetch status: failed after 4 attempts

- Summary: Repeats text a number of times.

- Signatures:

  - `REPT(text, number_times)`

- Examples:

  - REPT("A",3)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094134

- Source fetch status: failed after 4 attempts

- Summary: Repeats text a number of times.

- Signatures:

  - `REPT(text, number_times)`

- Examples:

  - REPT("A",3)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rept-function-04c4d778-e712-43b4-9c15-d656582bb061
- Google Sheets: https://support.google.com/docs/answer/3094134
