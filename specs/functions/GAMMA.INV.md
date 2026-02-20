# GAMMA.INV

## GAMMA.INV

## Purpose
Returns inverse gamma distribution quantile.

## Syntax
- Excel: `GAMMA.INV(probability, alpha, beta)`
- Google Sheets: `GAMMA.INV(probability, alpha, beta)`

## Behavior
- Inverts GAMMA.DIST with deterministic numeric solving behavior.

## Examples (expected outputs)
- `GAMMA.INV(0.5, 2, 1) -> 1.678`

## Error Cases
- Probability outside 0-1 returns error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/gamma.rs`
- Proposed handler: `fn_gamma_inv`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/gammainv-function-06393558-37ab-47d0-aa63-432f99e7916d

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `GAMMA.INV(probability, alpha, beta)`

- Examples:

  - GAMMA.INV(0.5, 2, 1)

- Notes: Not implemented in IronCalc.

- Error behavior: Probability outside 0-1 returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116467

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `GAMMA.INV(probability, alpha, beta)`

- Examples:

  - GAMMA.INV(0.5, 2, 1)

- Notes: Not implemented in IronCalc.

- Error behavior: Probability outside 0-1 returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/gammainv-function-06393558-37ab-47d0-aa63-432f99e7916d
- Google Sheets: https://support.google.com/docs/answer/9116467
