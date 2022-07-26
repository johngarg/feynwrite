#!/usr/bin/env python3

"""Defines EXOTICS dict of multiplets in Granada dictionary."""

# Depends on: tensor.py, sm.py

from tensor import Tensor


def S() -> Tensor:
    label = "S"
    latex = r"\mathcal{S}"
    tensor = Tensor(label, [], latex=latex, hypercharge=0)
    return tensor


def S1() -> Tensor:
    label = "S1"
    latex = r"\mathcal{S}_{1}"
    tensor = Tensor(label, [], latex=latex, hypercharge=1)
    return tensor


def S2() -> Tensor:
    label = "S2"
    latex = r"\mathcal{S}_{2}"
    tensor = Tensor(label, [], latex=latex, hypercharge=2)
    return tensor


def varphi(i) -> Tensor:
    label = "varphi"
    latex = r"\varphi"
    tensor = Tensor(label, [i], latex=latex)
    return tensor


def Xi(I) -> Tensor:
    label = "Xi"
    latex = r"\Xi"
    tensor = Tensor(label, [I], latex=latex)
    return tensor


def Xi1(i0, i1) -> Tensor:
    label = "Xi1"
    latex = r"\Xi_{1}"
    tensor = Tensor(label, [i0, i1], latex=latex)
    return tensor


def Theta1(i0, i1, i3) -> Tensor:
    label = "Theta1"
    latex = r"\Theta_{1}"
    tensor = Tensor(label, [i0, i1, i3], latex=latex)
    return tensor


def Theta3(i0, i1, i3) -> Tensor:
    label = "Theta3"
    latex = r"\Theta_{3}"
    tensor = Tensor(label, [i0, i1, i3], latex=latex)
    return tensor


def omega1(c0) -> Tensor:
    label = "omega1"
    latex = r"\omega_{1}"
    tensor = Tensor(label, [c0], latex=latex)
    return tensor


def omega2(c0) -> Tensor:
    label = "omega2"
    latex = r"\omega_{2}"
    tensor = Tensor(label, [c0], latex=latex)
    return tensor


def omega4(c0) -> Tensor:
    label = "omega4"
    latex = r"\omega_{4}"
    tensor = Tensor(label, [c0], latex=latex)
    return tensor


def Pi1(c0, i0) -> Tensor:
    label = "Pi1"
    latex = r"\Pi_{1}"
    tensor = Tensor(label, [c0, i0], latex=latex)
    return tensor


def Pi7(c0, i0) -> Tensor:
    label = "Pi7"
    latex = r"\Pi_{7}"
    tensor = Tensor(label, [c0, i0], latex=latex)
    return tensor


def zeta(c0, i0, i1) -> Tensor:
    label = "zeta"
    latex = r"\zeta"
    tensor = Tensor(label, [c0, i0, i1], latex=latex)
    return tensor


def Omega1(c0, c1) -> Tensor:
    label = "Omega1"
    latex = r"\Omega_{1}"
    tensor = Tensor(label, [c0, c1], latex=latex)
    return tensor


def Omega2(c0, c1) -> Tensor:
    label = "Omega2"
    latex = r"\Omega_{2}"
    tensor = Tensor(label, [c0, c1], latex=latex)
    return tensor


def Omega4(c0, c1) -> Tensor:
    label = "Omega4"
    latex = r"\Omega_{4}"
    tensor = Tensor(label, [c0, c1], latex=latex)
    return tensor


def Upsilon(c0, c1, i0, i1) -> Tensor:
    label = "Upsilon"
    latex = r"\Upsilon"
    tensor = Tensor(label, [c0, c1, i0, i1], latex=latex)
    return tensor


def Phi(c0, c1, i0) -> Tensor:
    label = "Phi"
    latex = r"\Phi"
    tensor = Tensor(label, [c0, c1, i0], latex=latex)
    return tensor
