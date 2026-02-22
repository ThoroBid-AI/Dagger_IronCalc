# NA

## NA

## Purpose
Returns #N/A error.

## Syntax
- Excel: `NA()`
- Google Sheets: `NA()`

## Behavior
- Dedicated missing-value error constructor.

## Examples (expected outputs)
- `NA() -> #N/A`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/information.rs`
- Proposed handler: `fn_na`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c

- Source fetch status: failed after 4 attempts

- Summary: Returns #N/A error.

- Signatures:

  - `NA()`

- Examples:

  - NA()

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093359

- Source fetch status: failed after 4 attempts

- Summary: Returns #N/A error.

- Signatures:

  - `NA()`

- Examples:

  - NA()

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c
- Google Sheets: https://support.google.com/docs/answer/3093359
