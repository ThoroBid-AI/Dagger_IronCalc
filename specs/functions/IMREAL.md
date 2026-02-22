# IMREAL

## IMREAL

## Purpose
Returns the real coefficient of a complex number.

## Syntax
- Excel: `IMREAL(inumber)`
- Google Sheets: `IMREAL(inumber)`

## Behavior
- Parses and returns numeric real part.

## Examples (expected outputs)
- `IMREAL("3+4i") -> 3`

## Error Cases
Malformed complex input returns #VALUE!-style error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_imreal`
- File: `base/src/functions/engineering/complex.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_imreal`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/imreal-function-d12bc4c0-25d0-4bb3-a25f-ece1938bf366

- Source fetch status: failed after 4 attempts

- Summary: Returns the real coefficient of a complex number.

- Signatures:

  - `IMREAL(inumber)`

- Examples:

  - IMREAL("3+4i")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7408138

- Source fetch status: failed after 4 attempts

- Summary: Returns the real coefficient of a complex number.

- Signatures:

  - `IMREAL(inumber)`

- Examples:

  - IMREAL("3+4i")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/imreal-function-d12bc4c0-25d0-4bb3-a25f-ece1938bf366
- Google Sheets: https://support.google.com/docs/answer/7408138
