# IMPORTRANGE

## IMPORTRANGE

## Purpose
Imports a range from another spreadsheet.

## Syntax
- Excel: `IMPORTRANGE(url, range_string)`
- Google Sheets: `IMPORTRANGE(spreadsheet_url, range_string)`

## Behavior
- Resolves external workbook reference and returns range values.

## Examples (expected outputs)
- `IMPORTRANGE("id","A1:B2") -> {1,2;3,4}`

## Error Cases
Invalid permissions or external access failures return errors.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importrange`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importrange`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Imports a range from another spreadsheet.

- Signatures:

  - `IMPORTRANGE(url, range_string)`

- Examples:

  - IMPORTRANGE("id","A1:B2")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093340

- Source fetch status: failed after 4 attempts

- Summary: Imports a range from another spreadsheet.

- Signatures:

  - `IMPORTRANGE(spreadsheet_url, range_string)`

- Examples:

  - IMPORTRANGE("id","A1:B2")

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093340
