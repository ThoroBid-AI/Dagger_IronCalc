# FREQUENCY

## FREQUENCY

## Purpose
Returns frequency counts for values across bins.

## Syntax
- Excel: `FREQUENCY(data_array, bins_array)`
- Google Sheets: `FREQUENCY(data_array, bins_array)`

## Behavior
- Returns a vertical array with one extra bin for values above last threshold.

## Examples (expected outputs)
- `FREQUENCY({1,2,3}, {2}) -> {2,1}`

## Error Cases
- Empty bins or non-numeric data produce errors.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/frequency.rs`
- Proposed handler: `fn_frequency`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/frequency-function-44e3be2b-eca0-42cd-a3f7-fd9ea898fdb9

- Source fetch status: failed after 4 attempts

- Summary: Returns frequency counts for values across bins.

- Signatures:

  - `FREQUENCY(data_array, bins_array)`

- Examples:

  - FREQUENCY({1,2,3}, {2})

- Notes: Not implemented in IronCalc.

- Error behavior: Empty bins or non-numeric data produce errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094286

- Source fetch status: failed after 4 attempts

- Summary: Returns frequency counts for values across bins.

- Signatures:

  - `FREQUENCY(data_array, bins_array)`

- Examples:

  - FREQUENCY({1,2,3}, {2})

- Notes: Not implemented in IronCalc.

- Error behavior: Empty bins or non-numeric data produce errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/frequency-function-44e3be2b-eca0-42cd-a3f7-fd9ea898fdb9
- Google Sheets: https://support.google.com/docs/answer/3094286
