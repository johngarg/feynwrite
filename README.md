# FeynWrite

Automate the production of FeynRules files.

Currently the library defines a simple domain-specific language related to
writing down terms in the Lagrangian, which are then exported to the FeynRules
format. This provides a number of advantages:
- Reduces boilerplate code often present in FeynRules model files
- Allows various checks to be done that guarantee the validity of the exported file
- Defines an extensible and (arguably) simpler input for the terms
- Allows the `.symm` and `.gauge` files required by `matchmakereft` to be produced automatically for a given model
- Facilitates exporting to another format (*e.g.* Matchete, LaTeX)
- Sets the stage for automating the definition of these terms


# Installation

If you don't use `pipx`, you're missing out.
Here are [installation instructions](https://github.com/pypa/pipx#readme)

Simply run:

    $ pipx install .

# Lagrangian

Modifications to the common Lagrangian can be made in the `granada.py` file. Important notes:
- Spinors with contracted indices should be written next to each other
- Adjoint SU(2) indices should be written in the opposite position to where they are if they are conjugated, since the conjugation function swaps the index position

# Usage

To use it:

    $ feynwrite [MULTIPLET]...
    
For help:

    $ feynwrite --help
