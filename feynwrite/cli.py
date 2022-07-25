import click


help_message = [
    "Print FeynRules file for the multiplets in the Granada dictionary.",
    "Names for the multiplets are as in https://arxiv.org/abs/1711.10391 but without backslashes.",
    "E.g. `feynwrite omega_1 zeta > FeynRulesFile.wl`.",
]


@click.command(help=" ".join(help_message))
@click.option("--as-cowboy", "-c", is_flag=True, help="Greet as a cowboy.")
@click.argument("multiplets", required=False, nargs=-1)
def main(multiplets, as_cowboy):
    """Automate the production of FeynRules files."""
    if not multiplets:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return

    greet = "Howdy" if as_cowboy else "Hello"
    click.echo(f"{greet}, {' '.join(multiplets)}.")
