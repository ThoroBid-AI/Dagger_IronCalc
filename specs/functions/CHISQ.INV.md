# CHISQ.INV

## CHISQ.INV

## Purpose
Returns inverse chi-square for a given probability.

## Syntax
- Excel: `CHISQ.INV(probability, degrees_freedom)`
- Google Sheets: `CHISQ.INV(probability, degrees_freedom)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CHISQ.INV(0.95, 2)` -> numeric

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_chisq_inv`
- File: `base/src/functions/statistical/chisq.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/chisq-inv-function-400db556-62b3-472d-80b3-254723e7092f

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse chi-square for a given probability.

- Signatures:

  - `CHISQ.INV(probability, degrees_freedom)`

- Examples:

  - CHISQ.INV(0.95, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7004181

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse chi-square for a given probability.

- Signatures:

  - `CHISQ.INV(probability, degrees_freedom)`

- Examples:

  - CHISQ.INV(0.95, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/chisq-inv-function-400db556-62b3-472d-80b3-254723e7092f
- Google Sheets: https://support.google.com/docs/answer/7004181
