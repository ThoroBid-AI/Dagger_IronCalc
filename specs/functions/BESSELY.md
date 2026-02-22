# BESSELY

## BESSELY

## Purpose
Returns Bessel function of the second kind of order x and x.

## Syntax
- Excel: `BESSELY(x, order)`
- Google Sheets: `BESSELY(x, order)`

## Behavior
- Computes Y-like behavior for real arguments where defined.
- Useful for wave-like analytic calculations.

## Examples (expected outputs)
- `BESSELY(1,0)` -> `0.088256964`

## Error Cases
- Singular/invalid argument combinations produce domain errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bessely`
- File: `base/src/functions/engineering/bessel.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bessely-function-f3a356b3-da89-42c3-8974-2da54d6353a2

- Source fetch status: failed after 4 attempts

- Summary: Returns Bessel function of the second kind of order x and x.

- Signatures:

  - `BESSELY(x, order)`

- Examples:

  - BESSELY(1,0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Singular/invalid argument combinations produce domain errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=BESSELY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bessely-function-f3a356b3-da89-42c3-8974-2da54d6353a2
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=BESSELY
