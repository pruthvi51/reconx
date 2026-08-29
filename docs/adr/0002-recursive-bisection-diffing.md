# ADR 0002: Recursive Bisection Row-Hash Diffing

## Status: Accepted
## Context
Comparing row-by-row over high-latency database connections is computationally infeasible.

## Decision
Execute segmented row-hash bisection in O(log N) queries to isolate exact discrepant keys.
