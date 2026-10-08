from reconx.engine.pushdown import PushdownTranspiler
from reconx.models.config import Dialect


def test_transpile_count_all_dialects():
    for dialect in [Dialect.POSTGRES, Dialect.SNOWFLAKE, Dialect.DUCKDB, Dialect.ORACLE, Dialect.TSQL]:
        sql = PushdownTranspiler.build_count_query("patients", dialect)
        assert "COUNT" in sql.upper()
        assert "patients" in sql.lower()

def test_transpile_checksum_oracle_and_snowflake():
    cols = ["total_claim_cost", "payer_coverage"]
    sql_ora = PushdownTranspiler.build_checksum_query("encounters", cols, Dialect.ORACLE)
    sql_snow = PushdownTranspiler.build_checksum_query("encounters", cols, Dialect.SNOWFLAKE)
    assert "SUM" in sql_ora.upper()
    assert "SUM" in sql_snow.upper()
