#!/usr/bin/env python3

"""Defines dictionary of multiplets in Granada dictionary."""

# Depends on: tensor.py, sm.py

from fractions import Fraction
from feynwrite.tensor import Coupling, Scalar, eps, delta
from feynwrite.sm import L, Q, H, eR, dR, uR

TERMS = []


def S() -> Scalar:
    label = "S"
    latex = r"\mathcal{S}"
    tensor = Scalar(label, [], latex=latex, hypercharge=0)
    return tensor


def S1() -> Scalar:
    label = "S1"
    latex = r"\mathcal{S}_{1}"
    tensor = Scalar(label, [], latex=latex, hypercharge=1)
    return tensor


def S2() -> Scalar:
    label = "S2"
    latex = r"\mathcal{S}_{2}"
    tensor = Scalar(label, [], latex=latex, hypercharge=2)
    return tensor


def varphi(i) -> Scalar:
    label = "varphi"
    latex = r"\varphi"
    tensor = Scalar(label, [i], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


# def Xi(I) -> Tensor:
#     label = "Xi"
#     latex = r"\Xi"
#     tensor = Tensor(label, [I], latex=latex)
#     return tensor


# def Xi1(i0, i1) -> Tensor:
#     label = "Xi1"
#     latex = r"\Xi_{1}"
#     tensor = Tensor(label, [i0, i1], latex=latex)
#     return tensor


# def Theta1(i0, i1, i3) -> Tensor:
#     label = "Theta1"
#     latex = r"\Theta_{1}"
#     tensor = Tensor(label, [i0, i1, i3], latex=latex)
#     return tensor


# def Theta3(i0, i1, i3) -> Tensor:
#     label = "Theta3"
#     latex = r"\Theta_{3}"
#     tensor = Tensor(label, [i0, i1, i3], latex=latex)
#     return tensor


# def omega1(c0) -> Tensor:
#     label = "omega1"
#     latex = r"\omega_{1}"
#     tensor = Tensor(label, [c0], latex=latex)
#     return tensor


# def omega2(c0) -> Tensor:
#     label = "omega2"
#     latex = r"\omega_{2}"
#     tensor = Tensor(label, [c0], latex=latex)
#     return tensor


# def omega4(c0) -> Tensor:
#     label = "omega4"
#     latex = r"\omega_{4}"
#     tensor = Tensor(label, [c0], latex=latex)
#     return tensor


# def Pi1(c0, i0) -> Tensor:
#     label = "Pi1"
#     latex = r"\Pi_{1}"
#     tensor = Tensor(label, [c0, i0], latex=latex)
#     return tensor


# def Pi7(c0, i0) -> Tensor:
#     label = "Pi7"
#     latex = r"\Pi_{7}"
#     tensor = Tensor(label, [c0, i0], latex=latex)
#     return tensor


# def zeta(c0, i0, i1) -> Tensor:
#     label = "zeta"
#     latex = r"\zeta"
#     tensor = Tensor(label, [c0, i0, i1], latex=latex)
#     return tensor


# def Omega1(c0, c1) -> Tensor:
#     label = "Omega1"
#     latex = r"\Omega_{1}"
#     tensor = Tensor(label, [c0, c1], latex=latex)
#     return tensor


# def Omega2(c0, c1) -> Tensor:
#     label = "Omega2"
#     latex = r"\Omega_{2}"
#     tensor = Tensor(label, [c0, c1], latex=latex)
#     return tensor


# def Omega4(c0, c1) -> Tensor:
#     label = "Omega4"
#     latex = r"\Omega_{4}"
#     tensor = Tensor(label, [c0, c1], latex=latex)
#     return tensor


# def Upsilon(c0, c1, i0, i1) -> Tensor:
#     label = "Upsilon"
#     latex = r"\Upsilon"
#     tensor = Tensor(label, [c0, c1, i0, i1], latex=latex)
#     return tensor


# def Phi(c0, c1, i0) -> Tensor:
#     label = "Phi"
#     latex = r"\Phi"
#     tensor = Tensor(label, [c0, c1, i0], latex=latex)
#     return tensor

# kappaS
kappaS = Coupling("kappaS", [], is_complex=False)
kappaS_term = kappaS * S() * H("i0").C * H("i0")
TERMS.append(kappaS_term)

# lambdaS
lambdaS = Coupling("lambdaS", [], is_complex=False)
lambdaS_term = lambdaS * S() * S() * H("i0").C * H("i0")
TERMS.append(lambdaS_term)

# kappaS3
kappaS3 = Coupling("kappaS3", [], is_complex=False)
kappaS3_term = kappaS3 * S() * S() * S()
TERMS.append(kappaS3_term)

# yS1
yS1 = Coupling("yS1", "-g0 -g1", is_complex=True)
yS1_term = (
    yS1 * S1().C * L("s0", "i0", "g0").bar * L("s0", "i1", "g1").CC * eps("i0", "i1")
)
TERMS.append(yS1_term)

# yvarphie
yvarphie = Coupling("yvarphie", "-g0 -g1", is_complex=True)
yvarphie_term = yvarphie * varphi("i0").C * eR("s0", "g0").bar * L("s0", "i0", "g1")
TERMS.append(yvarphie_term)

# yvarphid
yvarphid = Coupling("yvarphid", "-g0 -g1", is_complex=True)
yvarphid_term = (
    yvarphid * varphi("i0").C * dR("s0", "c0", "g0").bar * Q("s0", "c0", "i0", "g1")
)
TERMS.append(yvarphid_term)

# yvarphiu
yvarphiu = Coupling("yvarphiu", "-g0 -g1", is_complex=True)
yvarphiu_term = (
    yvarphiu
    * varphi("i0").C
    * Q("s0", "c0", "i1", "g0").bar
    * uR("s0", "c0", "g1")
    * eps("i0", "i1")
)
TERMS.append(yvarphiu_term)

# lambdavarphi
lambdavarphi = Coupling("lambdavarphi", "", is_complex=True)
lambdavarphi_term = lambdavarphi * varphi("i0").C * H("i0") * H("i1").C * H("i1")
TERMS.append(lambdavarphi_term)
