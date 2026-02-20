# INFO

## INFO

## Purpose
Returns metadata information about a formula or environment (where supported).

## Syntax
- Excel: `INFO(type_text)`
- Google Sheets: `INFO(type_text)`

## Behavior
- Accepts an info type and returns corresponding metadata in compatible output type.

## Examples (expected outputs)
- `INFO("system") -> "Windows"`

## Error Cases
- Unknown info type returns a value error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_info`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/info-function-725f259a-0e4b-49b3-8b52-58815c69acae

- Source fetch status: failed after 4 attempts

- Summary: INFO("system")

- Signatures:

  - `INFO(type_text)`

- Examples:

  - INFO("system")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Unknown info type returns a value error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=INFO

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/info-function-725f259a-0e4b-49b3-8b52-58815c69acae
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=INFO
