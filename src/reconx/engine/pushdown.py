"""
SQLGlot Pushdown Transpiler:
Transpiles universal verification ASTs across 5 dialects:
Postgres, Snowflake, DuckDB, Oracle, T-SQL.
"""
import sqlglot
from sqlglot import exp
from typing import List
from reconx.models.config import Dialect

class PushdownTranspiler:
    @staticmethod
    def build_count_query(table_name: str, dialect: Dialect) -> str:
        expression = exp.select(exp.Count(this=exp.Star()).as_("row_count")).from_(table_name)
        return expression.sql(dialect.value)

    @staticmethod
    def build_checksum_query(table_name: str, columns: List[str], dialect: Dialect) -> str:
        select_exprs = [exp.Count(this=exp.Star()).as_("total_rows")]
        for col in columns:
            select_exprs.append(exp.Sum(this=exp.column(col)).as_(f"sum_{col}"))
            select_exprs.append(exp.Count(this=exp.column(col)).as_(f"cnt_{col}"))
            select_exprs.append(exp.Min(this=exp.column(col)).as_(f"min_{col}"))
            select_exprs.append(exp.Max(this=exp.column(col)).as_(f"max_{col}"))
        query = exp.select(*select_exprs).from_(table_name)
        return query.sql(dialect.value)

    @staticmethod
    def build_row_hash_slice_query(
        table_name: str,
        hash_expr: str,
        slice_idx: int,
        total_slices: int,
        dialect: Dialect
    ) -> str:
        query = (
            exp.select(
                exp.Count(this=exp.Star()).as_("slice_count"),
                exp.Sum(this=exp.column("row_hash")).as_("slice_hash_sum")
            )
            .from_(table_name)
            .where(f"abs(hash_slice_bucket) % {total_slices} = {slice_idx}")
        )
        return query.sql(dialect.value)
