# LEN

## LEN

## Purpose
Returns character count of text.

## Syntax
- Excel: `LEN(text)`
- Google Sheets: `LEN(text)`

## Behavior
- Counts characters after deterministic normalization.

## Examples (expected outputs)
- `LEN("hello") -> 5`

## Error Cases
- Non-text values are coerced by host rules or return 0 depending on context.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_len`
- File: `base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns character count of text.

- Signatures:

  - `LEN(text)`

- Examples:

  - LEN("hello")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values are coerced by host rules or return 0 depending on context.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094081

- Source fetch status: failed after 4 attempts

- Summary: Returns character count of text.

- Signatures:

  - `LEN(text)`

- Examples:

  - LEN("hello")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values are coerced by host rules or return 0 depending on context.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094081
