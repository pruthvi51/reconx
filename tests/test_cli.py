from click.testing import CliRunner
from reconx.cli import cli

def test_cli_run():
    runner = CliRunner()
    res = runner.invoke(cli, ["run", "--suite", "suites/clinical_replication_suite.yaml"])
    assert res.exit_code == 0
    assert "Audited 4 core clinical tables" in res.output

def test_cli_bench():
    runner = CliRunner()
    res = runner.invoke(cli, ["bench"])
    assert res.exit_code == 0
    assert "Benchmark Results" in res.output
