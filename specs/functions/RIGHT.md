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

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - RIGHT("hello",2)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094087

- Summary: Returns rightmost characters from text.

- Signatures:

  - `RIGHT(string, [number_of_characters])`

- Examples:

  - RIGHT(A2,2)

  - RIGHT("lorem ipsum")

  - RIGHT(string, [number_of_characters])

- Notes: - 0 is a valid input for number_of_characters and will cause RIGHT to return the empty string.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094087
