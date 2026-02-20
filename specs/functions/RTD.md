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

- Summary: Retrieves real-time data from a program that supports COM automation.

- Signatures:

  - `RTD(ProgID, server, topic1, [topic2], ...)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description (Result) Result =RTD("mycomaddin.progid",,"Server_name","Price") Real-time data retrieved from a program that supports COM automation. #N/A Note The RTD COM automation add-in must be created and registered on a local computer. If you haven't installed a real-time data server, the RTD function returns the #N/A error message in a cell when you try to use the RTD function.

- Notes: - The RTD COM automation add-in must be created and registered on a local computer. If you haven't installed a real-time data server, you will get an error message in a cell when you try to use the RTD function. - When the server has been programmed to continually update results, unlike other functions, RTD formulas will change when Microsoft Excel is in automatic calculation mode.

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
