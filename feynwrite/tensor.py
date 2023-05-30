#!/usr/bin/env python3

"""Functions for representing fields and Lagrangian interactions."""

from fractions import Fraction
from typing import List, Union, Dict
from dataclasses import dataclass
from copy import deepcopy
import sympy

from feynwrite.utils import (
    INDICES,
    raise_lower_index,
    wolfram_block,
    sort_index_labels,
    wolfram_index_map,
    wolfram_func_call,
    sympy_to_mathematica
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

        # If initialised with an empty string, make sure self.indices is the
        # empty list
        if not indices:
            self.indices = []

        # By default, make latex label the same as string label
        self.latex = latex if latex else label

    def get_latex(self, base_latex=None) -> str:
        """Return LaTeX form of object. If base_latex is passed, use that instead. This
        is useful for dealing with conjugates.

        """
        if base_latex is None:
            base_latex = self.latex

        if not self.indices:
            return base_latex

        lower_indices, upper_indices = [], []
        for i in self.indices:
            if i[0] == "-":
                lower_indices.append(i[1:])
            else:
                upper_indices.append(i)

        lower_indices_string = "" if not lower_indices else f"_{{{' '.join(lower_indices)}}}"
        upper_indices_string = "" if not upper_indices else f"^{{{' '.join(upper_indices)}}}"

        base = f"{{{base_latex}}}"
        if self.is_field and (lower_indices or upper_indices):
            base = f"({base_latex})"

        return base + lower_indices_string + upper_indices_string

    @property
    def tensors(self) -> List["Tensor"]:
        """Utility function to help write __mul__ functions concisely."""
        return [self]

    def __repr__(self) -> str:
        return f"{self.label}({','.join(self.indices)})"

    def __mul__(self, other) -> "TensorProduct":
        assert hasattr(other, "tensors")
        return TensorProduct(self, *other.tensors)

    def get_index_labels(self) -> List[str]:
        """Return a list of indices without negative signs for lowered indices."""
        labels = []
        for i in self.indices:
            if not i:
                continue
            if i[0] == "-":
                labels.append(i[1:])
            else:
                labels.append(i)

        return labels

    @property
    def index_labels(self) -> List[str]:
        """Return a list of indices without negative signs for lowered indices, sorted
        as expected by SM model file.

        """
        return sort_index_labels(self.get_index_labels())

    def wolfram(self, label: str = "", indices: List[str] = []) -> str:
        """Return Wolfram-language form of object. For flexibility, pass in another
        label if it's preferable to export that one. This is useful for fermions.

        """
        if not label:
            label = self.label
        if not self.index_labels:
            return label
        if not indices:
            indices = self.index_labels
        return wolfram_func_call(label, indices)

    @property
    def C(self) -> "Tensor":
        """The hermitian conjugate of the tensor: reverses all fundamental indices.

        """

        # Don't reverse the generation and adjoint indices
        dont_reverse = {
            "generation",
            "isospin_adjoint",
            "isospin_4",
            "colour_adjoint",
            "colour_6",
        }
        dont_reverse = [INDICES[x] for x in dont_reverse]

        reversed_indices = []
        for i in self.indices:
            index_type = i[1] if i[0] == "-" else i[0]
            if index_type in dont_reverse:
                reversed_indices.append(i)
            else:
                reversed_indices.append(raise_lower_index(i))

        conj = deepcopy(self)
        conj.indices = reversed_indices
        conj.is_conj = not self.is_conj
        return conj


class Coupling(Tensor):
    """Tensor representing a coupling contant."""

    def __init__(self, *args, is_complex: bool = True, factor: str = "", **kwargs):
        super(Coupling, self).__init__(*args, **kwargs)
        self.is_field = False
        self.is_complex = is_complex
        # Constant factors that are absorbed in our code compared to the Granada
        # dictionary. Upon export `coupling -> coupling * coupling.factor`.
        self.factor = factor

    def get_latex(self) -> str:
        factor = sympy.latex(self.factor) if self.factor else ""
        return factor + " " + super(Coupling, self).get_latex()

    def wolfram(self) -> str:
        if self.factor:
            return super(Coupling, self).wolfram() + " " + sympy_to_mathematica(self.factor)
        return super(Coupling, self).wolfram()


class Field(Tensor):
    """Tensor representing a Field. An intermediate class wrapping common methods
    and properties of `Scalar`, `Fermion` and `Vector`.

    Fields must receive a hypercharge. This is always the hypercharge of the
    field as defined, conjugating the field will not reverse the hypercharge by
    default. This behaviour is made by choice, so that upon export the
    hypercharge of the field is never ambiguous. The hypercharge is reversed by
    hand only when checking whether a `TensorProduct` object is a singlet.

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
        self.mass_label = self.label.removeprefix("Granada")

    def get_latex(self) -> str:
        # Maybe add dagger to base latex
        base_latex = self.latex
        if self.is_conj:
            base_latex += "^\\dagger"

        return super(Field, self).get_latex(base_latex=base_latex)

    def wolfram(self, label: str = ""):
        indices = self.index_labels
        if not self.is_sm:
            # Unsorted in this case
            indices = self.get_index_labels()
        return super(Field, self).wolfram(label=label, indices=indices)

    def feynrules_class_entry(self, count: int) -> str:
        """Return the Wolfram-language code represented the `M$ClassesDescription` of
        the FeynRules file. This should only be called on an exotic field.

        """
        assert not self.is_sm

        spin_label = str(type(self)).split(".")[-1][0]

        indices = [wolfram_index_map(idx) for idx in self.indices]
        indices = [idx for idx in indices if idx != "Index[Spinor]"]

        lines = [
            f"{spin_label}[{count}] == ",
            f"  {{ ClassName -> {self.label}",
            f"  , Mass -> M{self.mass_label}",
            f"  , Width -> 0",
            f"  , SelfConjugate -> {self.is_self_conj}",
            f"  , QuantumNumbers -> {{Y -> {self.hypercharge}}}"
            if not self.is_self_conj
            else "",
            f"  , Indices -> {{{', '.join(indices)}}}" if indices else "",
            '  , FullName -> "heavy"',
            "  }",
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
        chirality: str = "D",
        is_charge_conj: bool = False,
        is_dirac_adjoint: bool = False,
        **kwargs,
    ):
        super(Fermion, self).__init__(*args, **kwargs)
        # Chirality
        assert chirality in {"L", "R", "D"}
        self.chirality = chirality

        self.is_charge_conj = is_charge_conj
        self.is_dirac_adjoint = is_dirac_adjoint

    def get_latex(self) -> str:
        # Maybe add bar or charge conjugate to base latex
        base_latex = self.latex
        if self.is_dirac_adjoint:
            base_latex = f"\\overline{{{base_latex}}}"
        if self.is_charge_conj:
            base_latex = "{" + base_latex + "^{C}}"

        return super(Field, self).get_latex(base_latex=base_latex)

    def flip_chirality(self) -> None:
        """Flip the chirality of the fermion by side-effect."""
        if self.chirality == "R":
            self.chirality = "L"
        else:
            self.chirality = "R"

    @property
    def left(self) -> "Fermion":
        assert self.chirality == "D"
        other = deepcopy(self)
        other.chirality = "L"
        return other

    @property
    def right(self) -> "Fermion":
        assert self.chirality == "D"
        other = deepcopy(self)
        other.chirality = "R"
        return other

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

        # Deal with chirality
        if not self.is_sm and self.chirality != "D":
            label += self.chirality

        # Deal with charge conjugates and dirac adjoints
        if self.is_charge_conj:
            label = f"CC[{label}]"
        if self.is_dirac_adjoint:
            label = f"anti[{label}]"

        # Dress label with indices
        output = super(Fermion, self).wolfram(label=label)

        # For bar, add . for matrix multiplication
        if self.is_dirac_adjoint:
            output = output + "."

        return output

    def feynrules_free_terms(self) -> str:
        """Returns a string representing the free-field Lagrangian for the fermion."""
        assert not self.is_sm

        kinetic = f"I {self.label}bar.Ga[mu].DC[{self.label}, mu]"
        mass = f"M{self.mass_label} {self.label}bar.{self.label}"

        # Adjust factors for Majorana fermions
        if self.is_self_conj:
            kinetic = "1/2 " + kinetic
            mass = "1/2 " + mass

        expr = f"{kinetic} - {mass}"

        # Keep track of name for model file
        wolfram_term_name = f"LFree{self.label}"
        self.wolfram_term_name = wolfram_term_name

        return f"{wolfram_term_name} :=\n" + wolfram_block(
            ["mu"], expr, repl="/.gotoBFM"
        )

    def feynrules_class_entry_chiral(self, count: int, chirality: str) -> str:
        """Returns the Wolfram-language code for the class entry for the unphysical field
        picking out the `chirality` component of the fermion.

        For a Majorana fermion X, we default the components to X_R and X_R^c, so
        asking for the left-handed component

        """
        assert not self.is_sm
        assert chirality in {"L", "R"}

        spin_label = str(type(self)).split(".")[-1][0]

        indices = [wolfram_index_map(idx) for idx in self.indices]
        indices = [idx for idx in indices if idx != "Index[Spinor]"]

        index_label_patterns = [idx + "_" for idx in self.index_labels]
        index_label_patterns_str = ",".join(index_label_patterns)
        index_labels_str = ",".join(self.index_labels)
        projector = "left" if chirality == "L" else "right"

        lines = [
            f"{spin_label}[{count}] == ",
            f"  {{ ClassName -> {self.label}{chirality}",
            f"  , Mass -> M{self.mass_label}",
            f"  , Width -> 0",
            f"  , SelfConjugate -> {self.is_self_conj}",
            f"  , QuantumNumbers -> {{Y -> {self.hypercharge}}}"
            if not self.is_self_conj
            else "",
            f"  , Indices -> {{{', '.join(indices)}}}" if indices else "",
            f"  , Unphysical -> True",
            f"  , Definitions -> {{{self.label}{chirality}[{index_label_patterns_str}] :> {projector}[{self.label}[{index_labels_str}]]}}",
            "  }",
        ]

        return "\n".join(line for line in lines if line)


class Scalar(Field):
    def __init__(self, *args, **kwargs):
        super(Scalar, self).__init__(*args, **kwargs)

    @property
    def C(self) -> "Scalar":
        if self.is_self_conj:
            return self

        # Tensor conjugation method
        conj = super(Field, self).C

        return conj

    def wolfram(self) -> str:
        label = self.label

        # Deal with conj
        if self.is_conj:
            label = f"anti[{label}]"

        return super(Scalar, self).wolfram(label=label)

    def feynrules_free_terms(self) -> str:
        """Returns a string representing the free-field Lagrangian for the scalar."""
        assert not self.is_sm

        indices = self.index_labels + ["mu"]

        # We always want the kinetic term to look like (D S)^dag (D S), but
        # would look like (D S) (D S)^dag if S where already `conj`ed. Fix this
        # here by hand
        if self.is_conj:
            dagger = self.wolfram()
            no_dagger = self.C.wolfram()
        else:
            # Real scalar will also enter this branch
            dagger = self.C.wolfram()
            no_dagger = self.wolfram()

        kinetic = f"DC[{dagger}, mu] DC[{no_dagger}, mu]"
        mass = f"M{self.label}^2 {dagger} {no_dagger}"

        # Adjust factors for real scalars
        if self.is_self_conj:
            kinetic = "1/2 " + kinetic
            mass = "1/2 " + mass

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

    def get_latex(self):
        return " ".join(t.get_latex() for t in self.tensors)

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

    @property
    def structures(self):
        return [
            t for t in self.tensors if not t.is_field and not isinstance(t, Coupling)
        ]

    def feynrules_param_entries(self) -> List[str]:
        """Returns a list of strings representing the `M$Parameters` entries in the FeynRules file."""
        couplings = self.couplings
        assert len(couplings) == 1
        coupling = couplings[0]
        # The only coupling indices should be generation indices
        non_trivial_indices = [c for c in coupling.indices if c]
        coupling_indices = [wolfram_index_map("g")] * len(non_trivial_indices)
        lines = [
            f"{coupling.label} ==",
            "  { ParameterType -> Internal",
            f"  , ComplexParameter -> {coupling.is_complex}",
            # Don't include `Indices` entry if there are no indices!
            f"  , Indices -> {{{', '.join(coupling_indices)}}}"
            if coupling_indices
            else "",
            f'  , Description -> "Coupling {coupling.label} of {self.__repr__()} interaction"',
            "  }",
        ]
        # Filter out empty strings
        coupling = "\n".join(line for line in lines if line)

        # Masses
        masses = []
        for f in self.exotics:
            lines = [
                f"M{f.mass_label} == ",
                "  { ParameterType -> Internal",
                f'  , Description -> "{f.label} mass"',
                "  }",
            ]
            masses.append("\n".join(lines))

        return [coupling, *masses]

    def sum_hypercharges(self) -> Union[Fraction, int]:
        """Returns the sum of the hypercharges of the term."""
        tally = 0
        for f in self.fields:
            y = f.hypercharge * (-1 if f.is_conj else 1)
            tally += y
        return tally

    def expand_indices(kind: str, replacements: Dict[str, str]):
        pass


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

    # Get type of indices from first letter
    kind = first[1 if is_lower else 0]

    # For colour indices, use K3 instead?
    if len(indices) == 3 and kind == INDICES["colour_fundamental"]:
        # label = "Sqrt[2]*K3"
        label = "EpsSU3"

    # For isospin adjoint indices, use fsu2 instead of Eps
    kind = first[1 if is_lower else 0]
    if len(indices) == 3 and kind == INDICES["isospin_adjoint"]:
        label = "fsu2"

    tensor = Tensor(label=label, indices=indices)
    tensor.latex = r"\epsilon"
    tensor.is_field = False
    return tensor

def eps4(Q0: str, Q1: str):
    assert Q0[0] == "-" and Q1[0] == "-"
    label = "Eps4"
    tensor = Tensor(label=label, indices=[Q0, Q1])
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


def c2224(Q: str, i: str, j: str, k: str):
    """[C^Q]^i_{ jk}"""
    assert i[0] != "-" and j[0] == "-" and k[0] == "-"
    assert Q[0] == INDICES["isospin_4"] or Q[1] == INDICES["isospin_4"]

    label = "C2224"
    tensor = Tensor(label=label, indices=[Q, i, j, k])
    tensor.latex = r"C_{2224}"
    tensor.is_field = False
    return tensor

def c344(I: str, Q0: str, Q1: str):
    """[C^I]^Q0_{ Q1}"""
    assert Q0[0] == INDICES["isospin_4"] or Q0[1] == INDICES["isospin_4"]
    assert Q1[0] == INDICES["isospin_4"] or Q1[1] == INDICES["isospin_4"]

    label = "C344"
    tensor = Tensor(label=label, indices=[I, Q0, Q1])
    tensor.latex = r"C_{344}"
    tensor.is_field = False
    return tensor


def K(X: str, a: str, b: str):
    assert X[0] != "-" and a[0] == "-" and b[0] == "-"
    assert (
        X[0] == INDICES["colour_6"]
        and a[1] == INDICES["colour_fundamental"]
        and b[1] == INDICES["colour_fundamental"]
    )

    label = "K6"
    tensor = Tensor(label=label, indices=[X, a, b])
    tensor.latex = r"K"
    tensor.is_field = False
    return tensor
