# ISOMITTED

## ISOMITTED

## Purpose
Returns TRUE for omitted arguments in array formulas or omitted value contexts.

## Syntax
- Excel: `ISOMITTED(value)`
- Google Sheets: `ISOMITTED(value)`

## Behavior
- Detects omitted optional arguments in function call context.

## Examples (expected outputs)
- `ISOMITTED(, ) -> TRUE`

## Error Cases
- Standalone invocation may always return FALSE in non-array contexts.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isomitted`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/isomitted-function-831d6fbc-0f07-40c4-9c5b-9c73fd1d60c1

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE for omitted arguments in array formulas or omitted value contexts.

- Signatures:

  - `ISOMITTED(value)`

- Examples:

  - ISOMITTED(, )

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Standalone invocation may always return FALSE in non-array contexts.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=ISOMITTED

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/isomitted-function-831d6fbc-0f07-40c4-9c5b-9c73fd1d60c1
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=ISOMITTED
