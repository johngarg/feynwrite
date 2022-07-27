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
def main(multiplets) -> None:
    """Automate the production of FeynRules files."""

    # For a naked call, print help
    if not multiplets:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return

    # Check that multiplets are valid
    valid_multiplets = {"S", "S1", "S2", "varphi"}
    model_labels = []
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
    click.echo(model.export())
