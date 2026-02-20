# FIND

## FIND

## Purpose
Returns the position of a substring inside text (case-sensitive).

## Syntax
- Excel: `FIND(find_text, within_text, [start_num])`
- Google Sheets: `FIND(find_text, within_text, [start_num])`

## Behavior
- 1-based indexing, supports start offset, empty or out-of-range inputs trigger errors, case-sensitive.

## Examples (expected outputs)
- `FIND("b", "abc") -> 2`

## Error Cases
- Returns #VALUE! when text is not found or start position is invalid.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_find`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FIND(find_text, within_text, [start_num])`

- Examples:

  - FIND("b", "abc")

- Notes: Implemented in IronCalc.

- Error behavior: Returns #VALUE! when text is not found or start position is invalid.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094126

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FIND(find_text, within_text, [start_num])`

- Examples:

  - FIND("b", "abc")

- Notes: Implemented in IronCalc.

- Error behavior: Returns #VALUE! when text is not found or start position is invalid.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094126
