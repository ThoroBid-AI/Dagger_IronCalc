# CONVERT

## CONVERT

## Purpose
Converts numeric value between unit systems.

## Syntax
- Excel: `CONVERT(number, from_unit, to_unit)`
- Google Sheets: `CONVERT(number, from_unit, to_unit)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CONVERT(1, "m", "cm")` -> `100`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_convert`
- File: `base/src/functions/engineering/convert.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/convert-function-d785bef1-808e-4aac-bdcd-666c810f9af2

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CONVERT(number, from_unit, to_unit)`

- Examples:

  - CONVERT(1, "m", "cm")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055540

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CONVERT(number, from_unit, to_unit)`

- Examples:

  - CONVERT(1, "m", "cm")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/convert-function-d785bef1-808e-4aac-bdcd-666c810f9af2
- Google Sheets: https://support.google.com/docs/answer/6055540
