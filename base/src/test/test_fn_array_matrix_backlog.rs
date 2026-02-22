#![allow(clippy::unwrap_used)]

use crate::test::util::new_empty_model;

#[test]
fn spill_literal_array_and_obstruction() {
    let mut model = new_empty_model();
    model._set("A1", "={1,2;3,4}");
    model.evaluate();

    assert_eq!(model._get_text("A1"), *"1");
    assert_eq!(model._get_text("B1"), *"2");
    assert_eq!(model._get_text("A2"), *"3");
    assert_eq!(model._get_text("B2"), *"4");

    model._set("D1", "99");
    model._set("C1", "={1,2}");
    model.evaluate();

    assert_eq!(model._get_text("C1"), *"#SPILL!");
    assert_eq!(model._get_text("D1"), *"99");
}

#[test]
fn transpose_spill_dependency() {
    let mut model = new_empty_model();
    model._set("A1", "=B3");
    model._set("B1", "=TRANSPOSE({1,2,3})");
    model.evaluate();

    assert_eq!(model._get_text("B1"), *"1");
    assert_eq!(model._get_text("B2"), *"2");
    assert_eq!(model._get_text("B3"), *"3");
    assert_eq!(model._get_text("A1"), *"3");
}

#[test]
fn array_backlog_functions() {
    let mut model = new_empty_model();

    model._set("C1", "1");
    model._set("C2", "2");
    model._set("C3", "3");
    model._set("A1", "=ARRAYFORMULA(C1:C3*2)");
    model._set("A5", "=INDEX(ARRAYFORMULA(C1:C3*2),3,1)");

    model._set("E1", "=ARRAY_CONSTRAIN({1,2;3,4;5,6},2,1)");
    model._set("E5", "=INDEX(ARRAY_CONSTRAIN({1,2;3,4;5,6},2,1),2,1)");

    model._set("G1", "=FILTER({1,2;3,4;5,6},{TRUE;FALSE;TRUE})");
    model._set("G5", "=INDEX(FILTER({1,2;3,4;5,6},{TRUE;FALSE;TRUE}),2,2)");
    model._set("J1", "=FILTER({1,2;3,4;5,6},{TRUE,FALSE})");
    model._set("T1", "=FILTER({1,2},{FALSE,FALSE})");
    model._set("T2", "=FILTER({1,2},{FALSE,FALSE},\"none\")");

    model._set("L1", "=MMULT({1,2;3,4},{5,6;7,8})");
    model._set("L5", "=INDEX(MMULT({1,2;3,4},{5,6;7,8}),2,2)");

    model._set("O1", "=SPLIT(\"a,b,,c\",\",\",TRUE,FALSE)");
    model._set("O5", "=INDEX(SPLIT(\"a,b,,c\",\",\",TRUE,FALSE),1,4)");
    model._set("O2", "=SPLIT(\"a,b,,c\",\",\")");

    model._set("R5", "=INDEX(TRANSPOSE({1,2;3,4}),2,1)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"2");
    assert_eq!(model._get_text("A2"), *"4");
    assert_eq!(model._get_text("A3"), *"6");
    assert_eq!(model._get_text("A5"), *"6");

    assert_eq!(model._get_text("E1"), *"1");
    assert_eq!(model._get_text("E2"), *"3");
    assert_eq!(model._get_text("E5"), *"3");

    assert_eq!(model._get_text("G1"), *"1");
    assert_eq!(model._get_text("H1"), *"2");
    assert_eq!(model._get_text("G2"), *"5");
    assert_eq!(model._get_text("H2"), *"6");
    assert_eq!(model._get_text("G5"), *"6");

    assert_eq!(model._get_text("J1"), *"1");
    assert_eq!(model._get_text("J2"), *"3");
    assert_eq!(model._get_text("J3"), *"5");

    assert_eq!(model._get_text("T1"), *"#N/A");
    assert_eq!(model._get_text("T2"), *"none");

    assert_eq!(model._get_text("L1"), *"19");
    assert_eq!(model._get_text("M1"), *"22");
    assert_eq!(model._get_text("L2"), *"43");
    assert_eq!(model._get_text("M2"), *"50");
    assert_eq!(model._get_text("L5"), *"50");

    assert_eq!(model._get_text("O1"), *"a");
    assert_eq!(model._get_text("P1"), *"b");
    assert_eq!(model._get_text("Q1"), *"");
    assert_eq!(model._get_text("R1"), *"c");
    assert_eq!(model._get_text("O5"), *"c");

    assert_eq!(model._get_text("O2"), *"a");
    assert_eq!(model._get_text("P2"), *"b");
    assert_eq!(model._get_text("Q2"), *"c");

    assert_eq!(model._get_text("R5"), *"2");
}

#[test]
fn sheets_array_aliases_return_full_arrays() {
    let mut model = new_empty_model();

    model._set("A1", "=SEQUENCE(2,3,10,2)");
    model._set("E1", "=SCAN(10,{1,2;3,4})");
    model._set("I1", "=SORT({3,9;1,8;2,7})");
    model._set("L1", "=SORTN({3,9;1,8;2,7},2,0,1,TRUE)");
    model._set("N1", "=TOCOL({1,2;3,4})");
    model._set("P1", "=TOROW({1,2;3,4},0,TRUE)");

    model.evaluate();

    assert_eq!(model._get_text("A1"), *"10");
    assert_eq!(model._get_text("B1"), *"12");
    assert_eq!(model._get_text("C1"), *"14");
    assert_eq!(model._get_text("A2"), *"16");
    assert_eq!(model._get_text("B2"), *"18");
    assert_eq!(model._get_text("C2"), *"20");

    assert_eq!(model._get_text("E1"), *"11");
    assert_eq!(model._get_text("F1"), *"13");
    assert_eq!(model._get_text("E2"), *"16");
    assert_eq!(model._get_text("F2"), *"20");

    assert_eq!(model._get_text("I1"), *"1");
    assert_eq!(model._get_text("J1"), *"8");
    assert_eq!(model._get_text("I2"), *"2");
    assert_eq!(model._get_text("J2"), *"7");
    assert_eq!(model._get_text("I3"), *"3");
    assert_eq!(model._get_text("J3"), *"9");

    assert_eq!(model._get_text("L1"), *"1");
    assert_eq!(model._get_text("M1"), *"8");
    assert_eq!(model._get_text("L2"), *"2");
    assert_eq!(model._get_text("M2"), *"7");

    assert_eq!(model._get_text("N1"), *"1");
    assert_eq!(model._get_text("N2"), *"2");
    assert_eq!(model._get_text("N3"), *"3");
    assert_eq!(model._get_text("N4"), *"4");

    assert_eq!(model._get_text("P1"), *"1");
    assert_eq!(model._get_text("Q1"), *"3");
    assert_eq!(model._get_text("R1"), *"2");
    assert_eq!(model._get_text("S1"), *"4");
}
