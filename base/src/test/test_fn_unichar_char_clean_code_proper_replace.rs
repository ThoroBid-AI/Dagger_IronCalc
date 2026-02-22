#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn text_backlog_happy_path() {
    let mut model = new_empty_model();
    model._set("A1", "=CHAR(65)");
    model._set("A2", "=CLEAN(\"A\"&CHAR(9)&\"B\"&CHAR(10))");
    model._set("A3", "=CODE(\"A\")");
    model._set("A4", "=PROPER(\"hELLO, wORLD-2026\")");
    model._set("A5", "=PROPER(\"o'CONNOR\")");
    model._set("A6", "=REPLACE(\"abcdef\",2,3,\"Z\")");
    model._set("A7", "=REPLACE(\"abc\",5,2,\"z\")");
    model._set("A8", "=UNICHAR(9731)");
    model._set("A9", "=_xlfn.UNICHAR(65)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"A");
    assert_eq!(model._get_text("A2"), *"AB");
    assert_eq!(model._get_text("A3"), *"65");
    assert_eq!(model._get_text("A4"), *"Hello, World-2026");
    assert_eq!(model._get_text("A5"), *"O'Connor");
    assert_eq!(model._get_text("A6"), *"aZef");
    assert_eq!(model._get_text("A7"), *"abcz");
    assert_eq!(model._get_text("A8"), *"☃");
    assert_eq!(model._get_text("A9"), *"A");
}

#[test]
fn text_backlog_error_cases() {
    let mut model = new_empty_model();
    model._set("A1", "=CHAR(0)");
    model._set("A2", "=UNICHAR(0)");
    model._set("A3", "=CODE(\"\")");
    model._set("A4", "=REPLACE(\"abc\",0,1,\"x\")");
    model._set("A5", "=REPLACE(\"abc\",2,-1,\"x\")");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#NUM!");
    assert_eq!(model._get_text("A2"), *"#VALUE!");
    assert_eq!(model._get_text("A3"), *"#VALUE!");
    assert_eq!(model._get_text("A4"), *"#VALUE!");
    assert_eq!(model._get_text("A5"), *"#VALUE!");
}

#[test]
fn text_backlog_wrong_number_of_arguments() {
    let mut model = new_empty_model();
    model._set("A1", "=CHAR()");
    model._set("A2", "=CLEAN(\"A\",\"B\")");
    model._set("A3", "=CODE()");
    model._set("A4", "=PROPER()");
    model._set("A5", "=REPLACE(\"a\",1,1)");
    model._set("A6", "=UNICHAR(65,66)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#ERROR!");
    assert_eq!(model._get_text("A2"), *"#N/A");
    assert_eq!(model._get_text("A3"), *"#ERROR!");
    assert_eq!(model._get_text("A4"), *"#N/A");
    assert_eq!(model._get_text("A5"), *"#ERROR!");
    assert_eq!(model._get_text("A6"), *"#ERROR!");
}
