# CODE

## CODE

## Purpose
Returns numeric code for the first character in text.

## Syntax
- Excel: `CODE(text)`
- Google Sheets: `CODE(text)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CODE("A")` -> `65`

## Error Cases
- Empty input or invalid UTF sequence returns an error.

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



- Source URL: https://support.microsoft.com/en-us/office/code-function-c32b692b-2ed0-4a04-bdd9-75640144b928

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CODE(text)`

- Examples:

  - CODE("A")

- Notes: See source link when network access is restored.

- Error behavior: Empty input or invalid UTF sequence returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094122

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CODE(text)`

- Examples:

  - CODE("A")

- Notes: See source link when network access is restored.

- Error behavior: Empty input or invalid UTF sequence returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/code-function-c32b692b-2ed0-4a04-bdd9-75640144b928
- Google Sheets: https://support.google.com/docs/answer/3094122
