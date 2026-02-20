# COUNTA

## COUNTA

## Purpose
Returns count of non-empty values in references.

## Syntax
- Excel: `COUNTA(value1, [value2], ...)`
- Google Sheets: `COUNTA(value1, [value2], ...)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUNTA(1, "x", FALSE, "") -> 3`

## Error Cases
- Empty argument list returns 0.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_counta`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNTA(value1, [value2], ...)`

- Examples:

  - COUNTA(1, "x", FALSE, "")

- Notes: See source link when network access is restored.

- Error behavior: Empty argument list returns 0.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093991

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNTA(value1, [value2], ...)`

- Examples:

  - COUNTA(1, "x", FALSE, "")

- Notes: See source link when network access is restored.

- Error behavior: Empty argument list returns 0.



## Sources
- Excel: https://support.microsoft.com/en-us/office/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509
- Google Sheets: https://support.google.com/docs/answer/3093991
