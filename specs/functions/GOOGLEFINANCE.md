# GOOGLEFINANCE

## GOOGLEFINANCE

## Purpose
Fetches finance data from online provider for ticker and attributes.

## Syntax
- Excel: `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date], [interval])`
- Google Sheets: `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date], [interval])`

## Behavior
- Performs remote data fetch and returns scalar or array output.

## Examples (expected outputs)
- `GOOGLEFINANCE("NASDAQ:GOOGL", "price") -> 1800.45`

## Error Cases
- Missing network/backend or invalid ticker returns service error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_googlefinance`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Fetches finance data from online provider for ticker and attributes.

- Signatures:

  - `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date], [interval])`

- Examples:

  - GOOGLEFINANCE("NASDAQ:GOOGL", "price")

- Notes: Not implemented in IronCalc.

- Error behavior: Missing network/backend or invalid ticker returns service error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093281

- Source fetch status: failed after 4 attempts

- Summary: Fetches finance data from online provider for ticker and attributes.

- Signatures:

  - `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date], [interval])`

- Examples:

  - GOOGLEFINANCE("NASDAQ:GOOGL", "price")

- Notes: Not implemented in IronCalc.

- Error behavior: Missing network/backend or invalid ticker returns service error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093281
