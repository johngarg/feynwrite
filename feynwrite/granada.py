#!/usr/bin/env python3

"""Defines dictionary of multiplets in Granada dictionary."""

# Depends on: tensor.py, sm.py

from fractions import Fraction
from feynwrite.tensor import Coupling, Scalar, eps, delta, sigma, c2224
from feynwrite.sm import L, Q, H, eR, dR, uR

TERMS = []


def S() -> Scalar:
    """(1,1,0)"""
    label = "S"
    latex = r"\mathcal{S}"
    tensor = Scalar(label, [], latex=latex, hypercharge=0)
    tensor.is_self_conj = True
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
    tensor.is_self_conj = True
    return tensor


def Xi1(I) -> Scalar:
    label = "Xi1"
    latex = r"\Xi_{1}"
    tensor = Scalar(label, [I], latex=latex, hypercharge=1)
    return tensor


def Theta1(Q) -> Scalar:
    label = "Theta1"
    latex = r"\Theta_{1}"
    tensor = Scalar(label, [Q], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


def Theta3(Q) -> Scalar:
    label = "Theta3"
    latex = r"\Theta_{3}"
    tensor = Scalar(label, [Q], latex=latex, hypercharge=Fraction("3/2"))
    return tensor


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
kappaS_term = Coupling("kappaS", [], is_complex=False) * S() * H("i0").C * H("i0")
TERMS.append(kappaS_term)

# lambdaS
lambdaS_term = (
    Coupling("lambdaS", [], is_complex=False) * S() * S() * H("i0").C * H("i0")
)
TERMS.append(lambdaS_term)

# kappaS3
kappaS3_term = Coupling("kappaS3", [], is_complex=False) * S() * S() * S()
TERMS.append(kappaS3_term)

# yS1
yS1_term = (
    Coupling("yS1", "-g0 -g1", is_complex=True)
    * S1().C
    * L("s0", "i0", "g0").bar
    * L("s0", "i1", "g1").CC
    * eps("i0", "i1")
)
TERMS.append(yS1_term)

# yS2
yS2_term = (
    Coupling("yS2", "-g0 -g1", is_complex=True)
    * S2().C
    * eR("s0", "g0").bar
    * eR("s0", "g1").CC
)
TERMS.append(yS2_term)

# yvarphie
yvarphie_term = (
    Coupling("yvarphie", "-g0 -g1", is_complex=True)
    * varphi("i0").C
    * eR("s0", "g0").bar
    * L("s0", "i0", "g1")
)
TERMS.append(yvarphie_term)

# yvarphid
yvarphid_term = (
    Coupling("yvarphid", "-g0 -g1", is_complex=True)
    * varphi("i0").C
    * dR("s0", "c0", "g0").bar
    * Q("s0", "c0", "i0", "g1")
)
TERMS.append(yvarphid_term)

# yvarphiu
yvarphiu_term = (
    Coupling("yvarphiu", "-g0 -g1", is_complex=True)
    * varphi("i0").C
    * Q("s0", "c0", "i1", "g0").bar
    * uR("s0", "c0", "g1")
    * eps("i0", "i1")
)
TERMS.append(yvarphiu_term)

# lambdavarphi
lambdavarphi_term = (
    Coupling("lambdavarphi", [], is_complex=True)
    * varphi("i0").C
    * H("i0")
    * H("i1").C
    * H("i1")
)
TERMS.append(lambdavarphi_term)

# kappaXi
kappaXi_term = (
    Coupling("kappaXi", [], is_complex=False)
    * H("i0").C
    * Xi("-I0")
    * sigma("I0", "i0", "-i1")
    * H("i1")
)
TERMS.append(kappaXi_term)

# lambdaXi
lambdaXi_term = (
    Coupling("lambdaXi", [], is_complex=False)
    * Xi("-I0")
    * Xi("I0")
    * H("i0").C
    * H("i0")
)
TERMS.append(lambdaXi_term)

# lambdaXi1
lambdaXi1_term = (
    Coupling("lambdaXi1", [], is_complex=False, factor="1/4")
    * Xi1("-I0").C
    * sigma("I0", "i0", "-i1")
    * Xi1("-I1")
    * sigma("I1", "i1", "-i0")
    * H("i2").C
    * H("i2")
)
TERMS.append(lambdaXi1_term)

# lambdaXi1P
lambdaXi1P_term = (
    Coupling("lambdaXi1P", [], is_complex=False, factor="I/(2*Sqrt[2])")
    * Xi1("I0").C
    * Xi1("I1")
    * H("i0").C
    * sigma("I2", "i0", "-i1")
    * H("i1")
    * eps("-I0", "-I1", "-I2")
)
TERMS.append(lambdaXi1P_term)

# yXi1
yXi1_term = (
    Coupling("yXi1", "-g0 -g1", is_complex=True)
    * Xi1("-I0").C
    * L("s0", "i0", "g0").bar
    * L("s0", "i2", "g1").CC
    * sigma("I0", "i0", "-i1")
    * eps("i1", "i2")
)
TERMS.append(yXi1_term)

# kappaXi1
kappaXi1_term = (
    Coupling("kappaXi1", [], is_complex=True)
    * Xi1("-I0").C
    * H("i0")
    * eps("-i0", "-i1")
    * sigma("I0", "i1", "-i2")
    * H("i2")
)
TERMS.append(kappaXi1_term)

# lambdaTheta1
lambdaTheta1_term = (
    Coupling("lambdaTheta1", [], is_complex=True)
    * H("i0").C
    * H("i1")
    * H("i2").C
    * eps("i2", "i3")
    * c2224("-Q0", "i0", "-i1", "-i3")
    * Theta1("Q0")
)
TERMS.append(lambdaTheta1_term)

# lambdaTheta3
lambdaTheta3_term = (
    Coupling("lambdaTheta3", [], is_complex=True)
    * H("i0").C
    * H("i1").C
    * eps("i1", "i4")
    * H("i2").C
    * eps("i2", "i3")
    * c2224("-Q0", "i0", "-i4", "-i3")
    * Theta3("Q0")
)
TERMS.append(lambdaTheta3_term)
