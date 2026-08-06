from reconx.spark.diff_engine import create_recon_spark_session, reconcile_large_tables

def test_pyspark_reconciliation():
    spark = create_recon_spark_session()
    src_data = [(1, "A", 10.0), (2, "B", 20.0), (3, "C", 30.0)]
    tgt_data = [(1, "A", 10.0), (2, "B", 25.0), (4, "D", 40.0)]

    src_df = spark.createDataFrame(src_data, ["id", "code", "amount"])
    tgt_df = spark.createDataFrame(tgt_data, ["id", "code", "amount"])

    res = reconcile_large_tables(spark, src_df, tgt_df, "id", ["code", "amount"])
    assert res["matched"] == 1 # id 1
    assert res["mismatched"] == 1 # id 2
    assert res["missing_in_target"] == 1 # id 3
    assert res["extra_in_target"] == 1 # id 4
    assert res["total_records"] == 4
