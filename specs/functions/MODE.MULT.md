# MODE.MULT

## MODE.MULT

## Purpose
Returns all most frequent values.

## Syntax
- Excel: `MODE.MULT(number1, [number2], ...)`
- Google Sheets: `MODE.MULT(number1, [number2], ...)`

## Behavior
- Returns all modal values.

## Examples (expected outputs)
- `MODE.MULT({1,2,2,3,3}) -> {2,3}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_mode_mult`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mode-mult-function-50fd9464-b2ba-4191-b57a-39446689ae8c

- Source fetch status: failed after 4 attempts

- Summary: Returns all most frequent values.

- Signatures:

  - `MODE.MULT(number1, [number2], ...)`

- Examples:

  - MODE.MULT({1,2,2,3,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368267

- Source fetch status: failed after 4 attempts

- Summary: Returns all most frequent values.

- Signatures:

  - `MODE.MULT(number1, [number2], ...)`

- Examples:

  - MODE.MULT({1,2,2,3,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mode-mult-function-50fd9464-b2ba-4191-b57a-39446689ae8c
- Google Sheets: https://support.google.com/docs/answer/9368267
