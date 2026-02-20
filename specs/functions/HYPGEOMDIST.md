# HYPGEOMDIST

## HYPGEOMDIST

## Purpose
Legacy alias for the hypergeometric distribution.

## Syntax
- Excel: `HYPGEOMDIST(sample_s, number_sample, number_pop, population_s)`
- Google Sheets: `HYPGEOMDIST(sample_s, number_sample, number_pop, population_s)`

## Behavior
- Legacy argument order mapped to equivalent HYPGEOM.DIST cumulative behavior.

## Examples (expected outputs)
- `HYPGEOMDIST(2, 3, 10, 5) -> 0.238`

## Error Cases
Invalid range values and inconsistent parameters return domain errors.

## Notes
- Implemented in IronCalc.
- Handler: `fn_hyp_geom_dist`
- File: `base/src/functions/statistical/hypegeom.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_hyp_geom_dist`
- File: `base/src/functions/statistical/hypegeom.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hypgeomdist-function-23e37961-2871-4195-9629-d0b2c108a12e

- Source fetch status: not captured in this snapshot

- Summary: Legacy alias for the hypergeometric distribution.

- Signatures:

  - `HYPGEOMDIST(sample_s, number_sample, number_pop, population_s)`

- Examples:

  - HYPGEOMDIST(2, 3, 10, 5)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094004

- Source fetch status: not captured in this snapshot

- Summary: Legacy alias for the hypergeometric distribution.

- Signatures:

  - `HYPGEOMDIST(sample_s, number_sample, number_pop, population_s)`

- Examples:

  - HYPGEOMDIST(2, 3, 10, 5)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hypgeomdist-function-23e37961-2871-4195-9629-d0b2c108a12e
- Google Sheets: https://support.google.com/docs/answer/3094004
