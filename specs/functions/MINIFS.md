# MINIFS

## MINIFS

## Purpose
Returns min with criteria conditions.

## Syntax
- Excel: `MINIFS(min_range, criteria_range1, criteria1, ...)`
- Google Sheets: `MINIFS(min_range, criteria_range1, criteria1, ...)`

## Behavior
- Filters then returns lowest match.

## Examples (expected outputs)
- `MINIFS({1,2,3},{1,2,3},{">1"}) -> 2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_minifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599

- Source fetch status: failed after 4 attempts

- Summary: Returns min with criteria conditions.

- Signatures:

  - `MINIFS(min_range, criteria_range1, criteria1, ...)`

- Examples:

  - MINIFS({1,2,3},{1,2,3},{">1"})

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7014063

- Source fetch status: failed after 4 attempts

- Summary: Returns min with criteria conditions.

- Signatures:

  - `MINIFS(min_range, criteria_range1, criteria1, ...)`

- Examples:

  - MINIFS({1,2,3},{1,2,3},{">1"})

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599
- Google Sheets: https://support.google.com/docs/answer/7014063
