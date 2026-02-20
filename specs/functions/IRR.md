# IRR

## IRR

## Purpose
Returns internal rate of return for periodic cash flows.

## Syntax
- Excel: `IRR(values, [guess])`
- Google Sheets: `IRR(values, [guess])`

## Behavior
- Uses iterative root solving on net present value equation.

## Examples (expected outputs)
- `IRR({-1000,300,300,300,300}) -> 0.193`

## Error Cases
- No convergence or invalid cash flow signs return error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_irr`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc

- Source fetch status: failed after 4 attempts

- Summary: IRR({-1000,300,300,300,300})

- Signatures:

  - `IRR(values, [guess])`

- Examples:

  - IRR({-1000,300,300,300,300})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: No convergence or invalid cash flow signs return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093231

- Source fetch status: failed after 4 attempts

- Summary: IRR({-1000,300,300,300,300})

- Signatures:

  - `IRR(values, [guess])`

- Examples:

  - IRR({-1000,300,300,300,300})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: No convergence or invalid cash flow signs return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc
- Google Sheets: https://support.google.com/docs/answer/3093231
