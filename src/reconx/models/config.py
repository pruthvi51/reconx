"""
Pydantic v2 schemas for Reconciliation Suites, Tolerances, and Results.
"""
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class Dialect(str, Enum):
    POSTGRES = "postgres"
    SNOWFLAKE = "snowflake"
    DUCKDB = "duckdb"
    ORACLE = "oracle"
    TSQL = "tsql"

class ToleranceConfig(BaseModel):
    numeric_epsilon: float = 1e-4
    timestamp_truncate: str = "second"
    ignore_whitespace: bool = True
    ignore_case: bool = False
    null_equals_empty_string: bool = True

class TablePairConfig(BaseModel):
    source_table: str
    target_table: str
    primary_keys: List[str]
    compare_columns: Optional[List[str]] = None
    exclude_columns: List[str] = Field(default_factory=list)
    tolerances: ToleranceConfig = Field(default_factory=ToleranceConfig)
    use_spark_threshold: int = 1_000_000

class ReconSuiteConfig(BaseModel):
    suite_name: str
    description: str
    source_dialect: Dialect
    target_dialect: Dialect
    tables: List[TablePairConfig]
