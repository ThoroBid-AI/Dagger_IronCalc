# ISO.CEILING

## ISO.CEILING

## Purpose
Rounds value up to nearest multiple using ISO week-compatible numeric behavior.

## Syntax
- Excel: `ISO.CEILING(number, [significance], [mode])`
- Google Sheets: `ISO.CEILING(number, [significance], [mode])`

## Behavior
- Applies ISO-compatible ceiling behavior for number/significance/mode.

## Examples (expected outputs)
- `ISO.CEILING(12.2) -> 13`

## Error Cases
- Invalid significance or mode returns error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_iso_ceiling`
- Proposed file: `base/src/functions/mathematical.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/iso-ceiling-function-e587bb73-6cc2-4113-b664-ff5b09859a83

- Source fetch status: failed after 4 attempts

- Summary: ISO.CEILING(12.2)

- Signatures:

  - `ISO.CEILING(number, [significance], [mode])`

- Examples:

  - ISO.CEILING(12.2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid significance or mode returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061294

- Source fetch status: failed after 4 attempts

- Summary: ISO.CEILING(12.2)

- Signatures:

  - `ISO.CEILING(number, [significance], [mode])`

- Examples:

  - ISO.CEILING(12.2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid significance or mode returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/iso-ceiling-function-e587bb73-6cc2-4113-b664-ff5b09859a83
- Google Sheets: https://support.google.com/docs/answer/9061294
