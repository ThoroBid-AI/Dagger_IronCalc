# HYPGEOM.DIST

## HYPGEOM.DIST

## Purpose
Returns the hypergeometric distribution probability.

## Syntax
- Excel: `HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)`
- Google Sheets: `HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)`

## Behavior
- Computes PMF or CDF based on cumulative flag.

## Examples (expected outputs)
- `HYPGEOM.DIST(2, 3, 5, 10, FALSE) -> 0.238`

## Error Cases
Invalid draw/sample ranges return a domain error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/statistical/hypegeom.rs`
- Proposed handler: `fn_hypgeom_dist`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_hypgeom_dist`
- Proposed file: `base/src/functions/statistical/hypegeom.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hypgeomdist-function-23e37961-2871-4195-9629-d0b2c108a12e

- Source fetch status: failed after 4 attempts

- Summary: Returns the hypergeometric distribution probability.

- Signatures:

  - `HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)`

- Examples:

  - HYPGEOM.DIST(2, 3, 5, 10, FALSE)

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094004

- Source fetch status: failed after 4 attempts

- Summary: Returns the hypergeometric distribution probability.

- Signatures:

  - `HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)`

- Examples:

  - HYPGEOM.DIST(2, 3, 5, 10, FALSE)

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hypgeomdist-function-23e37961-2871-4195-9629-d0b2c108a12e
- Google Sheets: https://support.google.com/docs/answer/3094004
