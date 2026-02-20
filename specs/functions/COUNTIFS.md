# COUNTIFS

## COUNTIFS

## Purpose
Counts cells that meet multiple criteria.

## Syntax
- Excel: `COUNTIFS(criteria_range1, criteria1, ...)`
- Google Sheets: `COUNTIFS(criteria_range1, criteria1, ...)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUNTIFS({1,2,3},{">1"}, {"A","B","A"}) -> 0`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_countifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNTIFS(criteria_range1, criteria1, ...)`

- Examples:

  - COUNTIFS({1,2,3},{">1"}, {"A","B","A"})

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3256550

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNTIFS(criteria_range1, criteria1, ...)`

- Examples:

  - COUNTIFS({1,2,3},{">1"}, {"A","B","A"})

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842
- Google Sheets: https://support.google.com/docs/answer/3256550
