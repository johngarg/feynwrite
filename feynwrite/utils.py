#!/usr/bin/env python3

from typing import List
from collections import defaultdict


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
        "  ExpandIndices[",
        "    " + expr,
        "    , FlavorExpand -> {SU2W, SU2D, Generation}",
        "  ]",
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
    return [*index_dict["s"], *index_dict["i"], *index_dict["g"], *index_dict["c"]]
