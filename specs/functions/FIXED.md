# FIXED

## FIXED

## Purpose
Formats a number to fixed decimals as text with optional thousands separators and rounding.

## Syntax
- Excel: `FIXED(number, [decimals], [no_commas])`
- Google Sheets: `FIXED(number, [decimals], [no_commas])`

## Behavior
- Applies host numeric rounding and returns text-formatted output.

## Examples (expected outputs)
- `FIXED(1234.567, 2, TRUE) -> "1234.57"`

## Error Cases
- Invalid decimal precision or non-numeric input returns error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_fixed`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/fixed-function-ffd5723c-324c-45e9-8b96-e41be2a8274a

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FIXED(number, [decimals], [no_commas])`

- Examples:

  - FIXED(1234.567, 2, TRUE)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid decimal precision or non-numeric input returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094075

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FIXED(number, [decimals], [no_commas])`

- Examples:

  - FIXED(1234.567, 2, TRUE)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid decimal precision or non-numeric input returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/fixed-function-ffd5723c-324c-45e9-8b96-e41be2a8274a
- Google Sheets: https://support.google.com/docs/answer/3094075
