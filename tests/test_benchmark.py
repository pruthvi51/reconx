from reconx.benchmarks.run_fault_injection import run_benchmark


def test_fault_injection_benchmark():
    res = run_benchmark()
    assert res["dataset_rows"] == 50000
    assert res["detected_mismatches"] == 5
    assert res["detected_missing"] == 5
    assert res["precision_pct"] == 100.0
    assert res["recall_pct"] == 100.0
