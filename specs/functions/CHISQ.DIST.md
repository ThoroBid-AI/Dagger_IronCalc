# CHISQ.DIST

## CHISQ.DIST

## Purpose
Returns the chi-square distribution value.

## Syntax
- Excel: `CHISQ.DIST(x, degrees_freedom, cumulative)`
- Google Sheets: `CHISQ.DIST(x, degrees_freedom, cumulative)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CHISQ.DIST(1, 2, TRUE)` -> `0.3935...`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_chisq_dist`
- File: `base/src/functions/statistical/chisq.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/chisq-dist-function-8486b05e-5c05-4942-a9ea-f6b341518732

- Source fetch status: failed after 4 attempts

- Summary: Returns the chi-square distribution value.

- Signatures:

  - `CHISQ.DIST(x, degrees_freedom, cumulative)`

- Examples:

  - CHISQ.DIST(1, 2, TRUE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7003347

- Source fetch status: failed after 4 attempts

- Summary: Returns the chi-square distribution value.

- Signatures:

  - `CHISQ.DIST(x, degrees_freedom, cumulative)`

- Examples:

  - CHISQ.DIST(1, 2, TRUE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/chisq-dist-function-8486b05e-5c05-4942-a9ea-f6b341518732
- Google Sheets: https://support.google.com/docs/answer/7003347
