# CRITBINOM

## CRITBINOM

## Purpose
Returns threshold value for binomial distribution by cumulative probability.

## Syntax
- Excel: `CRITBINOM(number_s, trials, probability_s)`
- Google Sheets: `CRITBINOM(number_s, trials, probability_s)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CRITBINOM(0.75, 10, 0.5) -> 6`

## Error Cases
- If probability outside 0-1, returns error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/critbinom-function-eb6b871d-796b-4d21-b69b-e4350d5f407b

- Source fetch status: failed after 4 attempts

- Summary: Returns threshold value for binomial distribution by cumulative probability.

- Signatures:

  - `CRITBINOM(number_s, trials, probability_s)`

- Examples:

  - CRITBINOM(0.75, 10, 0.5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: If probability outside 0-1, returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093623

- Source fetch status: failed after 4 attempts

- Summary: Returns threshold value for binomial distribution by cumulative probability.

- Signatures:

  - `CRITBINOM(number_s, trials, probability_s)`

- Examples:

  - CRITBINOM(0.75, 10, 0.5)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: If probability outside 0-1, returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/critbinom-function-eb6b871d-796b-4d21-b69b-e4350d5f407b
- Google Sheets: https://support.google.com/docs/answer/3093623
