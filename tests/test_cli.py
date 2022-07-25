import pytest
import click
from click.testing import CliRunner
from feynwrite import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ["John"])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == "Hello, John."
