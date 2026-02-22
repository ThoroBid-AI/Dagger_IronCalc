#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn backlog_math_financial_happy_path() {
    let mut model = new_empty_model();
    model._set("A1", "=FVSCHEDULE(1000,{0.02,0.03})");
    model._set("A2", "=MULTINOMIAL(1,2,3)");
    model._set("A3", "=SERIESSUM(2,1,2,{1,2,3})");
    model._set("A4", "=SUMPRODUCT({1,2,3},{4,5,6})");
    model._set("A5", "=CRITBINOM(10,0.5,0.75)");

    model._set("B1", "2");
    model._set("B2", "3");
    model._set("B3", "4");
    model._set("C1", "5");
    model._set("C2", "6");
    model._set("C3", "7");
    model._set("A6", "=SUMPRODUCT(B1:B3,C1:C3)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"1050.6");
    assert_eq!(model._get_text("A2"), *"60");
    assert_eq!(model._get_text("A3"), *"114");
    assert_eq!(model._get_text("A4"), *"32");
    assert_eq!(model._get_text("A5"), *"6");
    assert_eq!(model._get_text("A6"), *"56");
}

#[test]
fn backlog_math_financial_error_cases() {
    let mut model = new_empty_model();
    model._set("A1", "=FVSCHEDULE(1000,{0.02,\"x\"})");
    model._set("A2", "=MULTINOMIAL(1,-2,3)");
    model._set("A3", "=SERIESSUM(1,1,1,{1,\"x\"})");
    model._set("A4", "=SUMPRODUCT({1,2},{3,4,5})");
    model._set("A5", "=CRITBINOM(10,1.5,0.75)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#VALUE!");
    assert_eq!(model._get_text("A2"), *"#NUM!");
    assert_eq!(model._get_text("A3"), *"#VALUE!");
    assert_eq!(model._get_text("A4"), *"#VALUE!");
    assert_eq!(model._get_text("A5"), *"#NUM!");
}

#[test]
fn backlog_math_financial_wrong_number_of_arguments() {
    let mut model = new_empty_model();
    model._set("A1", "=FVSCHEDULE(1000)");
    model._set("A2", "=MULTINOMIAL()");
    model._set("A3", "=SERIESSUM(1,1,1)");
    model._set("A4", "=SUMPRODUCT()");
    model._set("A5", "=CRITBINOM(1,2)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#ERROR!");
    assert_eq!(model._get_text("A2"), *"#ERROR!");
    assert_eq!(model._get_text("A3"), *"#ERROR!");
    assert_eq!(model._get_text("A4"), *"#ERROR!");
    assert_eq!(model._get_text("A5"), *"#ERROR!");
}
