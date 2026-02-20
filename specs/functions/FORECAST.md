# FORECAST

## FORECAST

## Purpose
Predicts a value using linear trend from known data pairs.

## Syntax
- Excel: `FORECAST(x, known_ys, known_xs)`
- Google Sheets: `FORECAST(x, known_ys, known_xs)`

## Behavior
- Requires equal-length numeric arrays; computes slope and intercept and applies to x.

## Examples (expected outputs)
- `FORECAST(6, {20,25,30}, {1,2,3}) -> 35`

## Error Cases
- Mismatched array lengths or invalid regression input returns error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99

- Source fetch status: failed after 4 attempts

- Summary: Predicts a value using linear trend from known data pairs.

- Signatures:

  - `FORECAST(x, known_ys, known_xs)`

- Examples:

  - FORECAST(6, {20,25,30}, {1,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Mismatched array lengths or invalid regression input returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094000

- Source fetch status: failed after 4 attempts

- Summary: Predicts a value using linear trend from known data pairs.

- Signatures:

  - `FORECAST(x, known_ys, known_xs)`

- Examples:

  - FORECAST(6, {20,25,30}, {1,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Mismatched array lengths or invalid regression input returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99
- Google Sheets: https://support.google.com/docs/answer/3094000
