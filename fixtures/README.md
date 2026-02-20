# Oracle Fixtures

Fixtures are stored as JSON files under `fixtures/<FUNCTION>/<case_id>_<engine>.json`.

## Required Fields
- `engine`: `excel` or `sheets`
- `version`: Excel build or Sheets capture date
- `locale`: `en-US`
- `function`: function name
- `case_id`: unique case identifier
- `inputs`: list of `{ cell, value }` entries
- `formula`: formula string (include leading `=`)
- `target`: target cell reference (must include sheet, e.g. `Sheet1!A1`)
- `expected_text`: expected formatted output text
- `notes`: optional

## Notes
- Use explicit sheet names in all `cell` and `target` fields (e.g. `Sheet1!A1`).
- `expected_text` should match the displayed/ formatted output from the oracle.
