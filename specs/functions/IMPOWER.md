# IMPOWER

## IMPOWER

## Purpose
Raises a complex number to a complex power.

## Syntax
- Excel: `IMPOWER(inumber, number)`
- Google Sheets: `IMPOWER(inumber, number)`

## Behavior
- Computes principal complex power with deterministic branch handling.

## Examples (expected outputs)
- `IMPOWER("1+i", 2) -> 0+2i`

## Error Cases
Invalid exponentiation for poles or malformed inputs returns error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_impower`
- File: `base/src/functions/engineering/complex.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_impower`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/impower-function-210fd2f5-f8ff-4c6a-9d60-30e34fbdef39

- Source fetch status: failed after 4 attempts

- Summary: Raises a complex number to a complex power.

- Signatures:

  - `IMPOWER(inumber, number)`

- Examples:

  - IMPOWER("1+i", 2)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9003065

- Source fetch status: failed after 4 attempts

- Summary: Raises a complex number to a complex power.

- Signatures:

  - `IMPOWER(inumber, number)`

- Examples:

  - IMPOWER("1+i", 2)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/impower-function-210fd2f5-f8ff-4c6a-9d60-30e34fbdef39
- Google Sheets: https://support.google.com/docs/answer/9003065
