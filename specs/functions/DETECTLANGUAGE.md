# DETECTLANGUAGE

## DETECTLANGUAGE

## Purpose
Detects the probable language of text and returns a language code.

## Syntax
- Excel: `DETECTLANGUAGE(text)`
- Google Sheets: `DETECTLANGUAGE(text)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DETECTLANGUAGE("bonjour") -> "fr"`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  1. `determine language code from text and return locale identifier`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/detectlanguage-function-0748e285-1912-4d24-b735-57d18142fa3b

- Source fetch status: failed after 4 attempts

- Summary: Detects the probable language of text and returns a language code.

- Signatures:

  - `DETECTLANGUAGE(text)`

- Examples:

  - DETECTLANGUAGE("bonjour")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093278

- Source fetch status: failed after 4 attempts

- Summary: Detects the probable language of text and returns a language code.

- Signatures:

  - `DETECTLANGUAGE(text)`

- Examples:

  - DETECTLANGUAGE("bonjour")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/detectlanguage-function-0748e285-1912-4d24-b735-57d18142fa3b
- Google Sheets: https://support.google.com/docs/answer/3093278
