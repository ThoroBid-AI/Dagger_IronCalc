use ironcalc_base::Model;
use serde::Deserialize;
use std::error::Error;
use std::fs;
use std::path::{Path, PathBuf};

#[derive(Debug, Deserialize)]
struct FixtureInput {
    cell: String,
    value: String,
}

#[derive(Debug, Deserialize)]
#[allow(dead_code)]
struct Fixture {
    engine: String,
    version: String,
    locale: String,
    function: String,
    case_id: String,
    inputs: Vec<FixtureInput>,
    formula: String,
    target: Option<String>,
    expected_text: String,
    #[serde(default)]
    notes: String,
}

#[derive(Debug)]
struct ResultRow {
    fixture_path: String,
    function: String,
    case_id: String,
    engine: String,
    status: String,
    expected: String,
    actual: String,
}

fn collect_json_files(dir: &Path, out: &mut Vec<PathBuf>) -> std::io::Result<()> {
    if !dir.exists() {
        return Ok(());
    }
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        if path.is_dir() {
            collect_json_files(&path, out)?;
        } else if path.extension().and_then(|s| s.to_str()) == Some("json") {
            out.push(path);
        }
    }
    Ok(())
}

fn compare_expected(expected: &str, actual: &str) -> bool {
    if expected == actual {
        return true;
    }
    let expected_num = expected.parse::<f64>();
    let actual_num = actual.parse::<f64>();
    if let (Ok(e), Ok(a)) = (expected_num, actual_num) {
        let abs = (e - a).abs();
        let tol = 1e-12_f64.max(1e-9_f64 * e.abs());
        return abs <= tol;
    }
    false
}

fn parse_cell(
    model: &Model,
    cell_ref: &str,
) -> Result<ironcalc_base::expressions::types::CellReferenceIndex, String> {
    model
        .parse_reference(cell_ref)
        .ok_or_else(|| format!("Invalid cell reference: {cell_ref}"))
}

fn run_fixture(fixture: &Fixture) -> Result<(String, String), String> {
    let mut model = Model::new_empty("fixture", "en", "UTC", "en")
        .map_err(|e| format!("Model init failed: {e}"))?;

    for input in &fixture.inputs {
        let idx = parse_cell(&model, &input.cell)?;
        model
            .set_user_input(idx.sheet, idx.row, idx.column, input.value.clone())
            .map_err(|e| format!("Input set failed ({}) : {e}", input.cell))?;
    }

    let target = fixture
        .target
        .as_deref()
        .unwrap_or("Sheet1!A1");
    let target_idx = parse_cell(&model, target)?;
    model
        .set_user_input(
            target_idx.sheet,
            target_idx.row,
            target_idx.column,
            fixture.formula.clone(),
        )
        .map_err(|e| format!("Formula set failed ({target}): {e}"))?;

    model.evaluate();

    let actual = model
        .get_formatted_cell_value(target_idx.sheet, target_idx.row, target_idx.column)
        .map_err(|e| format!("Read result failed ({target}): {e}"))?;

    Ok((fixture.expected_text.clone(), actual))
}

fn write_report(path: &Path, rows: &[ResultRow]) -> Result<(), Box<dyn Error>> {
    let mut out = String::new();
    out.push_str("fixture_path,function,case_id,engine,status,expected,actual\n");
    for row in rows {
        let line = format!(
            "{},{},{},{},{},{},{}\n",
            row.fixture_path,
            row.function,
            row.case_id,
            row.engine,
            row.status,
            row.expected.replace(',', ""),
            row.actual.replace(',', ""),
        );
        out.push_str(&line);
    }
    fs::write(path, out)?;
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    let mut fixtures_dir = "fixtures".to_string();
    let mut report_path = "specs/reports/conformance_report.csv".to_string();

    let mut args = std::env::args().skip(1);
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--fixtures" => {
                if let Some(val) = args.next() {
                    fixtures_dir = val;
                }
            }
            "--report" => {
                if let Some(val) = args.next() {
                    report_path = val;
                }
            }
            _ => {
                eprintln!("Unknown argument: {arg}");
                return Err("Invalid arguments".into());
            }
        }
    }

    let mut files = Vec::new();
    collect_json_files(Path::new(&fixtures_dir), &mut files)?;
    files.sort();

    if files.is_empty() {
        eprintln!("No fixtures found in {fixtures_dir}");
        return Err("No fixtures found".into());
    }

    let mut rows = Vec::new();
    let mut failures = 0usize;

    for path in files {
        let data = fs::read_to_string(&path)?;
        let fixture: Fixture = serde_json::from_str(&data)?;
        let fixture_path = path.display().to_string();
        match run_fixture(&fixture) {
            Ok((expected, actual)) => {
                let ok = compare_expected(&expected, &actual);
                if !ok {
                    failures += 1;
                }
                rows.push(ResultRow {
                    fixture_path,
                    function: fixture.function.clone(),
                    case_id: fixture.case_id.clone(),
                    engine: fixture.engine.clone(),
                    status: if ok { "OK".to_string() } else { "FAIL".to_string() },
                    expected,
                    actual,
                });
            }
            Err(e) => {
                failures += 1;
                rows.push(ResultRow {
                    fixture_path,
                    function: fixture.function.clone(),
                    case_id: fixture.case_id.clone(),
                    engine: fixture.engine.clone(),
                    status: "ERROR".to_string(),
                    expected: fixture.expected_text.clone(),
                    actual: e,
                });
            }
        }
    }

    let report_path = Path::new(&report_path);
    if let Some(parent) = report_path.parent() {
        fs::create_dir_all(parent)?;
    }
    write_report(report_path, &rows)?;

    let total = rows.len();
    let ok = total.saturating_sub(failures);
    println!("Conformance complete: total={total} ok={ok} failed={failures}");

    if failures > 0 {
        std::process::exit(1);
    }

    Ok(())
}
