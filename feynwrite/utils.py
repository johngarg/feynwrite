#!/usr/bin/env python3

from typing import List
from collections import defaultdict

# Conventional index heads
INDICES = {
    "lorentz": "mu",
    "colour_fundamental": "c",
    "colour_adjoint": "C",
    "colour_6": "X",
    "spinor": "s",
    "isospin_fundamental": "i",
    "isospin_adjoint": "I",
    "isospin_4": "Q",
    "generation": "g",
}

EXTRA_PARAMS = r"""EpsSU3 ==
  { ParameterType -> Internal
  , ComplexParameter -> True
  , Indices -> {Index[Colour], Index[Colour], Index[Colour]}
  , Description -> "Three-index epsilon symbol for contracting colour triplets into the antitriplet irrep."
  }
, T6 ==
  { ParameterType -> Internal
  , ComplexParameter -> True
  , Indices -> {Index[Gluon], Index[Sextet], Index[Sextet]}
  , Description -> "SU(3) generators in the sextet representation. See Appendix A.3 of 0909.2666."
  }
, K6 ==
  { ParameterType -> Internal
  , ComplexParameter -> True
  , Indices -> {Index[Sextet], Index[Colour], Index[Colour]}
  , Description -> "Matrices for contracting 3x3 into a 6 fo SU(3). See Appendix A.2 of 0909.2666."
  }
, C2224 ==
  { ParameterType -> Internal
  , ComplexParameter -> True
  , Indices -> {Index[SU2D], Index[SU2D], Index[SU2D], Index[SU24]}
  , Description -> "Matrices for contracting 2x2x2x4 of SU(2). Defined as: sigma(I,i,-j)*C(Q,-I,-k)*Eps(-Q, -R) from 1711.10391."
  }"""


def index_generator(label: str):
    max_number_indices = 20
    for i in range(1, max_number_indices + 1):
        yield label + str(i)


def raise_lower_index(idx: str) -> str:
    if idx[0] == "-":
        return idx[1:]
    return "-" + idx


def wolfram_block(indices: List[str], expr: str, repl: str = "") -> str:
    lines = [
        "Block[",
        "  " + f"{{{','.join(indices)}}}",
        "  ,",
        "  " + expr,
        f"]{repl};",
    ]
    return "\n".join(lines)


def sort_index_labels(index_labels: List[str]) -> List[str]:
    # Index labels shouldn't start with a "-" ever
    index_dict = defaultdict(list)
    for i in index_labels:
        if not i:
            continue
        index_dict[i[0]].append(i)
    # Order in SM model file
    return [
        *index_dict[INDICES["lorentz"]],
        *index_dict[INDICES["spinor"]],
        *index_dict[INDICES["isospin_adjoint"]],
        *index_dict[INDICES["isospin_fundamental"]],
        *index_dict[INDICES["generation"]],
        *index_dict[INDICES["colour_adjoint"]],
        *index_dict[INDICES["colour_6"]],
        *index_dict[INDICES["colour_fundamental"]],
        # FIXME C2224 wants isospin_4 index at the end, so fix this way. If we
        # introduce a 4-plet with colour, this may break.
        *index_dict[INDICES["isospin_4"]],
    ]


def wolfram_index_map(idx: str):
    correspondance = {
        "isospin_4": "SU24",
        "isospin_adjoint": "SU2W",
        "isospin_fundamental": "SU2D",
        "generation": "Generation",
        "colour_adjoint": "Gluon",
        "colour_fundamental": "Colour",
        "colour_6": "Sextet",
        "spinor": "Spinor",
    }

    if idx[0] == "-":
        idx = idx[1:]

    for k, v in INDICES.items():
        if v == idx[0]:
            return f"Index[{correspondance[k]}]"

    raise Exception(f"Unrecognised index {idx}")


def wolfram_func_call(func: str, indices: List[str]):
    return f"{func}[{','.join(indices)}]"


def format_wolfram_list(coll, starting_string: str = ""):
    coll_list = list(coll)
    coll_list[0] = "{ " + coll_list[0]
    coll_block = starting_string
    coll_block += "\n, ".join(coll_list)
    coll_block += "\n};\n\n"
    return coll_block

def format_latex_eqn(coll, lhs: str = ""):
    output_string = "\\begin{align}\n"

    indent = "  "
    output_string += lhs + " &= " + coll[0]
    for latex_string in coll[1:]:
        output_string += indent + "& \\quad + " + latex_string + "\\\\ \n"

    output_string += "\\end{align}"

    return output_string

def sympy_to_mathematica(expr) -> str:
    """Convert sympy expression to string in Mathematica format."""
    return str(expr)\
        .replace("**", "^")\
        .replace("sqrt", "Sqrt")\
        .replace("(", "[")\
        .replace(")", "]")
