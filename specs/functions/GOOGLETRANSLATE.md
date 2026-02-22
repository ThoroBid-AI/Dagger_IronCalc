# GOOGLETRANSLATE

## GOOGLETRANSLATE

## Purpose
Translates text between languages via service integration.

## Syntax
- Excel: `GOOGLETRANSLATE(text, source_language, target_language)`
- Google Sheets: `GOOGLETRANSLATE(text, source_language, target_language)`

## Behavior
- Returns translated text with deterministic handling of language codes.

## Examples (expected outputs)
- `GOOGLETRANSLATE("hello", "en", "es") -> "hola"`

## Error Cases
- Missing backend/language codes returns service error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_googletranslate`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Translates text between languages via service integration.

- Signatures:

  - `GOOGLETRANSLATE(text, source_language, target_language)`

- Examples:

  - GOOGLETRANSLATE("hello", "en", "es")

- Notes: Not implemented in IronCalc.

- Error behavior: Missing backend/language codes returns service error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093331

- Source fetch status: failed after 4 attempts

- Summary: Translates text between languages via service integration.

- Signatures:

  - `GOOGLETRANSLATE(text, source_language, target_language)`

- Examples:

  - GOOGLETRANSLATE("hello", "en", "es")

- Notes: Not implemented in IronCalc.

- Error behavior: Missing backend/language codes returns service error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093331
