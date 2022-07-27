#!/usr/bin/env python3

"""Functions for representing fields and Lagrangian interactions."""

from fractions import Fraction
from typing import List, Union, Dict
from dataclasses import dataclass
from copy import deepcopy

from feynwrite.utils import (
    INDICES,
    raise_lower_index,
    wolfram_block,
    sort_index_labels,
    wolfram_index_map,
)


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
        """Return a list of indices without negative signs for lowered indices."""
        labels = []
        for i in self.indices:
            if not i:
                continue
            if i[0] == "-":
                labels.append(i[1:])
            else:
                labels.append(i)

        return sort_index_labels(labels)

    def wolfram(self) -> str:
        """Return Wolfram-language form of object."""
        if not self.index_labels:
            return self.label
        return f"{self.label}[{','.join(self.index_labels)}]"

    @property
    def C(self) -> "Tensor":
        """The hermitian conjugate of the tensor: reverses all indices except for
        generation.

        """
        reversed_indices = []
        for i in self.indices:
            if i[0] == INDICES["generation"]:
                reversed_indices.append(i)
            else:
                reversed_indices.append(raise_lower_index(i))

        conj = deepcopy(self)
        conj.indices = reversed_indices
        conj.is_conj = not self.is_conj
        return conj


class Coupling(Tensor):
    """Tensor representing a coupling contant."""

    def __init__(self, *args, is_complex: bool = True, **kwargs):
        super(Coupling, self).__init__(*args, **kwargs)
        self.is_field = False
        self.is_complex = is_complex


class Field(Tensor):
    """Tensor representing a Field. An intermediate class wrapping common methods
    and properties of `Scalar`, `Fermion` and `Vector`.

    Fields must receive a hypercharge.

    """

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
        self.wolfram_term_name: str = ""

    def feynrules_class_entry(self, count: int) -> List[str]:
        """Return the Wolfram-language code represented the `M$ClassesDescription` of
        the FeynRules file. This should only be called on an exotic field.

        """
        assert not self.is_sm

        count += 1
        spin_label = str(type(self)).split(".")[-1][0]

        indices = [wolfram_index_map(idx) for idx in self.indices]

        lines = [
            f"{spin_label}[{count}] == ",
            f"{{ ClassName -> {self.label}",
            f"  , Mass -> M{self.label}",
            f"  , Width -> 0",
            f"  , SelfConjugate -> {self.is_self_conj}",
            f"  , QuantumNumbers -> {{Y -> {self.hypercharge}}}",
            f"  , Indices -> {{{', '.join(indices)}}}" if indices else "",
            '  , FullName -> "heavy"',
            "}",
        ]

        return "\n".join(line for line in lines if line)


class Fermion(Field):
    """Class representing a (0,1/2) or (1/2,0) fermion. This is specified by
    `chirality`.

    `is_charge_conj` and `is_dirac_adjoint` are toggled by `.CC` and `.bar`,
    respectively.

    """

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

    def flip_chirality(self) -> None:
        """Flip the chirality of the fermion by side-effect."""
        if self.chirality == "R":
            self.chirality = "L"
        else:
            self.chirality = "R"

    @property
    def CC(self) -> "Fermion":
        """Lowers only the gauge indices"""
        conj = self.C
        conj.is_charge_conj = not self.is_charge_conj
        conj.flip_chirality()
        conj.indices[0] = raise_lower_index(conj.indices[0])
        return conj

    @property
    def bar(self) -> "Fermion":
        """The same as the method `.C` in practice, but toggles `is_dirac_adjoint`."""
        dirac_adjoint = self.C
        dirac_adjoint.is_dirac_adjoint = not self.is_dirac_adjoint
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
        """Returns a string representing the free-field Lagrangian for the scalar."""

        # TODO Adapt constant factors here for `is_self_conj` case

        assert not self.is_sm

        indices = self.index_labels + ["mu"]

        # We always want the kinetic term to look like (D S)^dag (D S), but
        # would look like (D S) (D S)^dag if S where already `conj`ed. Fix this
        # here by hand
        if self.is_conj:
            dagger = self.wolfram()
            no_dagger = self.C.wolfram()
        else:
            dagger = self.C.wolfram()
            no_dagger = self.wolfram()

        kinetic = f"DC[{dagger}, mu] DC[{no_dagger}, mu]"
        mass = f"M{self.label}^2 {dagger} {no_dagger}"
        expr = f"{kinetic} - {mass}"

        # Keep track of name for model file
        wolfram_term_name = f"LFree{self.label}"
        self.wolfram_term_name = wolfram_term_name

        return f"{wolfram_term_name} :=\n" + wolfram_block(
            indices, expr, repl="/.gotoBFM"
        )


