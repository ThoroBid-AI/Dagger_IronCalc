# GESTEP

## GESTEP

## Purpose
Returns 1 if number >= step, else 0.

## Syntax
- Excel: `GESTEP(number, [step])`
- Google Sheets: `GESTEP(number, [step])`

## Behavior
- Compares number to threshold.

## Examples (expected outputs)
- `GESTEP(1.5, 2) -> 0`
- `GESTEP(2.5, 2) -> 1`

## Error Cases
- Invalid step or non-numeric input returns error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_gestep`
- File: `base/src/functions/engineering/misc.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/gestep-function-f37e7d2a-41da-4129-be95-640883fca9df

- Source fetch status: failed after 4 attempts

- Summary: Returns 1 if number >= step, else 0.

- Signatures:

  - `GESTEP(number, [step])`

- Examples:

  - GESTEP(1.5, 2)

  - GESTEP(2.5, 2)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid step or non-numeric input returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061379

- Source fetch status: failed after 4 attempts

- Summary: Returns 1 if number >= step, else 0.

- Signatures:

  - `GESTEP(number, [step])`

- Examples:

  - GESTEP(1.5, 2)

  - GESTEP(2.5, 2)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid step or non-numeric input returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/gestep-function-f37e7d2a-41da-4129-be95-640883fca9df
- Google Sheets: https://support.google.com/docs/answer/9061379
