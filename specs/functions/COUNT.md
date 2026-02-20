# COUNT

## COUNT

## Purpose
Counts numeric entries in arguments.

## Syntax
- Excel: `COUNT(value1, [value2], ...)`
- Google Sheets: `COUNT(value1, [value2], ...)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `COUNT(1,2,"3",FALSE)` -> `2`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_count`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNT(value1, [value2], ...)`

- Examples:

  - COUNT(1,2,"3",FALSE)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093620

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUNT(value1, [value2], ...)`

- Examples:

  - COUNT(1,2,"3",FALSE)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c
- Google Sheets: https://support.google.com/docs/answer/3093620
