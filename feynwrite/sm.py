#!/usr/bin/env python3

"""Defines the SM fields and Lagrangian in terms of Tensor and TensorProduct
objects.

"""

from fractions import Fraction
from tensor import Scalar, Fermion


def L(s0, i0, g0):
    label = "L"
    tensor = Fermion(label=label, indices=[s0, i0, g0], hypercharge=Fraction("-1/2"))
    tensor.is_sm = True
    return tensor


def Q(s0, c0, i0, g0):
    label = "Q"
    tensor = Fermion(label=label, indices=[s0, c0, i0, g0], hypercharge=Fraction("1/6"))
    tensor.is_sm = True
    return tensor


def H(i0):
    label = "H"
    tensor = Scalar(label=label, indices=[i0], hypercharge=Fraction("1/2"))
    tensor.is_sm = True
    return tensor


def eR(s0):
    label = "eR"
    tensor = Fermion(label=label, indices=[s0], chirality="R", hypercharge=-1)
    tensor.is_sm = True
    tensor.latex = r"e_{R}"
    return tensor


def dR(s0, c0):
    label = "dR"
    tensor = Fermion(
        label=label, indices=[s0, c0], chirality="R", hypercharge=Fraction("-1/3")
    )
    tensor.is_sm = True
    tensor.latex = r"d_{R}"
    return tensor


def uR(s0, c0):
    label = "uR"
    tensor = Fermion(
        label=label, indices=[s0, c0], chirality="R", hypercharge=Fraction("2/3")
    )
    tensor.is_sm = True
    tensor.latex = r"u_{R}"
    return tensor
