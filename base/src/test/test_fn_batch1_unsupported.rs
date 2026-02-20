#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn test_batch1_unsupported_functions_return_nimpl() {
    let mut model = new_empty_model();
    let functions = [
        "ACCRINT",
        "ACCRINTM",
        "ADDRESS",
        "AGGREGATE",
        "AMORDEGRC",
        "AMORLINC",
        "ARRAY_CONSTRAIN",
        "ASC",
        "AVERAGE.WEIGHTED",
        "BAHTTEXT",
    ];

    for (idx, function) in functions.iter().enumerate() {
        let cell = format!("A{}", idx + 1);
        model._set(&cell, &format!("={function}(1)"));
    }
    model.evaluate();

    for row in 1..=functions.len() as i32 {
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

#[test]
fn test_add_fallback_uses_sum() {
    let mut model = new_empty_model();
    model._set("A1", "=ADD(1,2,3)");
    model._set("A2", "=ADD(1)");
    model.evaluate();

    assert_eq!(model._get_text("A1"), *"6");
    assert_eq!(model._get_text("A2"), *"#ERROR!");
}

#[test]
fn test_betainvn_alias_to_betainv() {
    let mut model = new_empty_model();
    model._set("A1", "=BETA.INVN(0.5, 2, 2, 0, 1)");
    model._set("A2", "=BETAINVN(0.5, 2, 2, 0, 1)");
    model.evaluate();

    assert_eq!(model._get_text("A1"), *"0.5");
    assert_eq!(model._get_text("A2"), *"0.5");
}

#[test]
fn test_arrayformula_passthrough() {
    let mut model = new_empty_model();
    model._set("A1", "=ARRAYFORMULA(1+2)");
    model._set("A2", "=ARRAYFORMULA(1)");
    model.evaluate();

    assert_eq!(model._get_text("A1"), *"3");
    assert_eq!(model._get_text("A2"), *"1");
}

#[test]
fn test_areas_returns_one_for_simple_reference() {
    let mut model = new_empty_model();
    model._set("A1", "1");
    model._set("A2", "2");
    model._set("A3", "=AREAS(A1:A2)");
    model.evaluate();

    assert_eq!(model._get_text("A3"), *"1");
}
