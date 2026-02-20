# SIGN
## SIGN
## Purpose
Returns the sign of a numeric value: 1 if positive, 0 if zero, and -1 if negative.
## Syntax
- Excel: `SIGN(number)`
- Google Sheets: `SIGN(number)`
## Behavior
SIGN is deterministic and only depends on numeric coercion of number. Empty cells resolve through normal engine coercion rules; if a coercion path is not defined, return an error.
## Examples (expected outputs)
- `=SIGN(-7)` -> `-1`
- `=SIGN(0)` -> `0`
- `=SIGN(7)` -> `1`
## Error Cases
- `SIGN("text")` -> `#VALUE!`
- Extra or missing arguments -> `#VALUE!`
## Notes
Single-argument utility function used in branching and normalization logic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sign`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sign-function-109c932d-fcdc-4023-91f1-2dd0e916a1d8

- Source fetch status: failed after 4 attempts

- Summary: Returns the sign of a numeric value: 1 if positive, 0 if zero, and -1 if negative.

- Signatures:

  - `SIGN(number)`

- Examples:

  - SIGN(-7)

  - SIGN(0)

  - SIGN(7)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: `SIGN("text")` -> `#VALUE!`



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093513

- Source fetch status: failed after 4 attempts

- Summary: Returns the sign of a numeric value: 1 if positive, 0 if zero, and -1 if negative.

- Signatures:

  - `SIGN(number)`

- Examples:

  - SIGN(-7)

  - SIGN(0)

  - SIGN(7)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: `SIGN("text")` -> `#VALUE!`



## Sources
- Excel: https://support.microsoft.com/en-us/office/sign-function-109c932d-fcdc-4023-91f1-2dd0e916a1d8
- Google Sheets: https://support.google.com/docs/answer/3093513
