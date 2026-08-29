# ADR 0001: SQLGlot Cross-Dialect Pushdown Transpiler

## Status: Accepted
## Context
Validating across Oracle, Snowflake, Postgres, DuckDB, and T-SQL requires engine-specific pushdown logic.

## Decision
Use SQLGlot to generate universal ASTs and transpile natively to each target dialect.
