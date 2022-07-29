#!/usr/bin/env python3

from typing import List
from collections import defaultdict

# Conventional index heads
INDICES = {
    "lorentz": "mu",
    "colour_fundamental": "c",
    "colour_adjoint": "C",
    "spinor": "s",
    "isospin_fundamental": "i",
    "isospin_adjoint": "I",
    "isospin_4": "Q",
    "generation": "g",
}


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
    }

    if idx[0] == "-":
        idx = idx[1:]

    for k, v in INDICES.items():
        if v == idx[0]:
            return f"Index[{correspondance[k]}]"

    raise Exception(f"Unrecognised index {idx}")
