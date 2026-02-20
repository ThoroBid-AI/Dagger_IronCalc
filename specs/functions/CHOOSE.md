# CHOOSE

## CHOOSE

## Purpose
Returns a value from a list by index.

## Syntax
- Excel: `CHOOSE(index_num, value1, [value2], ...)`
- Google Sheets: `CHOOSE(index, value1, [value2], ...)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CHOOSE(2,"A","B","C")` -> `B`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_choose`
- File: `base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/choose-function-fc5c184f-cb62-4ec7-a46e-38653b98f5bc

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CHOOSE(index_num, value1, [value2], ...)`

- Examples:

  - CHOOSE(2,"A","B","C")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093371

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CHOOSE(index, value1, [value2], ...)`

- Examples:

  - CHOOSE(2,"A","B","C")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/choose-function-fc5c184f-cb62-4ec7-a46e-38653b98f5bc
- Google Sheets: https://support.google.com/docs/answer/3093371
