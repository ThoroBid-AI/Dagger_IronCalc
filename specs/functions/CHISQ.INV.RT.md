# CHISQ.INV.RT

## CHISQ.INV.RT

## Purpose
Returns inverse right-tail chi-square value.

## Syntax
- Excel: `CHISQ.INV.RT(probability, degrees_freedom)`
- Google Sheets: `CHISQ.INV.RT(probability, degrees_freedom)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CHISQ.INV.RT(0.05, 2)` -> numeric

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_chisq_inv_rt`
- File: `base/src/functions/statistical/chisq.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/chisq-inv-rt-function-435b5ed8-98d5-4da6-823f-293e2cbc94fe

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse right-tail chi-square value.

- Signatures:

  - `CHISQ.INV.RT(probability, degrees_freedom)`

- Examples:

  - CHISQ.INV.RT(0.05, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7003348

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse right-tail chi-square value.

- Signatures:

  - `CHISQ.INV.RT(probability, degrees_freedom)`

- Examples:

  - CHISQ.INV.RT(0.05, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/chisq-inv-rt-function-435b5ed8-98d5-4da6-823f-293e2cbc94fe
- Google Sheets: https://support.google.com/docs/answer/7003348
