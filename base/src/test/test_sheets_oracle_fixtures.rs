#![allow(clippy::unwrap_used)]
#![allow(clippy::panic)]

use std::fs;
use std::path::{Path, PathBuf};

use serde::Deserialize;

use crate::{cell::CellValue, model::Model};

#[derive(Deserialize)]
struct FixtureInput {
    cell: String,
    value: String,
}

#[derive(Deserialize)]
struct Fixture {
    engine: String,
    function: String,
    case_id: String,
    inputs: Vec<FixtureInput>,
    formula: String,
    target: String,
    expected_text: String,
}

fn fixtures_root() -> PathBuf {
    let candidates = [PathBuf::from("../fixtures"), PathBuf::from("fixtures")];
    for candidate in candidates {
        if candidate.exists() {
            return candidate;
        }
    }
    panic!("Could not find fixtures directory");
}

fn collect_sheet_fixtures(root: &Path) -> Vec<PathBuf> {
    let mut files = Vec::new();
    if let Ok(function_dirs) = fs::read_dir(root) {
        for function_dir in function_dirs.flatten() {
            let path = function_dir.path();
            if !path.is_dir() {
                continue;
            }
            if let Ok(entries) = fs::read_dir(path) {
                for entry in entries.flatten() {
                    let file = entry.path();
                    if file.extension().and_then(|ext| ext.to_str()) != Some("json") {
                        continue;
                    }
                    if file
                        .file_name()
                        .and_then(|name| name.to_str())
                        .unwrap_or_default()
                        .ends_with("_sheets.json")
                    {
                        files.push(file);
                    }
                }
            }
        }
    }
    files.sort();
    files
}

fn values_match(expected_text: &str, value: &CellValue, formatted: &str) -> bool {
    fn approx_eq(a: f64, b: f64) -> bool {
        let abs_diff = (a - b).abs();
        let scale = a.abs().max(b.abs()).max(1.0);
        abs_diff <= 1e-8 * scale
    }

    fn parse_complex(text: &str) -> Option<(f64, f64)> {
        if !text.ends_with('i') {
            return None;
        }
        let body = &text[..text.len() - 1];
        let mut split_at = None;
        for (idx, ch) in body.char_indices().skip(1) {
            if ch == '+' || ch == '-' {
                split_at = Some(idx);
            }
        }
        let idx = split_at?;
        let (real_s, imag_s) = body.split_at(idx);
        let real = real_s.parse::<f64>().ok()?;
        let imag = imag_s.parse::<f64>().ok()?;
        Some((real, imag))
    }

    if expected_text == formatted {
        return true;
    }
    match value {
        CellValue::Number(number) => expected_text
            .parse::<f64>()
            .map(|v| approx_eq(v, *number))
            .unwrap_or(false),
        CellValue::Boolean(boolean) => {
            let expected = expected_text.to_uppercase();
            (*boolean && expected == "TRUE") || (!*boolean && expected == "FALSE")
        }
        CellValue::String(text) => {
            if expected_text == text {
                true
            } else if let (Some((er, ei)), Some((ar, ai))) =
                (parse_complex(expected_text), parse_complex(text))
            {
                approx_eq(er, ar) && approx_eq(ei, ai)
            } else {
                false
            }
        }
        CellValue::None => expected_text.is_empty(),
    }
}

#[test]
fn sheets_oracle_fixtures_match_ironcalc() {
    let root = fixtures_root();
    let fixture_files = collect_sheet_fixtures(&root);
    assert!(
        !fixture_files.is_empty(),
        "No *_sheets.json fixtures found in {}",
        root.display()
    );

    let mut checked = 0;
    let mut mismatches = Vec::new();

    for fixture_file in fixture_files {
        let raw = fs::read_to_string(&fixture_file).unwrap();
        let fixture: Fixture = serde_json::from_str(&raw).unwrap();
        if fixture.engine != "sheets" || fixture.expected_text.is_empty() {
            continue;
        }
        let mut model = Model::new_empty("oracle", "en", "UTC", "en").unwrap();

        for input in &fixture.inputs {
            let reference = model.parse_reference(&input.cell).unwrap_or_else(|| {
                panic!("Invalid input cell in fixture {}", fixture_file.display())
            });
            model
                .set_user_input(
                    reference.sheet,
                    reference.row,
                    reference.column,
                    input.value.clone(),
                )
                .unwrap();
        }

        let target = model
            .parse_reference(&fixture.target)
            .unwrap_or_else(|| panic!("Invalid target in fixture {}", fixture_file.display()));
        model
            .set_user_input(
                target.sheet,
                target.row,
                target.column,
                fixture.formula.clone(),
            )
            .unwrap();
        model.evaluate();

        let value = model
            .get_cell_value_by_index(target.sheet, target.row, target.column)
            .unwrap();
        let formatted = model
            .get_formatted_cell_value(target.sheet, target.row, target.column)
            .unwrap();

        checked += 1;
        if !values_match(&fixture.expected_text, &value, &formatted) {
            mismatches.push(format!(
                "{} ({}::{}) expected='{}' got_formatted='{}' got_value={:?}",
                fixture_file.display(),
                fixture.function,
                fixture.case_id,
                fixture.expected_text,
                formatted,
                value
            ));
        }
    }

    assert!(
        checked > 0,
        "No sheets fixtures with expected_text were checked"
    );
    assert!(
        mismatches.is_empty(),
        "Sheets oracle mismatches:\n{}",
        mismatches.join("\n")
    );
}
