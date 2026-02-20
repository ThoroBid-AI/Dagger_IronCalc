# FORECAST.ETS
## FORECAST.ETS
## Purpose
Forecasts values using exponential smoothing.
## Syntax
- Excel: `FORECAST.ETS(target_date, values, timeline, ...)`
- Google Sheets: `FORECAST.ETS(target_date, values, timeline, ...)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `FORECAST.ETS("2026-02-28", {1,2,3}, {1,2,3}) -> value`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `FORECAST.ETS(target_date, values, timeline, ...)`

- Examples:

  - FORECAST.ETS("2026-02-28", {1,2,3}, {1,2,3})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS
