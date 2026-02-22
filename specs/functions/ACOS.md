# ACOS

## ACOS


## Purpose
Return the arccosine (inverse cosine) of a number in radians.

## Syntax
- Excel: `ACOS(number)`
- Google Sheets: `ACOS(value)`

## Behavior
- Input must be between -1 and 1 (inclusive).
- Result is in radians, range 0 to PI.

## Examples (expected outputs)
- `ACOS(-0.5)` -> `2.094395102`

## Error Cases
- Input outside [-1, 1] returns an error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_acos`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/acos-function-cb73173f-d089-4582-afa1-76e5524b5d5b

- Source fetch status: failed after 4 attempts

- Summary: Return the arccosine (inverse cosine) of a number in radians.

- Signatures:

  - `ACOS(number)`

- Examples:

  - ACOS(-0.5)

- Notes: Implemented in IronCalc.

- Error behavior: Input outside [-1, 1] returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093461

- Source fetch status: failed after 4 attempts

- Summary: Return the arccosine (inverse cosine) of a number in radians.

- Signatures:

  - `ACOS(value)`

- Examples:

  - ACOS(-0.5)

- Notes: Implemented in IronCalc.

- Error behavior: Input outside [-1, 1] returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/acos-function-cb73173f-d089-4582-afa1-76e5524b5d5b
- Google Sheets: https://support.google.com/docs/answer/3093461
