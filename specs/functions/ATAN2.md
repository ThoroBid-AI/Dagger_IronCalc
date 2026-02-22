# ATAN2

## ATAN2


## Purpose
Return the arctangent of the specified x- and y-coordinates in radians.

## Syntax
- Excel: `ATAN2(x_num, y_num)`
- Google Sheets: `ATAN2(x, y)`

## Behavior
- Result is in radians, range -PI to PI (excluding -PI).
- If both inputs are 0, returns `#DIV/0!`.

## Examples (expected outputs)
- `ATAN2(1,1)` -> `0.785398163`
- `ATAN2(-1,-1)` -> `-2.35619449`

## Error Cases
- If both inputs are 0, returns `#DIV/0!`.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_atan2`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/atan2-function-c04592ab-b9e3-4908-b428-c96b3a565033

- Source fetch status: failed after 4 attempts

- Summary: Return the arctangent of the specified x- and y-coordinates in radians.

- Signatures:

  - `ATAN2(x_num, y_num)`

- Examples:

  - ATAN2(1,1)

  - ATAN2(-1,-1)

- Notes: Implemented in IronCalc.

- Error behavior: If both inputs are 0, returns `#DIV/0!`.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093468

- Source fetch status: failed after 4 attempts

- Summary: Return the arctangent of the specified x- and y-coordinates in radians.

- Signatures:

  - `ATAN2(x, y)`

- Examples:

  - ATAN2(1,1)

  - ATAN2(-1,-1)

- Notes: Implemented in IronCalc.

- Error behavior: If both inputs are 0, returns `#DIV/0!`.



## Sources
- Excel: https://support.microsoft.com/en-us/office/atan2-function-c04592ab-b9e3-4908-b428-c96b3a565033
- Google Sheets: https://support.google.com/docs/answer/3093468
