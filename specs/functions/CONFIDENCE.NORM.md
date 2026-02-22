# CONFIDENCE.NORM

## CONFIDENCE.NORM

## Purpose
Returns confidence interval half-width for normal distribution.

## Syntax
- Excel: `CONFIDENCE.NORM(alpha, standard_dev, size)`
- Google Sheets: `CONFIDENCE.NORM(alpha, standard_dev, size)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CONFIDENCE.NORM(0.05, 1.2, 10)` -> numeric

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_confidence_norm`
- File: `base/src/functions/statistical/normal.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/confidence-norm-function-7cec58a6-85bb-488d-91c3-63828d4fbfd4

- Source fetch status: failed after 4 attempts

- Summary: Returns confidence interval half-width for normal distribution.

- Signatures:

  - `CONFIDENCE.NORM(alpha, standard_dev, size)`

- Examples:

  - CONFIDENCE.NORM(0.05, 1.2, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093988

- Source fetch status: failed after 4 attempts

- Summary: Returns confidence interval half-width for normal distribution.

- Signatures:

  - `CONFIDENCE.NORM(alpha, standard_dev, size)`

- Examples:

  - CONFIDENCE.NORM(0.05, 1.2, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/confidence-norm-function-7cec58a6-85bb-488d-91c3-63828d4fbfd4
- Google Sheets: https://support.google.com/docs/answer/3093988
