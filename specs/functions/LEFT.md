# LEFT

## LEFT

## Purpose
Returns leftmost characters from a text string.

## Syntax
- Excel: `LEFT(text, [num_chars])`
- Google Sheets: `LEFT(text, [num_chars])`

## Behavior
- Returns prefix string of requested length with default 1.

## Examples (expected outputs)
- `LEFT("hello", 2) -> "he"`

## Error Cases
- Negative count returns error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_left`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: LEFT("hello", 2)

- Signatures:

  - `LEFT(text, [num_chars])`

- Examples:

  - LEFT("hello", 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Negative count returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094079

- Source fetch status: failed after 4 attempts

- Summary: LEFT("hello", 2)

- Signatures:

  - `LEFT(text, [num_chars])`

- Examples:

  - LEFT("hello", 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Negative count returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094079
