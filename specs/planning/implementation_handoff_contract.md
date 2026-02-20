# Implementation Handoff Contract

This is the single execution contract for handing backlog implementation to another LLM.

## Purpose
- Remove ambiguity about where code goes, what to edit, how to validate, and what to update.

## Runtime + Scope (Locked)
- Runtime target is the Rust engine in `base/`.
- `specs/lua_prompts.md` is a behavior/spec guidance artifact, not executable Lua runtime code.
- Implement only functions tracked in `specs/reports/lua_backlog_status.csv` unless explicitly expanded.

## Source Inputs (Use In This Order)
1. `specs/reports/lua_backlog_status.csv` (what is pending)
2. `specs/planning/lua_implementation_backlog.md` (execution order)
3. `specs/lua_prompts.md` (primary behavior details)
4. `specs/functions/<FUNCTION>.md` when present (additional detail)
5. `specs/reports/ironcalc_missing_but_in_hf.csv` (coverage guardrail)

## Per-Function Execution Steps
1. Pick the next `status_done=pending` function from `specs/reports/lua_backlog_status.csv` following backlog order.
2. Confirm it is not already implemented by checking existing lookup + dispatch in `base/src/functions/mod.rs` and notes in `specs/functions/<FUNCTION>.md`.
3. Read the function section in `specs/lua_prompts.md` and optional `specs/functions/<FUNCTION>.md`.
4. Implement parser/function identity wiring in `base/src/functions/mod.rs`:
- Add enum variant in `Function` if missing.
- Add name lookup mapping in `impl_function_lookup!` if missing.
- Add localized/serialized naming mapping where required in this file.
5. Implement evaluator dispatch in `Model::evaluate_function` in `base/src/functions/mod.rs`.
6. Implement handler logic in the correct module under `base/src/functions/` (or create one if needed).
7. Add or update tests under `base/src/test/` and/or relevant function test modules.
8. Run validation commands that are available in the execution environment.
9. Update tracker row in `specs/reports/lua_backlog_status.csv`:
- `status_impl=complete`
- `status_tests=complete`
- `status_oracle=complete` only if oracle artifacts were actually captured
- `status_done=complete` only when all required fields are complete
- `last_updated=YYYY-MM-DD`
- `notes` with any known parity caveat

## Required File Touchpoints (Typical)
- `base/src/functions/mod.rs`
- `base/src/functions/text.rs` / `base/src/functions/lookup_and_reference.rs` / `base/src/functions/mathematical.rs` / `base/src/functions/statistical/*.rs` (as appropriate)
- `base/src/test/*.rs` (or nearby function-specific test module)
- `specs/reports/lua_backlog_status.csv`

## Definition Of Done (Per Function)
- Function is callable by parser and resolves to a valid `Function` variant.
- Dispatch path reaches a concrete Rust handler.
- Behavior matches Excel/Sheets expectations for core and error cases.
- Tests exist and pass for the new/changed behavior.
- Tracker row is fully updated with concrete date and notes.

## Explicit Non-Goals
- Do not add a standalone Lua execution runtime for these functions.
- Do not edit archive docs for implementation logic.
- Do not mark tracker fields complete without code/test evidence.
