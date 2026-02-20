# BINOM.INV

## BINOM.INV

## Purpose
Returns smallest integer satisfying cumulative binomial probability.

## Syntax
- Excel: `BINOM.INV(number, trials, probability_s)`
- Google Sheets: `BINOM.INV(number, trials, probability_s)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `BINOM.INV(0.5, 10, 0.5)` -> `5`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_binom_inv`
- File: `base/src/functions/statistical/binom.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/binom-inv-function-80a0370c-ada6-49b4-83e7-05a91ba77ac9

- Source fetch status: failed after 4 attempts

- Summary: Returns smallest integer satisfying cumulative binomial probability.

- Signatures:

  - `BINOM.INV(number, trials, probability_s)`

- Examples:

  - BINOM.INV(0.5, 10, 0.5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093623

- Source fetch status: failed after 4 attempts

- Summary: Returns smallest integer satisfying cumulative binomial probability.

- Signatures:

  - `BINOM.INV(number, trials, probability_s)`

- Examples:

  - BINOM.INV(0.5, 10, 0.5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/binom-inv-function-80a0370c-ada6-49b4-83e7-05a91ba77ac9
- Google Sheets: https://support.google.com/docs/answer/3093623
