# CHAR

## CHAR

## Purpose
Returns the character represented by a numeric code point.

## Syntax
- Excel: `CHAR(number)`
- Google Sheets: `CHAR(number)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CHAR(65)` -> `A`

## Error Cases
- Invalid numeric input outside supported codepoint range returns an error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Parse function arity and normalize inputs.
- Reuse shared parser and numeric helpers where available.
- Implement domain checks and deterministic output formatting.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a

- Source fetch status: failed after 4 attempts

- Summary: Returns the character represented by a numeric code point.

- Signatures:

  - `CHAR(number)`

- Examples:

  - CHAR(65)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid numeric input outside supported codepoint range returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094120

- Source fetch status: failed after 4 attempts

- Summary: Returns the character represented by a numeric code point.

- Signatures:

  - `CHAR(number)`

- Examples:

  - CHAR(65)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid numeric input outside supported codepoint range returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a
- Google Sheets: https://support.google.com/docs/answer/3094120
