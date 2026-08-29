# ADR 0003: PySpark Distributed Joins for Large Tables

## Status: Accepted
## Context
Datasets with >1M rows exceed single-node memory and benefit from distributed computing.

## Decision
Delegate large table comparisons to PySpark hash-partitioned full outer joins with salted keys.
