# LARGE

## LARGE

## Purpose
Returns the k-th largest value in dataset.

## Syntax
- Excel: `LARGE(array, k)`
- Google Sheets: `LARGE(array, k)`

## Behavior
- Sorts values deterministically and returns k-th index from high end.

## Examples (expected outputs)
- `LARGE({1,2,3},2) -> 2`

## Error Cases
- Invalid k or insufficient entries returns error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_large`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/large-function-3af0af19-1190-42bb-bb8b-01672ec00a64

- Source fetch status: failed after 4 attempts

- Summary: LARGE({1,2,3},2)

- Signatures:

  - `LARGE(array, k)`

- Examples:

  - LARGE({1,2,3},2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid k or insufficient entries returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094008

- Source fetch status: failed after 4 attempts

- Summary: LARGE({1,2,3},2)

- Signatures:

  - `LARGE(array, k)`

- Examples:

  - LARGE({1,2,3},2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid k or insufficient entries returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/large-function-3af0af19-1190-42bb-bb8b-01672ec00a64
- Google Sheets: https://support.google.com/docs/answer/3094008
