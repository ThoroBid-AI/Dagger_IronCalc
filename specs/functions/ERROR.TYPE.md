# ERROR.TYPE

## ERROR.TYPE

## Purpose
Returns an integer code describing the last error type.

## Syntax
- Excel: `ERROR.TYPE(error_val)`
- Google Sheets: `ERROR.TYPE(error_val)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `ERROR.TYPE(#N/A) -> 7`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  1. `map each error variant to spreadsheet error code integer`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/error-type-function-10958677-7c8d-44f7-ae77-b9a9ee6eefaa

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `ERROR.TYPE(error_val)`

- Examples:

  - ERROR.TYPE(#N/A)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3238305

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `ERROR.TYPE(error_val)`

- Examples:

  - ERROR.TYPE(#N/A)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/error-type-function-10958677-7c8d-44f7-ae77-b9a9ee6eefaa
- Google Sheets: https://support.google.com/docs/answer/3238305
