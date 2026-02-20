# IMDIV

## IMDIV

## Purpose
Divides two complex numbers.

## Syntax
- Excel: `IMDIV(inumber1, inumber2)`
- Google Sheets: `IMDIV(inumber1, inumber2)`

## Behavior
- Performs complex division with deterministic normalization.

## Examples (expected outputs)
- `IMDIV("4+2i", "1+i") -> 3`

## Error Cases
Division by zero or malformed complex numbers returns error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_imdiv`
- File: `base/src/functions/engineering/complex.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_imdiv`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/imdiv-function-a505aff7-af8a-4451-8142-77ec3d74d83f

- Source fetch status: failed after 4 attempts

- Summary: Divides two complex numbers.

- Signatures:

  - `IMDIV(inumber1, inumber2)`

- Examples:

  - IMDIV("4+2i", "1+i")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7411898

- Source fetch status: failed after 4 attempts

- Summary: Divides two complex numbers.

- Signatures:

  - `IMDIV(inumber1, inumber2)`

- Examples:

  - IMDIV("4+2i", "1+i")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/imdiv-function-a505aff7-af8a-4451-8142-77ec3d74d83f
- Google Sheets: https://support.google.com/docs/answer/7411898
