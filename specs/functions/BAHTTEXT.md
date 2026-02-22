# BAHTTEXT

## BAHTTEXT

## Purpose
Converts a number to Thai Baht text representation.

## Syntax
- Excel: `BAHTTEXT(number)`
- Google Sheets: `BAHTTEXT(number)`

## Behavior
- Produces Thai currency textual form.
- Useful for checks and invoice-style documents.

## Examples (expected outputs)
- `BAHTTEXT(1234.56)` -> Thai text equivalent

## Error Cases
- Non-positive/invalid numeric input may return conversion error.

## Notes
Not implemented in IronCalc. Requires locale-sensitive number-to-text module.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bahttext-function-5ba4d0b4-abd3-4325-8d22-7a92d59aab9c

- Source fetch status: failed after 4 attempts

- Summary: Converts a number to Thai Baht text representation.

- Signatures:

  - `BAHTTEXT(number)`

- Examples:

  - BAHTTEXT(1234.56)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-positive/invalid numeric input may return conversion error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=BAHTTEXT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bahttext-function-5ba4d0b4-abd3-4325-8d22-7a92d59aab9c
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=BAHTTEXT
