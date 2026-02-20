#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn test_batch1_unsupported_functions_return_nimpl() {
    let mut model = new_empty_model();
    let functions = ["ACCRINT", "ACCRINTM", "AVERAGE.WEIGHTED", "BETA.INVN"];

    for (idx, function) in functions.iter().enumerate() {
        let cell = format!("A{}", idx + 1);
        model._set(&cell, &format!("={function}(1)"));
    }
    model.evaluate();

    for row in 1..=4 {
        let cell = format!("A{row}");
        assert_eq!(model._get_text(&cell), *"#N/IMPL!");
    }
}

#[test]
fn test_unknown_function_returns_name_error() {
    let mut model = new_empty_model();
    model._set("A1", "=NOT_A_FUNCTION(1)");
    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#NAME?");
}
