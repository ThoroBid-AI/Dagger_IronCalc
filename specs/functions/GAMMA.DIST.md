# GAMMA.DIST

## GAMMA.DIST

## Purpose
Returns gamma distribution cumulative or density values.

## Syntax
- Excel: `GAMMA.DIST(x, alpha, beta, cumulative)`
- Google Sheets: `GAMMA.DIST(x, alpha, beta, cumulative)`

## Behavior
- Returns CDF when cumulative=TRUE, otherwise PDF.

## Examples (expected outputs)
- `GAMMA.DIST(2, 2, 1, FALSE) -> 0.3679`

## Error Cases
- Alpha/beta must be positive; out-of-domain probability returns error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/gamma.rs`
- Proposed handler: `fn_gamma_dist`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/gamma-dist-function-9b6f1538-d11c-4d5f-8966-21f6a2201def

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `GAMMA.DIST(x, alpha, beta, cumulative)`

- Examples:

  - GAMMA.DIST(2, 2, 1, FALSE)

- Notes: Not implemented in IronCalc.

- Error behavior: Alpha/beta must be positive; out-of-domain probability returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7013989

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `GAMMA.DIST(x, alpha, beta, cumulative)`

- Examples:

  - GAMMA.DIST(2, 2, 1, FALSE)

- Notes: Not implemented in IronCalc.

- Error behavior: Alpha/beta must be positive; out-of-domain probability returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/gamma-dist-function-9b6f1538-d11c-4d5f-8966-21f6a2201def
- Google Sheets: https://support.google.com/docs/answer/7013989
