# CLEAN

## CLEAN

## Purpose
Removes non-printable characters from text.

## Syntax
- Excel: `CLEAN(text)`
- Google Sheets: `CLEAN(text)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CLEAN("a
")` -> `a`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

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



- Source URL: https://support.microsoft.com/en-us/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41

- Source fetch status: failed after 4 attempts

- Summary: Removes non-printable characters from text.

- Signatures:

  - `CLEAN(text)`

- Examples:

  - CLEAN("a ")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267340

- Source fetch status: failed after 4 attempts

- Summary: Removes non-printable characters from text.

- Signatures:

  - `CLEAN(text)`

- Examples:

  - CLEAN("a ")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41
- Google Sheets: https://support.google.com/docs/answer/3267340
