# F.TEST

## F.TEST

## Purpose
Returns right-tailed F-test probability for two variances.

## Syntax
- Excel: `F.TEST(array1, array2)`
- Google Sheets: `F.TEST(array1, array2)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `F.TEST({1,2,3},{4,5,6}) -> 0.12`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `compute F statistic and lookup right-tail significance`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ftest-function-4c9e1202-53fe-428c-a737-976f6fc3f9fd

- Source fetch status: failed after 4 attempts

- Summary: Returns right-tailed F-test probability for two variances.

- Signatures:

  - `F.TEST(array1, array2)`

- Examples:

  - F.TEST({1,2,3},{4,5,6})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7004183

- Source fetch status: failed after 4 attempts

- Summary: Returns right-tailed F-test probability for two variances.

- Signatures:

  - `F.TEST(array1, array2)`

- Examples:

  - F.TEST({1,2,3},{4,5,6})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ftest-function-4c9e1202-53fe-428c-a737-976f6fc3f9fd
- Google Sheets: https://support.google.com/docs/answer/7004183
