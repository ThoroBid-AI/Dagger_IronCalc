# BINOM.DIST.RANGE

## BINOM.DIST.RANGE

## Purpose
Returns probability for a range of successes in a binomial experiment.

## Syntax
- Excel: `BINOM.DIST.RANGE(trials, prob_s, number_s, number_s2)`
- Google Sheets: `BINOM.DIST.RANGE(trials, probability_s, successes, [successes2])`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `BINOM.DIST.RANGE(10, 0.5, 3, 5)` -> `0.5`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_binom_dist_range`
- File: `base/src/functions/statistical/binom.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/binom-dist-range-function-17331329-74c7-4053-bb4c-6653a7421595

- Source fetch status: failed after 4 attempts

- Summary: Returns probability for a range of successes in a binomial experiment.

- Signatures:

  - `BINOM.DIST.RANGE(trials, prob_s, number_s, number_s2)`

- Examples:

  - BINOM.DIST.RANGE(10, 0.5, 3, 5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=BINOM.DIST.RANGE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/binom-dist-range-function-17331329-74c7-4053-bb4c-6653a7421595
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=BINOM.DIST.RANGE
