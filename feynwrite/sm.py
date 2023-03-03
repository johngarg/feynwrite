#!/usr/bin/env python3

"""Defines the SM fields in terms of Tensor objects.

"""

from fractions import Fraction
from feynwrite.tensor import Scalar, Fermion


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
    # TODO Fix this, as exotic in Granada dictionary with the same name
    label = "Phi"
    tensor = Scalar(label=label, indices=[i], hypercharge=Fraction("1/2"))
    tensor.is_sm = True
    tensor.latex = "H"
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
