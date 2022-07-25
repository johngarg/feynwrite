#!/usr/bin/env python3

"""Fucntions for representing fields and Lagrangian interactions."""

from typing import List
from dataclasses import dataclass


@dataclass
class Tensor:
    def __init__(
        self, label: str, indices: List[str], latex: str = "", is_field: bool = True
    ):
        self.label = label
        self.indices = indices
        self.is_field = is_field

        # By default, make latex label the same as string label
        if not latex:
            self.latex = label

    @property
    def tensors(self):
        """Utility function to help write __mul__ functions concisely."""
        return [self]

    def __repr__(self):
        return f"{self.label}({','.join(self.indices)})"

    def __mul__(self, other):
        assert hasattr(other, "tensors")
        return TensorProduct(self, *other.tensors)


@dataclass
class TensorProduct:
    def __init__(self, *tensors):
        self.tensors = tensors

    @property
    def free_indices(self):
        # Separate upper and lower indices
        upper, lower = [], []
        for tensor in self.tensors:
            for index in tensor.indices:
                if index[0] == "-":
                    lower.append(index[1:])
                else:
                    upper.append(index)

        # Make sure indices are not repeated unless contracted correctly
        assert len(set(upper)) == len(upper)
        assert len(set(lower)) == len(lower)

        # Convert to sets for difference function
        upper, lower = set(upper), set(lower)

        return upper.symmetric_difference(lower)

    def __mul__(self, other):
        return self.__class__(*self.tensors, *other.tensors)

    def __repr__(self):
        return "*".join([t.__repr__() for t in self.tensors])


def eps(*indices):
    """Tensor representing antisymmetric symbol"""

    # Assert correct index structure
    first, *rest = indices
    is_lower = first[0] == "-"
    for index in rest:
        if is_lower:
            assert index[0] == "-"
        else:
            assert index[0] != "-"

    label = "Eps"
    tensor = Tensor(label=label, indices=indices)
    tensor.latex = r"\epsilon"
    tensor.is_field = False
    return tensor


def delta(i: str, j: str):
    # Assert correct index structure
    assert j[0] == "-" and i[0] != "-"

    label = "Delta"
    tensor = Tensor(label=label, indices=[i, j])
    tensor.latex = r"\delta"
    tensor.is_field = False
    return tensor
