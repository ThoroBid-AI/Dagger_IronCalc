# COUNTBLANK

## COUNTBLANK

## Purpose
Returns count of empty cells in a range.

## Syntax
- Excel: `COUNTBLANK(range)`
- Google Sheets: `COUNTBLANK(range)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUNTBLANK({"A",, "", "B"}) -> 2`

## Error Cases
- Non-range inputs may return argument error in strict mode.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_countblank`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNTBLANK(range)`

- Examples:

  - COUNTBLANK({"A",, "", "B"})

- Notes: See source link when network access is restored.

- Error behavior: Non-range inputs may return argument error in strict mode.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093403

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNTBLANK(range)`

- Examples:

  - COUNTBLANK({"A",, "", "B"})

- Notes: See source link when network access is restored.

- Error behavior: Non-range inputs may return argument error in strict mode.



## Sources
- Excel: https://support.microsoft.com/en-us/office/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22
- Google Sheets: https://support.google.com/docs/answer/3093403
