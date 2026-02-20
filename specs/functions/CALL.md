# CALL

## CALL

## Purpose
Calls an external routine in legacy workbook-compatible models.

## Syntax
- Excel: `CALL(program, arg1, [arg2], ...)`
- Google Sheets: not supported natively

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CALL("lib", 1, 2)` -> environment-specific

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Parse function arity and normalize inputs.
- Reuse shared parser and numeric helpers where available.
- Implement domain checks and deterministic output formatting.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/call-function-32d58445-e646-4ffd-8d5e-b45077a5e995

- Source fetch status: failed after 4 attempts

- Summary: Calls an external routine in legacy workbook-compatible models.

- Signatures:

  - `CALL(program, arg1, [arg2], ...)`

- Examples:

  - CALL("lib", 1, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CALL

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/call-function-32d58445-e646-4ffd-8d5e-b45077a5e995
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CALL
