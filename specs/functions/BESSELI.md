# BESSELI

## BESSELI

## Purpose
Returns the modified Bessel function I(n, x).

## Syntax
- Excel: `BESSELI(x, order)`
- Google Sheets: `BESSELI(x, order)`

## Behavior
- Computes I-variant Bessel function for scalar x and order.
- Uses numeric evaluation with domain checks used by IronCalc implementation.

## Examples (expected outputs)
- `BESSELI(1,0)` -> `1.266065877`

## Error Cases
- Invalid order or domain errors propagate to value errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_besseli`
- File: `base/src/functions/engineering/bessel.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/besseli-function-8d33855c-9a8d-444b-98e0-852267b1c0df

- Source fetch status: failed after 4 attempts

- Summary: Returns the modified Bessel function I(n, x).

- Signatures:

  - `BESSELI(x, order)`

- Examples:

  - BESSELI(1,0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid order or domain errors propagate to value errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=BESSELI

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/besseli-function-8d33855c-9a8d-444b-98e0-852267b1c0df
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=BESSELI
