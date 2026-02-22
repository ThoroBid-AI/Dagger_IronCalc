# AGGREGATE

## AGGREGATE

## Purpose
Returns an aggregate over data with optional options to ignore errors or hidden values.

## Syntax
- Excel: `AGGREGATE(function_num, options, array, [k])`
- Google Sheets: `AGGREGATE(function_num, options, array, [k])`

## Behavior
- Supports function selector in `function_num` and option flags in `options`.
- Can be used to produce stats like SUM, AVERAGE, MAX while ignoring filtered rows/errors.

## Examples (expected outputs)
- `AGGREGATE(9, 6, {1,2,#N/A,4}, 0)` -> `7`

## Error Cases
- Invalid `function_num` or unsupported options should return an argument error.
Error propagation depends on ignore options.

## Notes
Not implemented in IronCalc. Planned as a combined aggregate with compatibility layer.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/aggregate-function-43b9278e-6aa7-4f17-92b6-e19993fa26df

- Source fetch status: failed after 4 attempts

- Summary: Returns an aggregate over data with optional options to ignore errors or hidden values.

- Signatures:

  - `AGGREGATE(function_num, options, array, [k])`

- Examples:

  - AGGREGATE(9, 6, {1,2,#N/A,4}, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid `function_num` or unsupported options should return an argument error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=AGGREGATE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/aggregate-function-43b9278e-6aa7-4f17-92b6-e19993fa26df
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=AGGREGATE
