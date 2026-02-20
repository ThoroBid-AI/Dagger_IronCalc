# IMCOTH

## IMCOTH

## Purpose
Returns hyperbolic cotangent of a complex number.

## Syntax
- Excel: `IMCOTH(inumber)`
- Google Sheets: `IMCOTH(inumber)`

## Behavior
- Returns hyperbolic cotangent with deterministic complex handling.

## Examples (expected outputs)
- `IMCOTH("1") -> 1.313035285`

## Error Cases
Zero denominator or invalid format returns error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/engineering/complex.rs`
- Proposed handler: `fn_imcoth`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_imcoth`
- Proposed file: `base/src/functions/engineering/complex.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns hyperbolic cotangent of a complex number.

- Signatures:

  - `IMCOTH(inumber)`

- Examples:

  - IMCOTH("1")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9366256

- Source fetch status: failed after 4 attempts

- Summary: Returns hyperbolic cotangent of a complex number.

- Signatures:

  - `IMCOTH(inumber)`

- Examples:

  - IMCOTH("1")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9366256
