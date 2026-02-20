# MODE

## MODE

## Purpose
Returns most frequent value.

## Syntax
- Excel: `MODE(number1, [number2], ...)`
- Google Sheets: `MODE(number1, [number2], ...)`

## Behavior
- Single-mode return behavior.

## Examples (expected outputs)
- `MODE({1,2,2,3}) -> 2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_mode`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mode-function-e45192ce-9122-4980-82ed-4bdc34973120

- Source fetch status: failed after 4 attempts

- Summary: Returns most frequent value.

- Signatures:

  - `MODE(number1, [number2], ...)`

- Examples:

  - MODE({1,2,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094029

- Source fetch status: failed after 4 attempts

- Summary: Returns most frequent value.

- Signatures:

  - `MODE(number1, [number2], ...)`

- Examples:

  - MODE({1,2,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mode-function-e45192ce-9122-4980-82ed-4bdc34973120
- Google Sheets: https://support.google.com/docs/answer/3094029
