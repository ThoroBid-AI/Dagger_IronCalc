# CORREL

## CORREL

## Purpose
Returns Pearson correlation coefficient.

## Syntax
- Excel: `CORREL(array1, array2)`
- Google Sheets: `CORREL(array1, array2)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CORREL({1,2,3},{2,4,6})` -> `1`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_correl`
- File: `base/src/functions/statistical/correl.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/correl-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92

- Source fetch status: failed after 4 attempts

- Summary: Returns Pearson correlation coefficient.

- Signatures:

  - `CORREL(array1, array2)`

- Examples:

  - CORREL({1,2,3},{2,4,6})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093990

- Source fetch status: failed after 4 attempts

- Summary: Returns Pearson correlation coefficient.

- Signatures:

  - `CORREL(array1, array2)`

- Examples:

  - CORREL({1,2,3},{2,4,6})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/correl-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92
- Google Sheets: https://support.google.com/docs/answer/3093990
