#!/usr/bin/env python3

"""Function called for the command-line interface."""

import click

from feynwrite.model import Model
from feynwrite.granada import TERMS

help_message = [
    "Print FeynRules file for the multiplets in the Granada dictionary.",
    "Names for the multiplets are as in https://arxiv.org/abs/1711.10391 but without backslashes.",
    "E.g. `feynwrite omega_1 zeta > FeynRulesFile.wl`.",
]


@click.command(help=" ".join(help_message))
@click.argument("multiplets", required=False, nargs=-1)
@click.option(
    "--mmp-config", is_flag=True, help="Return MatchMakerParser configuration."
)
@click.option(
    "--latex", is_flag=True, help="Output model in LaTeX format."
)
@click.option(
    "-a", is_flag=True, help="Produce output for all valid multiplets."
)
@click.option(
    "--scalars", is_flag=True, help="Produce output for all valid scalars."
)
@click.option(
    "--fermions", is_flag=True, help="Produce output for all valid fermions."
)
def main(multiplets, mmp_config, latex, a, scalars, fermions) -> None:
    """Automate the production of FeynRules files."""

    if not a and not fermions and not scalars and not multiplets:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return

    # Check that multiplets are valid
    valid_multiplets = {
        # Colour-singlet scalars
        "S",
        "S1",
        "S2",
        "varphi",
        "Xi",
        "Xi1",
        "Theta1",
        "Theta3",
        # Colour-triplet scalars
        "omega1",
        "omega2",
        "omega4",
        "Pi1",
        "Pi7",
        "zeta",
        "Omega1",
        "Omega2",
        "Omega4",
        "Upsilon",
        "Phi",
        "N",
        "E",
        "Delta1",
        "Delta3",
        "Sigma",
        "Sigma1",
        "U",
        "D",
        "Q1",
        "Q5",
        "Q7",
        "T1",
        "T2",
    }
    valid_multiplets = {"Granada" + f for f in valid_multiplets}
    model_labels = []

    if scalars:
        multiplets = [
        "S",
        "S1",
        "S2",
        "varphi",
        "Xi",
        "Xi1",
        "Theta1",
        "Theta3",
        "omega1",
        "omega2",
        "omega4",
        "Pi1",
        "Pi7",
        "zeta",
        "Omega1",
        "Omega2",
        "Omega4",
        "Upsilon",
        "Phi",
        ]
    if fermions:
        multiplets = [
        "N",
        "E",
        "Delta1",
        "Delta3",
        "Sigma",
        "Sigma1",
        "U",
        "D",
        "Q1",
        "Q5",
        "Q7",
        "T1",
        "T2",
            ]
    if fermions or scalars:
        multiplets = ["Granada" + f for f in multiplets]

    if a:
        multiplets = valid_multiplets

    for multiplet in multiplets:
        if multiplet not in valid_multiplets:
            raise Exception(
                f"{multiplet} is not a valid multiplet present in the UV dictionary."
            )
        model_labels.append(multiplet)

    # Connect exotic field labels by "_" for name of model
    model_label = "_".join(model_labels)

    # Collect the Lagrangian
    lagrangian = []
    for term in TERMS:
        exotic_labels = [exotic.label for exotic in term.exotics]
        # We only want to include those terms that don't contain other exotics
        for exotic_label in exotic_labels:
            if exotic_label not in multiplets:
                break
        else:
            lagrangian.append(term)

    model = Model(model_label, terms=lagrangian)

    if mmp_config:
        click.echo(model.export_mmp_config())
        return

    if latex:
        click.echo(model.export_latex())
        return

    click.echo(model.export_feynrules())
