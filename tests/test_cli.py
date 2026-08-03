import pytest
import click
from click.testing import CliRunner
from feynwrite import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ["Q"])
    assert result.exception
    assert result.exit_code != 0
    # assert result.output.strip() == "Hello, John."


def test_bfm_replacement_excludes_already_split_terms(runner):
    result = runner.invoke(cli.main, ["Granadavarphi"])

    assert result.exit_code == 0
    l_tot = next(
        line for line in result.output.splitlines() if line.startswith("Ltot :=")
    )
    already_split, interaction_terms = l_tot.split(" + ((", maxsplit=1)

    assert already_split == "Ltot := LSM + LFreeGranadavarphi"
    assert interaction_terms.endswith(") /. gotoBFM);")
    assert "LSM" not in interaction_terms
    assert "LFreeGranadavarphi" not in interaction_terms


def test_bfm_replacement_includes_vector_interactions(runner):
    result = runner.invoke(cli.main, ["GranadaVL1"])

    assert result.exit_code == 0
    l_tot = next(
        line for line in result.output.splitlines() if line.startswith("Ltot :=")
    )
    already_split, interaction_terms = l_tot.split(" + ((", maxsplit=1)

    assert already_split == "Ltot := LSM + LFreeGranadaVL1"
    assert "LgBVL1" in interaction_terms
    assert "LgWVL1" in interaction_terms
    assert interaction_terms.endswith(") /. gotoBFM);")
