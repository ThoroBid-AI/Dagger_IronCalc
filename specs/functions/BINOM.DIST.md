# BINOM.DIST

## BINOM.DIST

## Purpose
Returns the binomial distribution.

## Syntax
- Excel: `BINOM.DIST(number, trials, probability_s, cumulative)`
- Google Sheets: `BINOM.DIST(number_s, trials, probability_s, cumulative)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `BINOM.DIST(1, 2, 0.5, FALSE)` -> `0.5`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_binom_dist`
- File: `base/src/functions/statistical/binom.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/binom-dist-function-c5ae37b6-f39c-4be2-94c2-509a1480770c

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BINOM.DIST(number, trials, probability_s, cumulative)`

- Examples:

  - BINOM.DIST(1, 2, 0.5, FALSE)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093987

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BINOM.DIST(number_s, trials, probability_s, cumulative)`

- Examples:

  - BINOM.DIST(1, 2, 0.5, FALSE)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/binom-dist-function-c5ae37b6-f39c-4be2-94c2-509a1480770c
- Google Sheets: https://support.google.com/docs/answer/3093987
