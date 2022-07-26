#!/usr/bin/env python3

"""Functions for representing fields and Lagrangian interactions."""

from fractions import Fraction
from typing import List, Union, Dict
from dataclasses import dataclass
from copy import deepcopy

from utils import index_generator, raise_lower_index, wolfram_module, sort_index_labels


@dataclass
class Tensor:
    def __init__(
        self,
        label: str,
        indices: Union[str, List[str]],
        latex: str = "",
        is_field: bool = True,
        is_conj: bool = False,
    ):
        self.label = label
        self.is_field = is_field
        self.is_conj = is_conj

        # Represent indices as space-separated string, e.g. "i j k"
        if isinstance(indices, str):
            indices = indices.split(" ")
        self.indices = indices

        self.latex = latex
        # By default, make latex label the same as string label
        if not latex:
            self.latex = label

    @property
    def tensors(self) -> List["Tensor"]:
        """Utility function to help write __mul__ functions concisely."""
        return [self]

    def __repr__(self) -> str:
        return f"{self.label}({','.join(self.indices)})"

    def __mul__(self, other) -> "TensorProduct":
        assert hasattr(other, "tensors")
        return TensorProduct(self, *other.tensors)

    @property
    def index_labels(self) -> List[str]:
        labels = [i if i[0] != "-" else i[1:] for i in self.indices]
        return sort_index_labels(labels)

    def wolfram(self) -> str:
        if not self.index_labels:
            return self.label
        return f"{self.label}[{','.join(self.index_labels)}]"

    @property
    def C(self) -> "Tensor":
        # Raise/lower indices, except for generation
        reversed_indices = []
        for i in self.indices:
            if i[0] == "g":
                reversed_indices.append(i)
            else:
                reversed_indices.append(raise_lower_index(i))

        conj = deepcopy(self)
        conj.indices = reversed_indices
        conj.is_conj = True
        return conj


class Coupling(Tensor):
    def __init__(self, *args, is_complex: bool = True, **kwargs):
        super(Coupling, self).__init__(*args, **kwargs)
        self.is_field = False
        self.is_complex = is_complex


class Field(Tensor):
    def __init__(
        self,
        *args,
        hypercharge: Union[int, Fraction],
        is_sm: bool = False,
        is_self_conj: bool = False,
        **kwargs,
    ):
        super(Field, self).__init__(*args, **kwargs)
        self.is_sm = is_sm
        self.hypercharge = hypercharge
        self.is_self_conj = is_self_conj

    def irrep(self) -> Dict[str, List[int]]:
        """Infer the SM irrep based on the indices of the field."""
        index_dict = {"c": [0, 0], "i": [0, 0]}
        for i in self.indices:
            is_lower = i[0] == "-"
            key = i if not is_lower else i[1:]
            if key[0] in {"g", "s"}:
                continue
            entry = 1 if is_lower else 0
            index_dict[key[0]][entry] += 1

        return dict(index_dict)


class Fermion(Field):
    def __init__(
        self,
        *args,
        chirality: str = "L",
        is_charge_conj: bool = False,
        is_dirac_adjoint: bool = False,
        **kwargs,
    ):
        super(Fermion, self).__init__(*args, **kwargs)
        # Chirality
        assert chirality in {"L", "R"}
        self.chirality = chirality

        self.is_charge_conj = is_charge_conj
        self.is_dirac_adjoint = is_dirac_adjoint

    def flip_chirality(self):
        if self.chirality == "R":
            self.chirality = "L"
        else:
            self.chirality = "R"

    @property
    def CC(self) -> "Fermion":
        """Lowers only the gauge indices"""
        conj = self.C
        conj.is_charge_conj = True
        conj.flip_chirality()
        conj.indices[0] = raise_lower_index(conj.indices[0])
        return conj

    @property
    def bar(self) -> "Fermion":
        dirac_adjoint = self.C
        dirac_adjoint.is_dirac_adjoint = True
        return dirac_adjoint

    def wolfram(self) -> str:
        label = self.label

        # Deal with charge conjugates and dirac adjoints
        if self.is_charge_conj:
            label = f"CC[{label}]"
        if self.is_dirac_adjoint:
            label = f"anti[{label}]"

        if not self.index_labels:
            output = label
        else:
            output = f"{label}[{','.join(self.index_labels)}]"

        # For bar, add . for matrix multiplication
        if self.is_dirac_adjoint:
            output = output + "."

        return output


