# Function Source Extraction Plan (Tables + Signatures)

> Archived snapshot (2026-02-20). Historical planning note.
> Current Lua workflow runs from `specs/lua_prompts.md`; detailed specs are optional.

## Goal
Extract robust, deterministic function documentation from Microsoft and Google Sheets help pages so each function doc can include:
- source signature candidates
- structured examples
- argument details from parameter tables
- error behavior notes

## 1) Source URL resolution
1. Keep canonical per-function URLs in `specs/functions/<FUNCTION>.md` `Sources` sections (when those files exist).
2. Build a daily refresh script that:
   - pulls Microsoft index once and maps visible function names to support pages
   - pulls Google Sheets index table and maps visible function names to answer pages
   - writes per-function URLs back into `## Sources`.

## 2) Fetch + normalization layer
- Use `urllib.request` with rotating User-Agent + Accept-Language (`en-US`) + short retry backoff.
- On each fetch:
  - decode bytes as UTF-8/replace
  - remove script/style/nav/footer chunks before parsing
  - parse HTML with regex-based section extraction (compatible with current environment)

## 3) Section parser
- Split HTML by heading tags (`h1`–`h6`) into ordered section tuples `(title, body_html)`.
- For each provider, target sections by keywords:
  - `syntax`
  - `examples`
  - `arguments` / `syntax` / `remarks` / `notes` / `return value`
  - `error`, `errors`, `error handling`

## 4) Table extraction strategy
1. Find `<table>` blocks in the candidate sections.
2. Parse `<tr>` and `<td>/<th>` cells.
3. Detect table intent using header row keywords:
   - Signature/Syntax table if header contains `Syntax`, `Function syntax`
   - Argument table if header contains `Argument`, `Description`
   - Example table if header contains `Example`, `Formula`, `Result`, `Input`
4. Convert relevant tables to compact bullets:
   - `name: description` for argument rows
   - `=FORMULA` style for example rows

## 5) Signature extraction rules
- First pass: scan `syntax` and `return` section HTML for signatures in `<code>`, `<b>`, `<strong>`.
- Second pass: scan visible text and image `alt` text for formula patterns like:
  - `FN(...)`
- De-duplicate and cap at 4 signatures.

## 6) Example extraction rules
- First pass: scan examples section code blocks and `alt` attributes.
- Second pass: extract example tables and map `Formula -> Result`/`Example` rows.
- If examples are not present, capture `No source data` marker and keep validator failure explicit.

## 7) Validation checks
- Update `scripts/validate_function_docs.py` to enforce:
  - both provider docs sections exist
  - per-provider URL domain is correct and non-generic for supported functions
  - signatures/errors/examples/notes are present and non-placeholder
  - signatures include at least one function call matching function name
  - examples contain at least one formula-like token
- Report all issues to `specs/reports/function_doc_validation.csv` with batch context.

## 8) Human-in-the-loop fallback
- Any failure with `placeholder`/`insufficient` reasons should generate a worker task for manual enrichment.
- Manual fixes only fill missing provider fields (don’t change behavior docs outside function docs).
