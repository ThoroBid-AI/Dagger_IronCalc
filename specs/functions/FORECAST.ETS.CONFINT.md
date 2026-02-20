# FORECAST.ETS.CONFINT
## FORECAST.ETS.CONFINT
## Purpose
Returns confidence interval for ETS forecast.
## Syntax
- Excel: `FORECAST.ETS.CONFINT(target_date, values, timeline, [statistic], [confidence])`
- Google Sheets: `FORECAST.ETS.CONFINT(target_date, values, timeline, [statistic], [confidence])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `FORECAST.ETS.CONFINT("2026-02-28",{1,2,3},{1,2,3},1,0.95) -> {low,high}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets.confint`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/forecast-ets-confint-function-6d4a7557-11fa-4678-9e6a-dbcc31a7c7df

- Source fetch status: failed after 4 attempts

- Summary: Returns confidence interval for ETS forecast.

- Signatures:

  - `FORECAST.ETS.CONFINT(target_date, values, timeline, [statistic], [confidence])`

- Examples:

  - FORECAST.ETS.CONFINT("2026-02-28",{1,2,3},{1,2,3},1,0.95)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS.CONFINT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/forecast-ets-confint-function-6d4a7557-11fa-4678-9e6a-dbcc31a7c7df
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS.CONFINT
