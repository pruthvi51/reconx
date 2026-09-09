# ADR 0004: Automated Schema Drift Detection

## Status: Accepted
## Context
Upstream DDL mutations silently break replication pipelines.

## Decision
Audit column existence and datatype compatibility prior to table diffing.
