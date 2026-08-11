from reconx.engine.schema_drift import SchemaDriftDetector

def test_no_drift():
    s1 = {"id": "int", "name": "varchar"}
    s2 = {"id": "int", "name": "varchar"}
    res = SchemaDriftDetector.detect_drift(s1, s2)
    assert res["has_drift"] is False

def test_detected_drift():
    s1 = {"id": "int", "name": "varchar", "old_col": "float"}
    s2 = {"id": "bigint", "name": "varchar", "new_col": "date"}
    res = SchemaDriftDetector.detect_drift(s1, s2)
    assert res["has_drift"] is True
    assert "old_col" in res["dropped_columns"]
    assert "new_col" in res["added_columns"]
    assert len(res["type_mismatches"]) == 1 # int vs bigint
