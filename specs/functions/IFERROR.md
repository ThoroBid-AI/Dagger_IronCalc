# IFERROR

## IFERROR

## Purpose
Returns a fallback value when a formula evaluates to an error.

## Syntax
- Excel: `IFERROR(value, value_if_error)`
- Google Sheets: `IFERROR(value, value_if_error)`

## Behavior
- Catches error values and returns fallback; propagates non-error values.

## Examples (expected outputs)
- `IFERROR(1/0, 0) -> 0`

## Error Cases
Non-error values pass through unchanged.

## Notes
- Implemented in IronCalc.
- Handler: `fn_iferror`
- File: `base/src/functions/logical.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_iferror`
- File: `base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611

- Source fetch status: failed after 4 attempts

- Summary: Returns a fallback value when a formula evaluates to an error.

- Signatures:

  - `IFERROR(value, value_if_error)`

- Examples:

  - IFERROR(1/0, 0)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093304

- Source fetch status: failed after 4 attempts

- Summary: Returns a fallback value when a formula evaluates to an error.

- Signatures:

  - `IFERROR(value, value_if_error)`

- Examples:

  - IFERROR(1/0, 0)

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611
- Google Sheets: https://support.google.com/docs/answer/3093304
