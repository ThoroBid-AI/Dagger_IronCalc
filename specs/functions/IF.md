# IF

## IF

## Purpose
Returns one of two values depending on logical test result.

## Syntax
- Excel: `IF(logical_test, value_if_true, value_if_false)`
- Google Sheets: `IF(condition, value_if_true, value_if_false)`

## Behavior
- Evaluates test with short-circuit branch semantics.

## Examples (expected outputs)
- `IF(1=1, "Y", "N") -> "Y"`

## Error Cases
Invalid argument count returns arity error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_if`
- File: `base/src/functions/logical.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_if`
- File: `base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2

- Source fetch status: failed after 4 attempts

- Summary: Returns one of two values depending on logical test result.

- Signatures:

  - `IF(logical_test, value_if_true, value_if_false)`

- Examples:

  - IF(1=1, "Y", "N")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093364

- Source fetch status: failed after 4 attempts

- Summary: Returns one of two values depending on logical test result.

- Signatures:

  - `IF(condition, value_if_true, value_if_false)`

- Examples:

  - IF(1=1, "Y", "N")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2
- Google Sheets: https://support.google.com/docs/answer/3093364
