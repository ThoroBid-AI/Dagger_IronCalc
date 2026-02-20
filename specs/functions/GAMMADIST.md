# GAMMADIST

## GAMMADIST

## Purpose
Legacy alias for Gamma distribution cumulative/density behavior.

## Syntax
- Excel: `GAMMADIST(x, alpha, beta, cumulative)`
- Google Sheets: `GAMMADIST(x, alpha, beta, cumulative)`

## Behavior
- Compatibility wrapper with the same semantics as modern GAMMA.DIST form.

## Examples (expected outputs)
- `GAMMADIST(2, 2, 1, FALSE) -> 0.3679`

## Error Cases
- Invalid shape/scale or x values return errors.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_gamma_dist`
- File: `base/src/functions/statistical/gamma.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/gammadist-function-7327c94d-0f05-4511-83df-1dd7ed23e19e

- Source fetch status: failed after 4 attempts

- Summary: Legacy alias for Gamma distribution cumulative/density behavior.

- Signatures:

  - `GAMMADIST(x, alpha, beta, cumulative)`

- Examples:

  - GAMMADIST(2, 2, 1, FALSE)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid shape/scale or x values return errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7013989

- Source fetch status: failed after 4 attempts

- Summary: Legacy alias for Gamma distribution cumulative/density behavior.

- Signatures:

  - `GAMMADIST(x, alpha, beta, cumulative)`

- Examples:

  - GAMMADIST(2, 2, 1, FALSE)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid shape/scale or x values return errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/gammadist-function-7327c94d-0f05-4511-83df-1dd7ed23e19e
- Google Sheets: https://support.google.com/docs/answer/7013989
