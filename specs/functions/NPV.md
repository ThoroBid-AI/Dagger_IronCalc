# NPV

## NPV

## Purpose
Computes net present value of a cash flow stream.

## Syntax
- Excel: `NPV(rate, value1, [value2], ...)`
- Google Sheets: `NPV(rate, value1, [value2], ...)`

## Behavior
Discounts future payments with constant rate and sums present value.

## Examples (expected outputs)
- `NPV(0.1, 100, 110)` -> `199.09`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_npv`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568

- Source fetch status: failed after 4 attempts

- Summary: Computes net present value of a cash flow stream.

- Signatures:

  - `NPV(rate, value1, [value2], ...)`

- Examples:

  - NPV(0.1, 100, 110)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093184

- Source fetch status: failed after 4 attempts

- Summary: Computes net present value of a cash flow stream.

- Signatures:

  - `NPV(rate, value1, [value2], ...)`

- Examples:

  - NPV(0.1, 100, 110)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568
- Google Sheets: https://support.google.com/docs/answer/3093184
