#!/usr/bin/env python3

"""Defines dictionary of multiplets in Granada dictionary."""

# Depends on: tensor.py, sm.py

from fractions import Fraction
from feynwrite.tensor import Coupling, Scalar, eps, delta, sigma
from feynwrite.sm import L, Q, H, eR, dR, uR

TERMS = []


def S() -> Scalar:
    """(1,1,0)"""
    label = "S"
    latex = r"\mathcal{S}"
    tensor = Scalar(label, [], latex=latex, hypercharge=0)
    return tensor


def S1() -> Scalar:
    """(1,1,1)"""
    label = "S1"
    latex = r"\mathcal{S}_{1}"
    tensor = Scalar(label, [], latex=latex, hypercharge=1)
    return tensor


def S2() -> Scalar:
    """(1,1,2)"""
    label = "S2"
    latex = r"\mathcal{S}_{2}"
    tensor = Scalar(label, [], latex=latex, hypercharge=2)
    return tensor


def varphi(i) -> Scalar:
    """(1,2,1/2)"""
    label = "varphi"
    latex = r"\varphi"
    tensor = Scalar(label, [i], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


def Xi(I) -> Scalar:
    """(1,3,0)"""
    label = "Xi"
    latex = r"\Xi"
    tensor = Scalar(label, [I], latex=latex, hypercharge=0)
    return tensor


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

# yS2
yS2 = Coupling("yS2", "-g0 -g1", is_complex=True)
yS2_term = yS2 * S2().C * eR("s0", "g0").bar * eR("s0", "g1").CC
TERMS.append(yS2_term)

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
lambdavarphi = Coupling("lambdavarphi", [], is_complex=True)
lambdavarphi_term = lambdavarphi * varphi("i0").C * H("i0") * H("i1").C * H("i1")
TERMS.append(lambdavarphi_term)

# kappaXi
kappaXi = Coupling("kappaXi", [], is_complex=False)
kappaXi_term = kappaXi * H("i0").C * Xi("-I0") * sigma("I0", "i0", "-i1") * H("i1")
TERMS.append(kappaXi_term)

# lambdaXi
lambdaXi = Coupling("lambdaXi", [], is_complex=False, factor="1 / 2")
lambdaXi_term = lambdaXi * Xi("-I0").C * Xi("I0") * H("i0").C * H("i0")
TERMS.append(lambdaXi_term)

# lambdaXiP
lambdaXiP = Coupling("lambdaXiP", [], is_complex=False, factor="I / (2 Sqrt[2])")
lambdaXiP_term = (
    lambdaXiP
    * Xi("I0").C
    * Xi("I1")
    * H("i0").C
    * sigma("I2", "i0", "-i1")
    * H("i1")
    * eps("-I0", "-I1", "-I2")
)
TERMS.append(lambdaXiP_term)
