#!/usr/bin/env python3

"""File that contains functions for generating the Mathematica code that will
enter the FeynRules output.

"""

# Depends on: tensor.py

from typing import List, Set
from feynwrite.tensor import TensorProduct, Field, Coupling
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Model:
    def __init__(self, name: str, terms: List[TensorProduct]):
        self.name = name
        self.terms = terms

    def __repr__(self) -> str:
        return f"Model({self.name})"

    def preamble(self) -> str:
        output = f'M$ModelName = "{self.name}";\n\n'
        output += f"M$Information =\n"
        output += f"{{ Date -> {datetime.today().strftime('%Y-%m-%d')} }};\n\n"
        output += "M$InteractionOrderHierarchy =\n"
        output += "{ {QCD, 1}\n"
        output += ", {QED, 2}\n"
        output += ", {NP, 1}\n"
        output += "};\n\n"
        return output

    @property
    def fields(self) -> List[Field]:
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
        return [f for f in self.fields if not f.is_sm]

    def export(self) -> str:
        params = set()
        for term in self.terms:
            for param in term.feynrules_param_entries():
                params.add(param)

        param_block = "M$Parameters = {\n"
        param_block += "\n,  ".join(params)
        param_block += "\n};\n\n"

        count = 100
        classes = set()
        for field in self.exotics:
            classes.add(field.feynrules_class_entry(count))

        classes_block = "M$ClassesDescription = {\n"
        classes_block += "\n,  ".join(classes)
        classes_block += "\n};\n\n"

        lagrangian = "(********************* The Lagrangian *********************)\n\n"
        lagrangian += "gotoBFM={G[a__]->G[a]+GQuantum[a],Wi[a__]->Wi[a]+WiQuantum[a],B[a__]->B[a]+BQuantum[a]};\n\n"

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
