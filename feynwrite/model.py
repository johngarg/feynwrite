#!/usr/bin/env python3

"""File that contains the Model class for generating the Mathematica code that
will enter the FeynRules output.

"""

# Depends on: tensor.py

from typing import List, Set
from dataclasses import dataclass
from datetime import datetime

from feynwrite.tensor import Tensor, Fermion, TensorProduct, Field, Coupling
from feynwrite.utils import format_wolfram_list, EXTRA_PARAMS


def _unique_subcollection(coll: List[TensorProduct], subcoll_name: str) -> List[Tensor]:
    """Return a list of unique subcoll from coll. For example
    `_unique_subcollection(coll=terms, subcoll_name="fields")` will return a
    list of unique fields in the terms.

    """
    seen = set()
    output = []
    for item in coll:
        for subitem in getattr(item, subcoll_name):
            if subitem.label in seen:
                continue
            seen.add(subitem.label)
            output.append(subitem)
    return output


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
        self.fields = _unique_subcollection(self.terms, "fields")
        self.couplings = _unique_subcollection(self.terms, "couplings")

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
    def exotics(self) -> List[Field]:
        """Return a list of exotic fields present in the model without duplicates."""
        return [f for f in self.fields if not f.is_sm]

    def export_mmp_config(self) -> str:
        """Returns a string representing the MatchMakerParser configuration file for the
        model.

        """
        sm_couplings = ["yd", "ydbar", "yu", "yubar", "yl", "ylbar"]
        couplings_with_ranges = []
        for sm_coupling in sm_couplings:
            couplings_with_ranges.append(f"{{{sm_coupling}, {{3,3}}}}")

        exotic_params = []
        # Add masses
        for exotic in self.exotics:
            exotic_params.append(f"M{exotic.label}")
        # Add couplings
        for coupling in self.couplings:
            exotic_params.append(coupling.label)
            exotic_params.append(coupling.label + "bar")

            n_indices = len(coupling.indices)
            # If coupling has not indices, it need not be added to $Couplings in
            # MatchMakerParser at all
            if not n_indices:
                continue

            n_f = 3  # FIXME This is hardcoded here
            dimensions = [str(n_f)] * n_indices
            dimensions_str = "{" + ",".join(dimensions) + "}"

            couplings_with_ranges.append(f"{{{coupling.label}, {dimensions_str}}}")
            couplings_with_ranges.append(f"{{{coupling.label}bar, {dimensions_str}}}")

        output = f"DeclareCouplings[{','.join(couplings_with_ranges)}];\n"
        output += f"DeclareExoticParams[{','.join(exotic_params)}];"
        return output

    def export(self) -> str:
        """Returns a string representing the FeynRules file for the model."""
        params = set()
        for term in self.terms:
            for param in term.feynrules_param_entries():
                params.add(param)

        param_list = list(params)
        param_list.append(EXTRA_PARAMS)
        param_block = format_wolfram_list(
            param_list, starting_string="M$Parameters =\n"
        )

        count = 200 - 1
        classes = set()
        for field in self.exotics:
            count += 1
            classes.add(field.feynrules_class_entry(count))
            # Add left and right fermions if needed
            if isinstance(field, Fermion):
                count += 1
                classes.add(field.feynrules_class_entry_chiral(count, "L"))
                count += 1
                classes.add(field.feynrules_class_entry_chiral(count, "R"))

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
