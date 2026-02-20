# GAMMALN.PRECISE

## GAMMALN.PRECISE

## Purpose
Returns the natural logarithm of Gamma with precision emphasis.

## Syntax
- Excel: `GAMMALN.PRECISE(x)`
- Google Sheets: `GAMMALN.PRECISE(x)`

## Behavior
- Precision-oriented variant of GAMMALN with stricter numeric pathway.

## Examples (expected outputs)
- `GAMMALN.PRECISE(5) -> 3.178053830`

## Error Cases
- Domain invalid for non-positive x.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/gamma.rs`
- Proposed handler: `fn_gammaln_precise`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/gammaln-precise-function-5cdfe601-4e1e-4189-9d74-241ef1caa599

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `GAMMALN.PRECISE(x)`

- Examples:

  - GAMMALN.PRECISE(5)

- Notes: Not implemented in IronCalc.

- Error behavior: Domain invalid for non-positive x.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093416

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `GAMMALN.PRECISE(x)`

- Examples:

  - GAMMALN.PRECISE(5)

- Notes: Not implemented in IronCalc.

- Error behavior: Domain invalid for non-positive x.



## Sources
- Excel: https://support.microsoft.com/en-us/office/gammaln-precise-function-5cdfe601-4e1e-4189-9d74-241ef1caa599
- Google Sheets: https://support.google.com/docs/answer/3093416
