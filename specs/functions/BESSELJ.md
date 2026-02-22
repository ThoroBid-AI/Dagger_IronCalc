# BESSELJ

## BESSELJ

## Purpose
Returns the Bessel function of the first kind J(n, x).

## Syntax
- Excel: `BESSELJ(x, order)`
- Google Sheets: `BESSELJ(x, order)`

## Behavior
- Computes Bessel J function for given arguments.
- Returns numeric output for real input ranges used in engineering use-cases.

## Examples (expected outputs)
- `BESSELJ(0.5,1)` -> `0.242268457`

## Error Cases
- Invalid numeric domains return argument errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_besselj`
- File: `base/src/functions/engineering/bessel.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/besselj-function-839cb181-48de-408b-9d80-bd02982d94f7

- Source fetch status: failed after 4 attempts

- Summary: Returns the Bessel function of the first kind J(n, x).

- Signatures:

  - `BESSELJ(x, order)`

- Examples:

  - BESSELJ(0.5,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid numeric domains return argument errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=BESSELJ

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/besselj-function-839cb181-48de-408b-9d80-bd02982d94f7
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=BESSELJ
