#!/usr/bin/env python3

"""Defines the SM fields and Lagrangian in terms of Tensor and TensorProduct
objects.

"""

from feynwrite.tensor import Tensor, TensorProduct, eps, delta


def L(spin, isospin, generation):
    label = "L"
    tensor = Tensor(label=label, indices=[spin, isospin, generation])
    return tensor


def Q(spin, colour, isospin, generation):
    label = "Q"
    tensor = Tensor(label=label, indices=[spin, colour, isospin, generation])
    return tensor


def H(isospin):
    label = "H"
    tensor = Tensor(label=label, indices=[isospin])
    return tensor


def eb(isospin):
    label = "eb"
    tensor = Tensor(label=label, indices=[isospin])
    tensor.latex = r"\bar{e}"
    return tensor
