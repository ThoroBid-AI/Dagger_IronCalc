# IFS

## IFS

## Purpose
Returns value corresponding to first true condition in a list.

## Syntax
- Excel: `IFS(condition1, value1, [condition2, value2], ...)`
- Google Sheets: `IFS(condition1, value1, [condition2, value2], ...)`

## Behavior
- Evaluates pairs in order and returns matching branch result.

## Examples (expected outputs)
- `IFS(1>2, "no", 2>1, "yes") -> "yes"`

## Error Cases
No matching condition or odd argument count returns error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_ifs`
- File: `base/src/functions/logical.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_ifs`
- File: `base/src/functions/logical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45

- Source fetch status: failed after 4 attempts

- Summary: Returns value corresponding to first true condition in a list.

- Signatures:

  - `IFS(condition1, value1, [condition2, value2], ...)`

- Examples:

  - IFS(1>2, "no", 2>1, "yes")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7014145

- Source fetch status: failed after 4 attempts

- Summary: Returns value corresponding to first true condition in a list.

- Signatures:

  - `IFS(condition1, value1, [condition2, value2], ...)`

- Examples:

  - IFS(1>2, "no", 2>1, "yes")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45
- Google Sheets: https://support.google.com/docs/answer/7014145
