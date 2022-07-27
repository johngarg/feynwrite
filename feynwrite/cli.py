import click

from feynwrite.model import Model
from feynwrite.granada import TERMS

help_message = [
    "Print FeynRules file for the multiplets in the Granada dictionary.",
    "Names for the multiplets are as in https://arxiv.org/abs/1711.10391 but without backslashes.",
    "E.g. `feynwrite omega_1 zeta > FeynRulesFile.wl`.",
]


@click.command(help=" ".join(help_message))
# @click.option("--as-cowboy", "-c", is_flag=True, help="Greet as a cowboy.")
@click.argument("multiplets", required=False, nargs=-1)
def main(multiplets):
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

    model_label = "_".join(model_labels)

    # Collect the Lagrangian
    lagrangian = []
    for term in TERMS:
        exotic_labels = [exotic.label for exotic in term.exotics]
        all_present = all([multiplet in exotic_labels for multiplet in multiplets])
        if all_present:
            lagrangian.append(term)

    model = Model(model_label, terms=lagrangian)
    click.echo(model.export())
