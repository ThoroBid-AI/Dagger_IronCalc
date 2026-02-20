# MAXIFS

## MAXIFS

## Purpose
Returns max with criteria conditions.

## Syntax
- Excel: `MAXIFS(max_range, criteria_range1, criteria1, ...)`
- Google Sheets: `MAXIFS(max_range, criteria_range1, criteria1, ...)`

## Behavior
- Filters then returns highest match.

## Examples (expected outputs)
- `MAXIFS({1,2,3},{1,2,3},{">1"}) -> 2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_maxifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MAXIFS(max_range, criteria_range1, criteria1, ...)`

- Examples:

  - MAXIFS({1,2,3},{1,2,3},{">1"})

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7013817

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MAXIFS(max_range, criteria_range1, criteria1, ...)`

- Examples:

  - MAXIFS({1,2,3},{1,2,3},{">1"})

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883
- Google Sheets: https://support.google.com/docs/answer/7013817
