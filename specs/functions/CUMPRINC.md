# CUMPRINC

## CUMPRINC

## Purpose
Returns cumulative principal paid between periods.

## Syntax
- Excel: `CUMPRINC(rate, nper, pv, start_period, end_period, type)`
- Google Sheets: `CUMPRINC(rate, nper, pv, start_period, end_period, type)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUMPRINC(0.05, 12, 10000, 1, 3, 0) -> 500`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_cumprinc`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CUMPRINC(rate, nper, pv, start_period, end_period, type)`

- Examples:

  - CUMPRINC(0.05, 12, 10000, 1, 3, 0)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093159

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CUMPRINC(rate, nper, pv, start_period, end_period, type)`

- Examples:

  - CUMPRINC(0.05, 12, 10000, 1, 3, 0)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d
- Google Sheets: https://support.google.com/docs/answer/3093159
