#!/usr/bin/env python3

"""Defines the SM fields in terms of Tensor objects.

"""

from fractions import Fraction
from feynwrite.tensor import Scalar, Fermion, Vector, Tensor


def L(s, i, g):
    label = "LL"
    tensor = Fermion(
        label=label, indices=[s, i, g], hypercharge=Fraction("-1/2"), chirality="L"
    )
    tensor.is_sm = True
    tensor.latex = "L"
    return tensor


def Q(s, c, i, g):
    label = "QL"
    tensor = Fermion(
        label=label, indices=[s, c, i, g], hypercharge=Fraction("1/6"), chirality="L"
    )
    tensor.is_sm = True
    tensor.latex = "Q"
    return tensor


def H(i):
    label = "Phi"
    tensor = Scalar(label=label, indices=[i], hypercharge=Fraction("1/2"))
    tensor.is_sm = True
    tensor.latex = "H"
    return tensor


def DH(l, i):
    label = "Phi"
    tensor = Vector(label=label, indices=[l, i], hypercharge=Fraction("1/2"))
    tensor.is_sm = True
    tensor.latex = "H"
    tensor.is_deriv = True
    return tensor


def eR(s, g):
    label = "LR"
    tensor = Fermion(label=label, indices=[s, g], chirality="R", hypercharge=-1)
    tensor.is_sm = True
    tensor.latex = r"e_{R}"
    return tensor


def dR(s, c, g):
    label = "DR"
    tensor = Fermion(
        label=label, indices=[s, c, g], chirality="R", hypercharge=Fraction("-1/3")
    )
    tensor.is_sm = True
    tensor.latex = r"d_{R}"
    return tensor


def uR(s, c, g):
    label = "UR"
    tensor = Fermion(
        label=label, indices=[s, c, g], chirality="R", hypercharge=Fraction("2/3")
    )
    tensor.is_sm = True
    tensor.latex = r"u_{R}"
    return tensor

def FS(V, l0, l1, V_index=None):
    indices = [V, l0, l1] if V_index is None else [V, l0, l1, V_index]
    tensor = Tensor(
        label="FS",
        indices=indices,
        latex=V,
        is_field=True,
        is_conj=False
    )
    tensor.is_sm = True
    return tensor
