# MID

## MID

## Purpose
Returns substring from text.

## Syntax
- Excel: `MID(text, start_num, num_chars)`
- Google Sheets: `MID(text, start_num, num_chars)`

## Behavior
- 1-based positional extraction.

## Examples (expected outputs)
- `MID("hello",2,2) -> "el"`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_mid`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns substring from text.

- Signatures:

  - `MID(text, start_num, num_chars)`

- Examples:

  - MID("hello",2,2)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094129

- Source fetch status: failed after 4 attempts

- Summary: Returns substring from text.

- Signatures:

  - `MID(text, start_num, num_chars)`

- Examples:

  - MID("hello",2,2)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094129
