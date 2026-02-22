#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn countunique_happy_path() {
    let mut model = new_empty_model();
    model._set("A1", "=COUNTUNIQUE(1,1,2,3)");
    model._set("A2", "=COUNTUNIQUE(TRUE,TRUE,FALSE)");
    model._set("A3", "=COUNTUNIQUE(\"a\",\"a\",\"b\")");

    model._set("B1", "1");
    model._set("B2", "1");
    model._set("B3", "2");
    model._set("B4", "3");
    model._set("B5", "3");
    model._set("A4", "=COUNTUNIQUE(B1:B5)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"3");
    assert_eq!(model._get_text("A2"), *"2");
    assert_eq!(model._get_text("A3"), *"2");
    assert_eq!(model._get_text("A4"), *"3");
}

#[test]
fn countunique_error_cases() {
    let mut model = new_empty_model();
    model._set("A1", "=COUNTUNIQUE()");
    model._set("A2", "=COUNTUNIQUE(#REF!,1)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#ERROR!");
    assert_eq!(model._get_text("A2"), *"#REF!");
}
