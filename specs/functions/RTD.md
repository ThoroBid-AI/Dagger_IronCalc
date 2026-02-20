# RTD

## RTD

## Purpose
Gets data from DDE/real-time data servers.

## Syntax
- Excel: `RTD(prog_id, server, topic1, topic2, ...)`
- Google Sheets: `RTD(prog_id, server, topic1, topic2, ...)`

## Behavior
Not supported in deterministic offline engine; treat as external data dependency.

## Examples (expected outputs)
- `RTD("ProgID","",1)` -> `#N/A`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_rtd`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rtd-function-e0cc001a-56f0-470a-9b19-9455dc0eb593

- Source fetch status: failed after 4 attempts

- Summary: Gets data from DDE/real-time data servers.

- Signatures:

  - `RTD(prog_id, server, topic1, topic2, ...)`

- Examples:

  - RTD("ProgID","",1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=RTD

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rtd-function-e0cc001a-56f0-470a-9b19-9455dc0eb593
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=RTD
