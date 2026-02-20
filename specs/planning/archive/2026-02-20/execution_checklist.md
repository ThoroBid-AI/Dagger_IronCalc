# Execution Checklist

> Archived snapshot (2026-02-20). Historical workflow notes only.
> For active execution, use `specs/planning/function_implementation_plan.md`.

## Phase 0: Baseline
- Confirm target oracles: Excel 365 (current) + Google Sheets.
- Confirm default locale: en-US.
- Confirm dual-engine selection scope (workbook-level first).

## Phase 1: Inventory & Validation
- Regenerate comparison matrices if needed:
  - Legacy reference: `python scripts/compare_functions.py` (not present in current repo)
  - Current equivalent:
    - `python scripts/update_function_matrix.py`
    - `python scripts/generate_hf_coverage_reports.py`
- Ensure normalized matrix exists:
  - `specs/matrices/function_matrix_normalized.csv`
- Run doc validator:
  - `python scripts/validate_function_docs.py`

## Phase 2: Planning & Batching
- Confirm complexity map:
  - `specs/data/function_complexity_map.csv`
- Confirm batch plan:
  - `specs/planning/archive/2026-02-20/function_batch_plan.md`
- Confirm implementation plan:
  - `specs/planning/function_implementation_plan.md`
- Confirm doc template:
  - `specs/planning/archive/2026-02-20/function_doc_template.md`

## Phase 3: Documentation
- Generate docs for Batch N (25–50 functions).
- For each doc, include:
  - Purpose, Syntax, Behavior, Examples, Error Cases, Notes, Sources.
- Add code locations for implemented functions using:
  - `specs/reports/function_impl_mapping.csv` (optional; generated only when mapping workflow is run)
- Run validator after each batch.

## Phase 4: Oracle Fixtures
- Define fixture cases per function.
- Capture Excel 365 and Sheets outputs.
- Store fixtures in versioned JSON.
- Run conformance tests.

## Phase 5: Implementation
- Implement functions in batches (easy → medium → hard).
- Add unit tests and conformance fixtures.
- Update coverage reports after each batch.

## Phase 6: Regression & Release
- Run full conformance suite.
- Verify deterministic output.
- Finalize documentation and coverage metrics.
