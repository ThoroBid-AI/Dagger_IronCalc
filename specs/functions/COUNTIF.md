# COUNTIF

## COUNTIF

## Purpose
Counts cells that meet a single criteria.

## Syntax
- Excel: `COUNTIF(range, criteria)`
- Google Sheets: `COUNTIF(range, criterion)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUNTIF({1,2,3}, 2) -> 1`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_countif`
- File: `base/src/functions/statistical/if_ifs.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/use-the-countif-function-in-microsoft-excel-e0de10c6-f885-4e71-abb4-1f464816df34

- Source fetch status: failed after 4 attempts

- Summary: Counts cells that meet a single criteria.

- Signatures:

  - `COUNTIF(range, criteria)`

- Examples:

  - COUNTIF({1,2,3}, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093480

- Source fetch status: failed after 4 attempts

- Summary: Counts cells that meet a single criteria.

- Signatures:

  - `COUNTIF(range, criterion)`

- Examples:

  - COUNTIF({1,2,3}, 2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/use-the-countif-function-in-microsoft-excel-e0de10c6-f885-4e71-abb4-1f464816df34
- Google Sheets: https://support.google.com/docs/answer/3093480
