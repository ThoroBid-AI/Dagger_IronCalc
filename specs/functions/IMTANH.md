# IMTANH

## IMTANH

## Purpose
Returns hyperbolic tangent of a complex number.

## Syntax
- Excel: `IMTANH(inumber)`
- Google Sheets: `IMTANH(inumber)`

## Behavior
- Computes tanh in complex domain deterministically.

## Examples (expected outputs)
- `IMTANH("1") -> 0.7616`

## Error Cases
- Invalid input returns error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_imtanh`
- Proposed file: `base/src/functions/engineering/complex.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: IMTANH("1")

- Signatures:

  - `IMTANH(inumber)`

- Examples:

  - IMTANH("1")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid input returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9366655

- Source fetch status: failed after 4 attempts

- Summary: IMTANH("1")

- Signatures:

  - `IMTANH(inumber)`

- Examples:

  - IMTANH("1")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid input returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9366655
