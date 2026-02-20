# FORECAST.ETS.SEASONALITY
## FORECAST.ETS.SEASONALITY
## Purpose
Returns seasonality period for ETS forecast data.
## Syntax
- Excel: `FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])`
- Google Sheets: `FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `FORECAST.ETS.SEASONALITY({1,2,3},{1,2,3}) -> 1`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets.seasonality`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/forecast-ets-seasonality-function-32a27a3b-d22f-42ce-8c5d-ef3649269f3c

- Source fetch status: failed after 4 attempts

- Summary: Returns seasonality period for ETS forecast data.

- Signatures:

  - `FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])`

- Examples:

  - FORECAST.ETS.SEASONALITY({1,2,3},{1,2,3})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS.SEASONALITY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/forecast-ets-seasonality-function-32a27a3b-d22f-42ce-8c5d-ef3649269f3c
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS.SEASONALITY
