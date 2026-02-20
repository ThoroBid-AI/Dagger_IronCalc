# GAMMAINV

## GAMMAINV

## Purpose
Returns inverse of gamma cumulative distribution.

## Syntax
- Excel: `GAMMAINV(probability, alpha, beta)`
- Google Sheets: `GAMMAINV(probability, alpha, beta)`

## Behavior
- Computes x such that GAMMA.DIST(x, alpha, beta, TRUE)=probability.

## Examples (expected outputs)
- `GAMMAINV(0.5, 2, 1) -> 1.678`

## Error Cases
- Probability outside [0,1] returns error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_gamma_inv`
- File: `base/src/functions/statistical/gamma.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/gammainv-function-06393558-37ab-47d0-aa63-432f99e7916d

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of gamma cumulative distribution.

- Signatures:

  - `GAMMAINV(probability, alpha, beta)`

- Examples:

  - GAMMAINV(0.5, 2, 1)

- Notes: Implemented in IronCalc.

- Error behavior: Probability outside [0,1] returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116467

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of gamma cumulative distribution.

- Signatures:

  - `GAMMAINV(probability, alpha, beta)`

- Examples:

  - GAMMAINV(0.5, 2, 1)

- Notes: Implemented in IronCalc.

- Error behavior: Probability outside [0,1] returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/gammainv-function-06393558-37ab-47d0-aa63-432f99e7916d
- Google Sheets: https://support.google.com/docs/answer/9116467