class Scalar(Field):
    def __init__(self, *args, **kwargs):
        super(Scalar, self).__init__(*args, **kwargs)

    def wolfram(self) -> str:
        label = self.label

        # Deal with conj
        if self.is_conj:
            label = f"anti[{label}]"

        if not self.index_labels:
            output = label
        else:
            output = f"{label}[{','.join(self.index_labels)}]"

        return output

    def feynrules_free_terms(self) -> str:
        indices = self.indices + ["mu"]
        kinetic = f"DC[{self.C.wolfram()}, mu] DC[{self.wolfram()}, mu]"
        mass = f"M{self.label}^2 {self.C.wolfram()} {self.wolfram()}"
        expr = f"{kinetic} - {mass}"
        return f"LFree{self.label} :=\n" + wolfram_module(indices, expr)


def Vector(Tensor):
    pass


@dataclass
class TensorProduct:
    def __init__(self, *tensors):
        self.tensors = tensors

    @property
    def free_indices(self) -> List[str]:
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

        return sorted(upper.symmetric_difference(lower))

    def __mul__(self, other):
        return self.__class__(*self.tensors, *other.tensors)

    def __repr__(self):
        return "*".join([t.__repr__() for t in self.tensors])

    def latex(self):
        return " ".join(t.latex for t in self.tensors)

    def wolfram(self):
        output = ""
        labels = ""
        indices = set()

        # Keep track of labels for Lagrangian term and indices for module
        for t in self.tensors:
            labels += t.label
            for i in t.index_labels:
                indices.add(i)

            wolfram_ = t.wolfram()
            if wolfram_[-1] != ".":
                wolfram_ = wolfram_ + " "
            output += wolfram_

        return f"L{labels} :=\n" + wolfram_module(indices, output.strip())

    @property
    def couplings(self):
        return [t for t in self.tensors if isinstance(t, Coupling)]

    @property
    def fields(self):
        return [t for t in self.tensors if t.is_field]

    def feynrules_param_entries(self) -> List[str]:
        # Couplings
        couplings = self.couplings
        assert len(couplings) == 1
        coupling = couplings[0]
        coupling_indices = ["Index[Generation]"] * len(coupling.indices)
        term_label = self.latex()
        lines = [
            f"{coupling.label} == ",
            "{ ParameterType -> External",
            f"  , ComplexParameter -> {coupling.is_complex}",
            f"  , Indices -> {{{', '.join(coupling_indices)}}}"
            if coupling_indices
            else "",
            "  , InteractionOrder -> {NP, 1}",
            f'  , Description -> "Coupling {coupling.latex} of {term_label} interaction"',
            "}",
        ]
        coupling = "\n".join(line for line in lines if line)

        # Masses
        masses = []
        for f in self.fields:
            if f.is_sm:
                continue

            is_fermion = isinstance(f, Fermion)

            lines = [
                f"M{f.label} == ",
                "{ ParameterType -> External",
                f'  , Description -> "{f.label} mass"',
                "}",
            ]
            masses.append("\n".join(lines))

        return [coupling, *masses]

    def feynrules_class_entries(self, count: int) -> List[str]:
        for f in self.fields:
            if f.is_sm:
                continue

            count += 1
            spin_label = str(type(f)).split(".")[-1][0]

            irrep = f.irrep()
            indices = []
            # Isospin options
            if sum(irrep["i"]) == 1:
                indices.append("Index[SU2D]")
            elif sum(irrep["i"]) == 2:
                indices.append("Index[SU2W]")
            elif sum(irrep["i"]) == 3:
                # TODO Fill this in properly
                indices.append("Index[SU24]")

            # Colour options
            if irrep["c"] == [1, 1]:
                # TODO Fill this in properly
                indices.append("Index[ColourAdjoint]")
            elif sum(irrep["c"]) == 1:
                indices.append("Index[Colour]")
            elif sum(irrep["c"]) == 2:
                indices.append("Index[Colour]")
                indices.append("Index[Colour]")

            lines = [
                f"{spin_label}[{count}] == ",
                f"{{ ClassName -> {f.label}",
                f"  , Mass -> M{f.label}",
                f"  , Width -> W{f.label}",
                f"  , SelfConjugate -> {f.is_self_conj}",
                f"  , QuantumNumbers -> {{Y -> {f.hypercharge}}}",
                f"  , Indices -> {{{', '.join(indices)}}}" if indices else "",
                '  , FullName -> "heavy"',
                "}",
            ]

        return "\n".join((line for line in lines if line))

    def sum_hypercharges(self) -> Fraction:
        tally = 0
        for f in self.fields:
            tally += f.hypercharge
        return tally


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