def Vector(Tensor):
    pass


@dataclass
class TensorProduct:
    """Class representing a product of tensors. It's use is mostly specialised to
    the case of representing a term in the Lagrangian, i.e. a single coupling
    constant and fields.

    """

    def __init__(self, *tensors):
        self.tensors = tensors
        # Filled in when `wolfram` method is called
        self.wolfram_term_name: str = ""

    @property
    def free_indices(self) -> List[str]:
        """Returns the uncontracted indices of the product."""
        # Separate upper and lower indices
        upper, lower = [], []
        for tensor in self.tensors:
            for index in tensor.indices:
                if not index:
                    continue
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

    @property
    def is_complex(self) -> bool:
        """Just check whether the coupling constant is complex."""
        couplings = self.couplings
        assert len(couplings) == 1
        return couplings[0].is_complex

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
            # Label Lagrangian terms by the couplings constants
            if isinstance(t, Coupling):
                labels += t.label
            for i in t.index_labels:
                indices.add(i)

            wolfram_ = t.wolfram()
            # For fermion chains, don't add an extra space when exporting
            if wolfram_[-1] != ".":
                wolfram_ = wolfram_ + " "
            output += wolfram_

        wolfram_term_name = f"L{labels}"
        self.wolfram_term_name = wolfram_term_name

        return f"{wolfram_term_name} :=\n" + wolfram_block(indices, output.strip())

    @property
    def couplings(self):
        return [t for t in self.tensors if isinstance(t, Coupling)]

    @property
    def fields(self):
        return [t for t in self.tensors if t.is_field]

    @property
    def exotics(self):
        return [f for f in self.fields if not f.is_sm]

    def feynrules_param_entries(self) -> List[str]:
        """Returns a list of strings representing the `M$Parameters` entries in the FeynRules file."""
        couplings = self.couplings
        assert len(couplings) == 1
        coupling = couplings[0]
        # The only coupling indices should be generation indices
        non_trivial_indices = [c for c in coupling.indices if c]
        coupling_indices = [wolfram_index_map("g")] * len(non_trivial_indices)
        lines = [
            f"{coupling.label} == ",
            "{ ParameterType -> Internal",
            f"  , ComplexParameter -> {coupling.is_complex}",
            # Don't include `Indices` entry if there are no indices!
            f"  , Indices -> {{{', '.join(coupling_indices)}}}"
            if coupling_indices
            else "",
            "  , InteractionOrder -> {NP, 1}",
            f'  , Description -> "Coupling {coupling.label} of {self.__repr__()} interaction"',
            "}",
        ]
        # Filter out empty strings
        coupling = "\n".join(line for line in lines if line)

        # Masses
        masses = []
        for f in self.exotics:
            lines = [
                f"M{f.label} == ",
                "{ ParameterType -> Internal",
                f'  , Description -> "{f.label} mass"',
                "}",
            ]
            masses.append("\n".join(lines))

        return [coupling, *masses]

    def sum_hypercharges(self) -> Union[Fraction, int]:
        """Returns the sum of the hypercharges of the term."""
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


def sigma(I: str, i: str, j: str):
    """Pauli matrices"""
    assert j[0] == "-" and i[0] != "-"

    label = "2*Ta"
    tensor = Tensor(label=label, indices=[I, i, j])
    tensor.latex = r"\sigma"
    tensor.is_field = False
    return tensor


def lambda_(A: str, a: str, b: str):
    """Gell-Mann matrices"""
    assert b[0] == "-" and a[0] != "-"

    label = "2*T"
    tensor = Tensor(label=label, indices=[A, a, b])
    tensor.latex = r"\lambda"
    tensor.is_field = False
    return tensor
