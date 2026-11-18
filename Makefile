.PHONY: help setup run-suite test demo bench clean

help:
	@echo "ReconX Automated Reconciliation Engine Commands:"
	@echo "  make setup      Install dependencies with uv"
	@echo "  make run-suite  Run reconciliation suite across 50+ tables"
	@echo "  make test       Execute test suite (unit and property tests)"
	@echo "  make demo       Launch Streamlit discrepancy audit dashboard"
	@echo "  make bench      Run fault-injection benchmark & bisection study"

setup:
	uv pip install -e ".[dev]"

run-suite:
	python3 -m reconx.cli run --suite suites/clinical_replication_suite.yaml

test:
	pytest -v tests/

demo:
	streamlit run app/streamlit_app.py

bench:
	python3 -m reconx.benchmarks.run_fault_injection

clean:
	rm -rf reports/ .pytest_cache target/
