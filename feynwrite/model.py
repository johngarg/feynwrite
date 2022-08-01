#!/usr/bin/env python3

"""File that contains the Model class for generating the Mathematica code that
will enter the FeynRules output.

"""

# Depends on: tensor.py

from typing import List, Set
from dataclasses import dataclass
from datetime import datetime

from feynwrite.tensor import TensorProduct, Field, Coupling
from feynwrite.utils import format_wolfram_list


@dataclass
class Model:
    """A model contains a list of `TensorProduct` objects representing terms in the
    interaction Lagrangian. Models should have a `name` that is written to the
    FeynRules file.

    The main role of the class is to provide the `export` method, which prints
    the FeynRules file associated with the model.

    """

    def __init__(self, name: str, terms: List[TensorProduct]):
        self.name = name
        self.terms = terms

    def __repr__(self) -> str:
        return f"Model({self.name})"

    def preamble(self) -> str:
        output = f'M$ModelName = "{self.name}";\n\n'
        output += f"M$Information =\n"
        output += f"{{ Date -> \"{datetime.today().strftime('%Y-%m-%d')}\" }};\n\n"
        output += "(* Sextet not defined in SM model file *)\n"
        output += "IndexRange[Index[Sextet]] = Range[6];\n"
        output += "IndexStyle[Sextet, x];\n"
        output += "AddGaugeRepresentation[SU3C -> {T6, Sextet}];\n\n"
        return output

    @property
    def fields(self) -> List[Field]:
        """Return a list of fields present in the model without duplicates."""
        seen = set()
        output = []
        for term in self.terms:
            for field in term.fields:
                if field.label in seen:
                    continue
                seen.add(field.label)
                output.append(field)
        return output

    @property
    def exotics(self) -> List[Field]:
        """Return a list of exotic fields present in the model without duplicates."""
        return [f for f in self.fields if not f.is_sm]

    def export(self) -> str:
        """Returns a string representing the FeynRules file for the model."""
        params = set()
        for term in self.terms:
            for param in term.feynrules_param_entries():
                params.add(param)

        param_block = format_wolfram_list(params, starting_string="M$Parameters =\n")

        count = 100 - 1
        classes = set()
        for field in self.exotics:
            classes.add(field.feynrules_class_entry(count))

        classes_block = format_wolfram_list(
            classes, starting_string="M$ClassesDescription =\n"
        )

        lagrangian = "(********************* The Lagrangian *********************)\n\n"
        lagrangian += "gotoBFM =\n{ G[a__] -> G[a] + GQuantum[a]\n, Wi[a__] -> Wi[a] + WiQuantum[a]\n, B[a__] -> B[a] + BQuantum[a] \n};\n\n"

        wolfram_term_names = set()
        for field in self.exotics:
            lagrangian += field.feynrules_free_terms()
            lagrangian += "\n\n"
            wolfram_term_names.add(field.wolfram_term_name)

        for term in self.terms:
            lagrangian += term.wolfram()
            lagrangian += "\n\n"
            term_name = term.wolfram_term_name
            wolfram_term_names.add(term_name)
            if term.is_complex:
                wolfram_term_names.add(f"HC[{term_name}]")

        l_tot = f"Ltot := LSM + {' + '.join(wolfram_term_names)};"

        return self.preamble() + param_block + classes_block + lagrangian + l_tot
