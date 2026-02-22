# FORECAST.LINEAR
## FORECAST.LINEAR
## Purpose
Returns linear trend forecast.
## Syntax
- Excel: `FORECAST.LINEAR(x, known_ys, known_xs)`
- Google Sheets: `FORECAST.LINEAR(x, known_ys, known_xs)`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `FORECAST.LINEAR(4,{3,5,7},{1,2,3}) -> 9`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.linear`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99

- Source fetch status: failed after 4 attempts

- Summary: Returns linear trend forecast.

- Signatures:

  - `FORECAST.LINEAR(x, known_ys, known_xs)`

- Examples:

  - FORECAST.LINEAR(4,{3,5,7},{1,2,3})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094000

- Source fetch status: failed after 4 attempts

- Summary: Returns linear trend forecast.

- Signatures:

  - `FORECAST.LINEAR(x, known_ys, known_xs)`

- Examples:

  - FORECAST.LINEAR(4,{3,5,7},{1,2,3})

- Notes: Deterministic and reproducible under seeded execution context.

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99
- Google Sheets: https://support.google.com/docs/answer/3094000
