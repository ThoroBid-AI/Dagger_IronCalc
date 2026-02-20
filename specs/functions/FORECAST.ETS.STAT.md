# FORECAST.ETS.STAT
## FORECAST.ETS.STAT
## Purpose
Returns regression statistic for ETS forecast.
## Syntax
- Excel: `FORECAST.ETS.STAT(values, timeline, stat_type)`
- Google Sheets: `FORECAST.ETS.STAT(values, timeline, stat_type)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `FORECAST.ETS.STAT({1,2,3},{1,2,3},1) -> value`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets.stat`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/forecast-ets-stat-function-60f2ae14-d0cf-465e-9736-625ccaaa60b4

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible under seeded execution context.

- Signatures:

  - `FORECAST.ETS.STAT(values, timeline, stat_type)`

- Examples:

  - FORECAST.ETS.STAT({1,2,3},{1,2,3},1)

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS.STAT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/forecast-ets-stat-function-60f2ae14-d0cf-465e-9736-625ccaaa60b4
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=FORECAST.ETS.STAT
