# RIGHT

## RIGHT

## Purpose
Returns rightmost characters from text.

## Syntax
- Excel: `RIGHT(text, [num_chars])`
- Google Sheets: `RIGHT(text, [num_chars])`

## Behavior
Returns trailing characters up to requested length.

## Examples (expected outputs)
- `RIGHT("hello",2)` -> `lo`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_right`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns rightmost characters from text.

- Signatures:

  - `RIGHT(text, [num_chars])`

- Examples:

  - RIGHT("hello",2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094087

- Source fetch status: failed after 4 attempts

- Summary: Returns rightmost characters from text.

- Signatures:

  - `RIGHT(text, [num_chars])`

- Examples:

  - RIGHT("hello",2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094087
