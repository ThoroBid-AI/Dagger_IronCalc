# SPARKLINE
## SPARKLINE
## Purpose
Computes SPARKLINE semantics for spreadsheet formulas.
## Syntax
- Excel: `SPARKLINE(...)`
- Google Sheets: `SPARKLINE(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sparkline`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples: No examples captured from source page or local docs.

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093289

- Summary: Computes SPARKLINE semantics for spreadsheet formulas.

- Signatures:

  - `SPARKLINE(data, [options])`

- Examples:

  - SPARKLINE(A1:F1)

  - SPARKLINE(A2:E2,{"charttype","bar";"max",40})

  - SPARKLINE(A2:E2,A4:B5)

  - SPARKLINE(A1:A5, {"charttype","column"; "axis", true; "axiscolor", "red"})

  - SPARKLINE(data, [options])

- Notes: - Colors can be written using their names (e.g., "green") or as a hex code (e.g., "#3D3D3D"). - To modify the color of a line chart, change the font color of the cell.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093289
