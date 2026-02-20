# IFNA

## IFNA

## Purpose
Returns fallback when value is #N/A, otherwise returns the value.

## Syntax
- Excel: `IFNA(value, value_if_na)`
- Google Sheets: `IFNA(value, value_if_na)`

## Behavior
- Special-cases only #N/A-like errors.

## Examples (expected outputs)
- `IFNA(NA(), "missing") -> "missing"`

## Error Cases
Only #N/A is intercepted; other errors pass through.

## Notes
- Implemented in IronCalc.
- Handler: `fn_ifna`
- File: `base/src/functions/logical.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_ifna`
- File: `base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461

- Source fetch status: failed after 4 attempts

- Summary: Returns fallback when value is #N/A, otherwise returns the value.

- Signatures:

  - `IFNA(value, value_if_na)`

- Examples:

  - IFNA(NA()

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9365944

- Source fetch status: failed after 4 attempts

- Summary: Returns fallback when value is #N/A, otherwise returns the value.

- Signatures:

  - `IFNA(value, value_if_na)`

- Examples:

  - IFNA(NA()

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461
- Google Sheets: https://support.google.com/docs/answer/9365944
