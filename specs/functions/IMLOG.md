# IMLOG

## IMLOG

## Purpose
Returns logarithm of a complex number with specified base.

## Syntax
- Excel: `IMLOG(inumber, [base])`
- Google Sheets: `IMLOG(inumber, [base])`

## Behavior
- Divides IMLN(inumber) by IMLN(base) when base is provided.

## Examples (expected outputs)
- `IMLOG("10", 10) -> 1`

## Error Cases
Invalid base (<=0, 1) or invalid complex input returns error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/engineering/complex.rs`
- Proposed handler: `fn_imlog`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_imlog`
- Proposed file: `base/src/functions/engineering/complex.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns logarithm of a complex number with specified base.

- Signatures:

  - `IMLOG(inumber, [base])`

- Examples:

  - IMLOG("10", 10)

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9366486

- Source fetch status: failed after 4 attempts

- Summary: Returns logarithm of a complex number with specified base.

- Signatures:

  - `IMLOG(inumber, [base])`

- Examples:

  - IMLOG("10", 10)

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9366486
