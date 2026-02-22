# CHISQ.DIST.RT

## CHISQ.DIST.RT

## Purpose
Returns right-tail probability of chi-square.

## Syntax
- Excel: `CHISQ.DIST.RT(x, degrees_freedom)`
- Google Sheets: `CHISQ.DIST.RT(x, degrees_freedom)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CHISQ.DIST.RT(1, 2)` -> `0.6065...`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_chisq_dist_rt`
- File: `base/src/functions/statistical/chisq.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/chisq-dist-rt-function-dc4832e8-ed2b-49ae-8d7c-b28d5804c0f2

- Source fetch status: failed after 4 attempts

- Summary: Returns right-tail probability of chi-square.

- Signatures:

  - `CHISQ.DIST.RT(x, degrees_freedom)`

- Examples:

  - CHISQ.DIST.RT(1, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7003199

- Source fetch status: failed after 4 attempts

- Summary: Returns right-tail probability of chi-square.

- Signatures:

  - `CHISQ.DIST.RT(x, degrees_freedom)`

- Examples:

  - CHISQ.DIST.RT(1, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/chisq-dist-rt-function-dc4832e8-ed2b-49ae-8d7c-b28d5804c0f2
- Google Sheets: https://support.google.com/docs/answer/7003199
