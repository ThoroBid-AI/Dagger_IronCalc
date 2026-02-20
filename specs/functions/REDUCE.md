# REDUCE

## REDUCE

## Purpose
Accumulates values from an array with a lambda-like reducer.

## Syntax
- Excel: `REDUCE(initial_value, array, reducer, [initial_value2], ...)`
- Google Sheets: `REDUCE(initial_value, array, reducer, ...)`

## Behavior
Runs reducer left-to-right across array values.

## Examples (expected outputs)
- `REDUCE(0,{1,2,3},LAMBDA(a,b,a+b))` -> `6`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_reduce`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/reduce-function-42e39910-b345-45f3-84b8-0642b568b7cb

- Source fetch status: failed after 4 attempts

- Summary: Accumulates values from an array with a lambda-like reducer.

- Signatures:

  - `REDUCE(initial_value, array, reducer, [initial_value2], ...)`

- Examples:

  - REDUCE(0,{1,2,3},LAMBDA(a,b,a+b)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12568597

- Source fetch status: failed after 4 attempts

- Summary: Accumulates values from an array with a lambda-like reducer.

- Signatures:

  - `REDUCE(initial_value, array, reducer, ...)`

- Examples:

  - REDUCE(0,{1,2,3},LAMBDA(a,b,a+b)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/reduce-function-42e39910-b345-45f3-84b8-0642b568b7cb
- Google Sheets: https://support.google.com/docs/answer/12568597
