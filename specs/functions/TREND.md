# TREND
## TREND
## Purpose
Computes TREND semantics for spreadsheet formulas.
## Syntax
- Excel: `TREND(...)`
- Google Sheets: `TREND(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_trend`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/trend-function-e2f135f0-8827-4096-9873-9a7cf7b51ef1

- Summary: Syntax: TREND(known_y's, [known_x's], [new_x's], [const])

- Signatures:

  - `TREND(known_y's, [known_x's], [new_x's], [const])`

- Examples:

  - TREND(known_y's, [known_x's], [new_x's], [const])

- Notes: - For information about how Microsoft Excel fits a line to data, see LINEST. - You can use TREND for polynomial curve fitting by regressing against the same variable raised to different powers. For example, suppose column A contains y-values and column B contains x-values. You can enter x^2 in column C, x^3 in column D, and so on, and then regress columns B through D against column A. - Formulas that return arrays must be entered as array formulas with Ctrl+Shift+Enter, unless you have a current version of Microsoft 365, and then you can just press Enter. - When entering an array constant for an argument such as known_x's, use commas to separ…

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094263

- Summary: Given partial data about a linear trend, fits an ideal linear trend using the least squares method and/or predicts further values. Sample Usage TREND(B2:B10,A2:A10) TREND(B2:B10,A2:A10,A11:A13,TRUE

- Signatures:

  - `TREND(known_data_y, [known_data_x], [new_data_x], [b])`

- Examples:

  - TREND(B2:B10,A2:A10)

  - TREND(B2:B10,A2:A10,A11:A13,TRUE)

  - TREND(known_data_y, [known_data_x], [new_data_x], [b])

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trend-function-e2f135f0-8827-4096-9873-9a7cf7b51ef1
- Google Sheets: https://support.google.com/docs/answer/3094263
