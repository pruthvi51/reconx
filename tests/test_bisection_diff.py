from reconx.engine.bisection import BisectionDiffer

def test_bisection_diff_exact_match():
    differ = BisectionDiffer(key_col="id", compare_cols=["name", "amount"])
    rows1 = [{"id": 1, "name": "A", "amount": 100}, {"id": 2, "name": "B", "amount": 200}]
    rows2 = [{"id": 1, "name": "A", "amount": 100}, {"id": 2, "name": "B", "amount": 200}]
    res = differ.diff_slices(rows1, rows2)
    assert res["matched_count"] == 2
    assert res["mismatched_count"] == 0
    assert res["match_rate_pct"] == 100.0

def test_bisection_diff_with_mismatch_and_missing():
    differ = BisectionDiffer(key_col="id", compare_cols=["name", "amount"])
    rows1 = [{"id": 1, "name": "A", "amount": 100}, {"id": 2, "name": "B", "amount": 200}, {"id": 3, "name": "C", "amount": 300}]
    rows2 = [{"id": 1, "name": "A", "amount": 100}, {"id": 2, "name": "B", "amount": 205}, {"id": 4, "name": "D", "amount": 400}]
    res = differ.diff_slices(rows1, rows2)
    assert res["matched_count"] == 1
    assert res["mismatched_count"] == 1 # id 2 has different amount
    assert res["missing_in_target_count"] == 1 # id 3
    assert res["extra_in_target_count"] == 1 # id 4
