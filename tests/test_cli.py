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


def test_varphi_prime_prime_interaction(runner):
    result = runner.invoke(cli.main, ["Granadavarphi"])

    assert result.exit_code == 0
    assert "LlambdaHatPrimePrimevarphi :=" in result.output
    assert (
        "lambdaHatPrimePrimevarphi anti[Phi][i0] Granadavarphi[i0] "
        "anti[Phi][i1] Granadavarphi[i1]" in result.output
    )
    assert "HC[LlambdaHatPrimePrimevarphi]" in result.output


def test_varphi_prime_prime_mmp_config(runner):
    result = runner.invoke(cli.main, ["Granadavarphi", "--mmp-config"])

    assert result.exit_code == 0
    assert "lambdaHatPrimePrimevarphi" in result.output
    assert "lambdaHatPrimePrimevarphibar" in result.output
