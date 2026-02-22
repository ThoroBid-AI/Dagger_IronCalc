# MIDB

## MIDB

## Purpose
Returns byte-based substring.

## Syntax
- Excel: `MIDB(text, start_num, num_chars)`
- Google Sheets: `MIDB(text, start_num, num_chars)`

## Behavior
- Byte-position extraction rules.

## Examples (expected outputs)
- `MIDB("hello",2,2) -> "el"`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_midb`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns byte-based substring.

- Signatures:

  - `MIDB(text, start_num, num_chars)`

- Examples:

  - MIDB("hello",2,2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9367691

- Source fetch status: failed after 4 attempts

- Summary: Returns byte-based substring.

- Signatures:

  - `MIDB(text, start_num, num_chars)`

- Examples:

  - MIDB("hello",2,2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9367691
