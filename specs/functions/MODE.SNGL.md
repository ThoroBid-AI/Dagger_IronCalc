# MODE.SNGL

## MODE.SNGL

## Purpose
Returns single mode.

## Syntax
- Excel: `MODE.SNGL(number1, [number2], ...)`
- Google Sheets: `MODE.SNGL(number1, [number2], ...)`

## Behavior
- Returns one mode with deterministic tie rules.

## Examples (expected outputs)
- `MODE.SNGL({1,2,2,3,3}) -> 2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_mode_sngl`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mode-sngl-function-f1267c16-66c6-4386-959f-8fba5f8bb7f8

- Source fetch status: failed after 4 attempts

- Summary: Returns single mode.

- Signatures:

  - `MODE.SNGL(number1, [number2], ...)`

- Examples:

  - MODE.SNGL({1,2,2,3,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094029

- Source fetch status: failed after 4 attempts

- Summary: Returns single mode.

- Signatures:

  - `MODE.SNGL(number1, [number2], ...)`

- Examples:

  - MODE.SNGL({1,2,2,3,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mode-sngl-function-f1267c16-66c6-4386-959f-8fba5f8bb7f8
- Google Sheets: https://support.google.com/docs/answer/3094029
