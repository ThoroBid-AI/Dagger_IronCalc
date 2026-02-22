# ARABIC

## ARABIC

## Purpose
Converts a Roman numeral string to an Arabic numeral.

## Syntax
- Excel: `ARABIC(text)`
- Google Sheets: `ARABIC(text)`

## Behavior
- Accepts Roman numeral input and returns decimal value.
- Input is case-insensitive and validated for syntax.

## Examples (expected outputs)
- `ARABIC("IV")` -> `4`
- `ARABIC("MCXLV")` -> `1145`

## Error Cases
- Invalid roman text returns error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_arabic`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/arabic-function-9a8da418-c17b-4ef9-a657-9370a30a674f

- Source fetch status: failed after 4 attempts

- Summary: Converts a Roman numeral string to an Arabic numeral.

- Signatures:

  - `ARABIC(text)`

- Examples:

  - ARABIC("IV")

  - ARABIC("MCXLV")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid roman text returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3238301

- Source fetch status: failed after 4 attempts

- Summary: Converts a Roman numeral string to an Arabic numeral.

- Signatures:

  - `ARABIC(text)`

- Examples:

  - ARABIC("IV")

  - ARABIC("MCXLV")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid roman text returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/arabic-function-9a8da418-c17b-4ef9-a657-9370a30a674f
- Google Sheets: https://support.google.com/docs/answer/3238301
