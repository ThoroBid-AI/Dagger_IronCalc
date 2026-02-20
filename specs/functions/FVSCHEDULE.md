# FVSCHEDULE

## FVSCHEDULE

## Purpose
Future value after applying a schedule of interest rates.

## Syntax
- Excel: `FVSCHEDULE(principal, schedule)`
- Google Sheets: `FVSCHEDULE(principal, schedule)`

## Behavior
- Sequentially compounds principal by each scheduled rate.

## Examples (expected outputs)
- `FVSCHEDULE(1000, {0.02, 0.03}) -> 1060.6`

## Error Cases
- Invalid array shape or non-numeric rates returns error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_fvschedule`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/fvschedule-function-bec29522-bd87-4082-bab9-a241f3fb251d

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FVSCHEDULE(principal, schedule)`

- Examples:

  - FVSCHEDULE(1000, {0.02, 0.03})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid array shape or non-numeric rates returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093226

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FVSCHEDULE(principal, schedule)`

- Examples:

  - FVSCHEDULE(1000, {0.02, 0.03})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid array shape or non-numeric rates returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/fvschedule-function-bec29522-bd87-4082-bab9-a241f3fb251d
- Google Sheets: https://support.google.com/docs/answer/3093226
