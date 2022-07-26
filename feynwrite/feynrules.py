#!/usr/bin/env python3

"""File that contains functions for generating the Mathematica code that will
enter the FeynRules output.

"""

# Depends on: tensor.py

from typing import List, Set
from tensor import TensorProduct, Field, Coupling
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Model:
    def __init__(self, name: str, terms: List[TensorProduct]):
        self.name = name
        self.terms = terms

    def preamble(self) -> str:
        output = f"M$ModelName = {self.name};\n\n"
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

    def export(self) -> str:
        output = ""
        params, classes = set(), set()
        count = 100
        for term in self.terms:
            for param in term.feynrules_param_entries():
                params.add(param)

            classes.add(term.feynrules_class_entries(count))

        param_block = "M$Parameters = {\n"
        param_block += "\n,  ".join(params)
        param_block += "\n};\n\n"

        classes_block = "M$ClassesDescription = {\n"
        classes_block += "\n,  ".join(classes)
        classes_block += "\n};\n\n"

        lagrangian = "(********************* The Lagrangian *********************)\n\n"
        for field in self.fields:
            if field.is_sm:
                continue
            lagrangian += field.feynrules_free_terms()
            lagrangian += "\n\n"

        for term in self.terms:
            lagrangian += term.wolfram()
            lagrangian += "\n\n"

        return self.preamble() + param_block + classes_block + lagrangian
