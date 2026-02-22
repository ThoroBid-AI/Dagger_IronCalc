#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn address_and_hyperlink_happy_path() {
    let mut model = new_empty_model();
    model._set("A1", "=ADDRESS(2,3)");
    model._set("A2", "=ADDRESS(2,3,2)");
    model._set("A3", "=ADDRESS(2,3,3)");
    model._set("A4", "=ADDRESS(2,3,4)");
    model._set("A5", "=ADDRESS(2,3,1,FALSE)");
    model._set("A6", "=ADDRESS(2,3,2,FALSE)");
    model._set("A7", "=ADDRESS(2,3,3,FALSE)");
    model._set("A8", "=ADDRESS(2,3,4,FALSE,\"Sheet 1\")");
    model._set("A9", "=HYPERLINK(\"https://ironcalc.com\")");
    model._set("A10", "=HYPERLINK(\"https://ironcalc.com\",\"IronCalc\")");
    model._set("A11", "=HYPERLINK(\"https://ironcalc.com\",123)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"$C$2");
    assert_eq!(model._get_text("A2"), *"C$2");
    assert_eq!(model._get_text("A3"), *"$C2");
    assert_eq!(model._get_text("A4"), *"C2");
    assert_eq!(model._get_text("A5"), *"R2C3");
    assert_eq!(model._get_text("A6"), *"R2C[3]");
    assert_eq!(model._get_text("A7"), *"R[2]C3");
    assert_eq!(model._get_text("A8"), *"'Sheet 1'!R[2]C[3]");
    assert_eq!(model._get_text("A9"), *"https://ironcalc.com");
    assert_eq!(model._get_text("A10"), *"IronCalc");
    assert_eq!(model._get_text("A11"), *"123");
}

#[test]
fn address_and_hyperlink_error_cases() {
    let mut model = new_empty_model();
    model._set("A1", "=ADDRESS(0,1)");
    model._set("A2", "=ADDRESS(1,0)");
    model._set("A3", "=ADDRESS(1,1,5)");
    model._set("A4", "=HYPERLINK()");
    model._set("A5", "=HYPERLINK(\"x\",#REF!)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"#VALUE!");
    assert_eq!(model._get_text("A2"), *"#VALUE!");
    assert_eq!(model._get_text("A3"), *"#NUM!");
    assert_eq!(model._get_text("A4"), *"#N/A");
    assert_eq!(model._get_text("A5"), *"#REF!");
}
