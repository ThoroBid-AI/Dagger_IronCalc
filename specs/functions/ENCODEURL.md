# ENCODEURL

## ENCODEURL

## Purpose
Percent-encodes a text string for safe URL use.

## Syntax
- Excel: `ENCODEURL(url)`
- Google Sheets: `ENCODEURL(url)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `ENCODEURL("A B") -> "A%20B"`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  1. `percent-encode characters outside RFC3986 unreserved set`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/encodeurl-function-07c7fb90-7c60-4bff-8687-fac50fe33d0e

- Source fetch status: failed after 4 attempts

- Summary: Percent-encodes a text string for safe URL use.

- Signatures:

  - `ENCODEURL(url)`

- Examples:

  - ENCODEURL("A B")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9199778

- Source fetch status: failed after 4 attempts

- Summary: Percent-encodes a text string for safe URL use.

- Signatures:

  - `ENCODEURL(url)`

- Examples:

  - ENCODEURL("A B")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/encodeurl-function-07c7fb90-7c60-4bff-8687-fac50fe33d0e
- Google Sheets: https://support.google.com/docs/answer/9199778
