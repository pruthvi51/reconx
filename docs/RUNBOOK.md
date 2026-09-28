# ReconX Operations Runbook

## 1. Running a Reconciliation Audit
`reconx run --suite suites/clinical_replication_suite.yaml`

## 2. Investigating Mismatched Rows
1. Open Streamlit Dashboard: `make demo`.
2. Select target table in Discrepancy Attribution Explorer.
3. Review attribute delta breakdown and download CSV audit manifest.
