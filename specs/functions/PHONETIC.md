# PHONETIC

## PHONETIC

## Purpose
Converts text to phonetic reading.

## Syntax
- Excel: `PHONETIC(text)`
- Google Sheets: `PHONETIC(text)`

## Behavior
Returns phonetic transcription for Japanese text.

## Examples (expected outputs)
- `PHONETIC("電話")` -> `デンワ`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_phonetic`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/phonetic-function-9a329dac-0c0f-42f8-9a55-639086988554

- Source fetch status: failed after 4 attempts

- Summary: Converts text to phonetic reading.

- Signatures:

  - `PHONETIC(text)`

- Examples:

  - PHONETIC("電話")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=PHONETIC

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/phonetic-function-9a329dac-0c0f-42f8-9a55-639086988554
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=PHONETIC
