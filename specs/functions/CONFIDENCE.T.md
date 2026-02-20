# CONFIDENCE.T

## CONFIDENCE.T

## Purpose
Returns confidence interval half-width for t distribution.

## Syntax
- Excel: `CONFIDENCE.T(alpha, standard_dev, size)`
- Google Sheets: `CONFIDENCE.T(alpha, standard_dev, size)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CONFIDENCE.T(0.05, 1.2, 10)` -> numeric

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_confidence_t`
- File: `base/src/functions/statistical/normal.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/confidence-t-function-e8eca395-6c3a-4ba9-9003-79ccc61d3c53

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CONFIDENCE.T(alpha, standard_dev, size)`

- Examples:

  - CONFIDENCE.T(0.05, 1.2, 10)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9365672

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CONFIDENCE.T(alpha, standard_dev, size)`

- Examples:

  - CONFIDENCE.T(0.05, 1.2, 10)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/confidence-t-function-e8eca395-6c3a-4ba9-9003-79ccc61d3c53
- Google Sheets: https://support.google.com/docs/answer/9365672
