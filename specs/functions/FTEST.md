# FTEST

## FTEST

## Purpose
Performs two-variable F-test variance comparison.

## Syntax
- Excel: `FTEST(array1, array2)`
- Google Sheets: `FTEST(array1, array2)`

## Behavior
- Calculates significance probability for variance ratio between two samples.

## Examples (expected outputs)
- `FTEST({1,2,3}, {4,5,6}) -> 0.74`

## Error Cases
- Too few values or invalid numeric input returns error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_f_test`
- File: `base/src/functions/statistical/fisher.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ftest-function-4c9e1202-53fe-428c-a737-976f6fc3f9fd

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FTEST(array1, array2)`

- Examples:

  - FTEST({1,2,3}, {4,5,6})

- Notes: Implemented in IronCalc.

- Error behavior: Too few values or invalid numeric input returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7004183

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FTEST(array1, array2)`

- Examples:

  - FTEST({1,2,3}, {4,5,6})

- Notes: Implemented in IronCalc.

- Error behavior: Too few values or invalid numeric input returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ftest-function-4c9e1202-53fe-428c-a737-976f6fc3f9fd
- Google Sheets: https://support.google.com/docs/answer/7004183
