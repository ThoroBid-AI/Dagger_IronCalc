# ASC

## ASC

## Purpose
Converts full-width (double-byte) text to half-width (single-byte) forms.

## Syntax
- Excel: `ASC(text)`
- Google Sheets: `ASC(text)`

## Behavior
- Transforms full-width alphanumeric and punctuation into ASCII-compatible forms.
- Leaves non-applicable characters unchanged.

## Examples (expected outputs)
- `ASC("ＡＢＣ")` -> `ABC`

## Error Cases
- Returns error for malformed UTF-8-like input sequences.

## Notes
Not implemented in IronCalc. Planned Unicode normalization utility.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/asc-function-0b6abf1c-c663-4004-a964-ebc00b723266

- Source fetch status: failed after 4 attempts

- Summary: Converts full-width (double-byte) text to half-width (single-byte) forms.

- Signatures:

  - `ASC(text)`

- Examples:

  - ASC("ＡＢＣ")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns error for malformed UTF-8-like input sequences.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061514

- Source fetch status: failed after 4 attempts

- Summary: Converts full-width (double-byte) text to half-width (single-byte) forms.

- Signatures:

  - `ASC(text)`

- Examples:

  - ASC("ＡＢＣ")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns error for malformed UTF-8-like input sequences.



## Sources
- Excel: https://support.microsoft.com/en-us/office/asc-function-0b6abf1c-c663-4004-a964-ebc00b723266
- Google Sheets: https://support.google.com/docs/answer/9061514
