#!/usr/bin/env python3

"""Defines the multiplets in the Granada dictionary and the terms in the Lagrangian necessary for single-field one-loop graphs."""

# Depends on: tensor.py, sm.py

from fractions import Fraction
from sympy import sqrt, I, Rational
from feynwrite.tensor import (
    Coupling,
    Scalar,
    Fermion,
    Vector,
    eps,
    delta,
    sigma,
    c2224,
    c344,
    t2244,
    K,
    Ga,
    lambda_,
)
from feynwrite.sm import L, Q, H, eR, dR, uR, DH, FS

TERMS = []


def S() -> Scalar:
    """(1,1,0)"""
    label = "Granada" + "S"
    latex = r"\mathcal{S}"
    tensor = Scalar(label, [], latex=latex, hypercharge=0)
    tensor.is_self_conj = True
    return tensor


def S1() -> Scalar:
    """(1,1,1)"""
    label = "Granada" + "S1"
    latex = r"\mathcal{S}_{1}"
    tensor = Scalar(label, [], latex=latex, hypercharge=1)
    return tensor


def S2() -> Scalar:
    """(1,1,2)"""
    label = "Granada" + "S2"
    latex = r"\mathcal{S}_{2}"
    tensor = Scalar(label, [], latex=latex, hypercharge=2)
    return tensor


def varphi(i) -> Scalar:
    """(1,2,1/2)"""
    label = "Granada" + "varphi"
    latex = r"\varphi"
    tensor = Scalar(label, [i], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


def Xi(I) -> Scalar:
    """(1,3,0)"""
    label = "Granada" + "Xi"
    latex = r"\Xi"
    tensor = Scalar(label, [I], latex=latex, hypercharge=0)
    tensor.is_self_conj = True
    return tensor


def Xi1(I) -> Scalar:
    label = "Granada" + "Xi1"
    latex = r"\Xi_{1}"
    tensor = Scalar(label, [I], latex=latex, hypercharge=1)
    return tensor


def Theta1(Q) -> Scalar:
    label = "Granada" + "Theta1"
    latex = r"\Theta_{1}"
    tensor = Scalar(label, [Q], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


def Theta3(Q) -> Scalar:
    label = "Granada" + "Theta3"
    latex = r"\Theta_{3}"
    tensor = Scalar(label, [Q], latex=latex, hypercharge=Fraction("3/2"))
    return tensor


def omega1(c) -> Scalar:
    label = "Granada" + "omega1"
    latex = r"\omega_{1}"
    tensor = Scalar(label, [c], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def omega2(c) -> Scalar:
    label = "Granada" + "omega2"
    latex = r"\omega_{2}"
    tensor = Scalar(label, [c], latex=latex, hypercharge=Fraction("2/3"))
    return tensor


def omega4(c) -> Scalar:
    label = "Granada" + "omega4"
    latex = r"\omega_{4}"
    tensor = Scalar(label, [c], latex=latex, hypercharge=Fraction("-4/3"))
    return tensor


def Pi1(c, i) -> Scalar:
    label = "Granada" + "Pi1"
    latex = r"\Pi_{1}"
    tensor = Scalar(label, [c, i], latex=latex, hypercharge=Fraction("1/6"))
    return tensor


def Pi7(c, i) -> Scalar:
    label = "Granada" + "Pi7"
    latex = r"\Pi_{7}"
    tensor = Scalar(label, [c, i], latex=latex, hypercharge=Fraction("7/6"))
    return tensor


def zeta(c, I) -> Scalar:
    label = "Granada" + "zeta"
    latex = r"\zeta"
    tensor = Scalar(label, [c, I], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def Omega1(X) -> Scalar:
    label = "Granada" + "Omega1"
    latex = r"\Omega_{1}"
    tensor = Scalar(label, [X], latex=latex, hypercharge=Fraction("1/3"))
    return tensor


def Omega2(X) -> Scalar:
    label = "Granada" + "Omega2"
    latex = r"\Omega_{2}"
    tensor = Scalar(label, [X], latex=latex, hypercharge=Fraction("-2/3"))
    return tensor


def Omega4(X) -> Scalar:
    label = "Granada" + "Omega4"
    latex = r"\Omega_{4}"
    tensor = Scalar(label, [X], latex=latex, hypercharge=Fraction("4/3"))
    return tensor


def Upsilon(X, I) -> Scalar:
    label = "Granada" + "Upsilon"
    latex = r"\Upsilon"
    tensor = Scalar(label, [X, I], latex=latex, hypercharge=Fraction("1/3"))
    return tensor


def Phi(C, i) -> Scalar:
    label = "Granada" + "Phi"
    latex = r"\Phi"
    tensor = Scalar(label, [C, i], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


def N(s) -> Fermion:
    label = "Granada" + "N"
    latex = "N"
    tensor = Fermion(label, [s], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor


def ND(s) -> Fermion:
    """Dirac fermion (1,1,0) with imposed fermion-number symmetry."""
    label = "Granada" + "ND"
    latex = "N_D"
    tensor = Fermion(label, [s], latex=latex, hypercharge=0, is_self_conj=False)
    return tensor


def E(s) -> Fermion:
    label = "Granada" + "E"
    latex = "E"
    tensor = Fermion(label, [s], latex=latex, hypercharge=-1)
    return tensor


def Delta1(s, i) -> Fermion:
    label = "Granada" + "Delta1"
    latex = r"\Delta_{1}"
    tensor = Fermion(label, [s, i], latex=latex, hypercharge=Fraction("-1/2"))
    return tensor


def Delta3(s, i) -> Fermion:
    label = "Granada" + "Delta3"
    latex = r"\Delta_{3}"
    tensor = Fermion(label, [s, i], latex=latex, hypercharge=Fraction("-3/2"))
    return tensor


def Sigma(s, I) -> Fermion:
    label = "Granada" + "Sigma"
    latex = r"\Sigma"
    tensor = Fermion(label, [s, I], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor


def SigmaD(s, I) -> Fermion:
    """Dirac fermion (1,3,0) with imposed fermion-number symmetry."""
    label = "Granada" + "SigmaD"
    latex = r"\Sigma_D"
    tensor = Fermion(label, [s, I], latex=latex, hypercharge=0, is_self_conj=False)
    return tensor


def Sigma1(s, I) -> Fermion:
    label = "Granada" + "Sigma1"
    latex = r"\Sigma_{1}"
    tensor = Fermion(label, [s, I], latex=latex, hypercharge=-1)
    return tensor


def U(s, a) -> Fermion:
    label = "Granada" + "U"
    latex = r"U"
    tensor = Fermion(label, [s, a], latex=latex, hypercharge=Fraction("2/3"))
    return tensor


def D(s, a) -> Fermion:
    label = "Granada" + "D"
    latex = r"D"
    tensor = Fermion(label, [s, a], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def Q1(s, a, i) -> Fermion:
    label = "Granada" + "Q1"
    latex = r"Q_{1}"
    tensor = Fermion(label, [s, a, i], latex=latex, hypercharge=Fraction("1/6"))
    return tensor


def Q5(s, a, i) -> Fermion:
    label = "Granada" + "Q5"
    latex = r"Q_{5}"
    tensor = Fermion(label, [s, a, i], latex=latex, hypercharge=Fraction("-5/6"))
    return tensor


def Q7(s, a, i) -> Fermion:
    label = "Granada" + "Q7"
    latex = r"Q_{7}"
    tensor = Fermion(label, [s, a, i], latex=latex, hypercharge=Fraction("7/6"))
    return tensor


def T1(s, a, I) -> Fermion:
    label = "Granada" + "T1"
    latex = r"T_{1}"
    tensor = Fermion(label, [s, a, I], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def T2(s, a, I) -> Fermion:
    label = "Granada" + "T2"
    latex = r"T_{2}"
    tensor = Fermion(label, [s, a, I], latex=latex, hypercharge=Fraction("2/3"))
    return tensor

def VB(l) -> Vector:
    label = "Granada" + "VB"
    latex = r"\mathcal{B}"
    tensor = Vector(label, [l], latex=latex, hypercharge=0, is_self_conj=True)
    tensor.is_self_conj = True
    return tensor

def VB1(l) -> Vector:
    label = "Granada" + "VB1"
    latex = r"\mathcal{B}_{1}"
    tensor = Vector(label, [l], latex=latex, hypercharge=1)
    return tensor

def VW(l, I) -> Vector:
    label = "Granada" + "VW"
    latex = r"\mathcal{W}"
    tensor = Vector(label, [l, I], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor

def VW1(l, I) -> Vector:
    label = "Granada" + "VW1"
    latex = r"\mathcal{W}_{1}"
    tensor = Vector(label, [l, I], latex=latex, hypercharge=1)
    return tensor

def VG(l, C) -> Vector:
    label = "Granada" + "VG"
    latex = r"\mathcal{G}"
    tensor = Vector(label, [l, C], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor

def VG1(l, C) -> Vector:
    label = "Granada" + "VG1"
    latex = r"\mathcal{G}_{1}"
    tensor = Vector(label, [l, C], latex=latex, hypercharge=1)
    return tensor

def VH(l, C, I) -> Vector:
    label = "Granada" + "VH"
    latex = r"\mathcal{H}"
    tensor = Vector(label, [l, C, I], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor

def VL1(l, i) -> Vector:
    label = "Granada" + "VL1"
    latex = r"\mathcal{L}_{1}"
    tensor = Vector(label, [l, i], latex=latex, hypercharge=Fraction("1/2"))
    return tensor

def VL3(l, i) -> Vector:
    label = "Granada" + "VL3"
    latex = r"\mathcal{L}_{3}"
    tensor = Vector(label, [l, i], latex=latex, hypercharge=Fraction("-3/2"))
    return tensor

def VU2(l, c) -> Vector:
    label = "Granada" + "VU2"
    latex = r"\mathcal{U}_{2}"
    tensor = Vector(label, [l, c], latex=latex, hypercharge=Fraction("2/3"))
    return tensor

def VU5(l, c) -> Vector:
    label = "Granada" + "VU5"
    latex = r"\mathcal{U}_{5}"
    tensor = Vector(label, [l, c], latex=latex, hypercharge=Fraction("5/3"))
    return tensor

def VQ1(l, c, i) -> Vector:
    label = "Granada" + "VQ1"
    latex = r"\mathcal{Q}_{1}"
    tensor = Vector(label, [l, c, i], latex=latex, hypercharge=Fraction("1/6"))
    return tensor

def VQ5(l, c, i) -> Vector:
    label = "Granada" + "VQ5"
    latex = r"\mathcal{Q}_{5}"
    tensor = Vector(label, [l, c, i], latex=latex, hypercharge=Fraction("-5/6"))
    return tensor

def VX(l, c, I) -> Vector:
    label = "Granada" + "VX"
    latex = r"\mathcal{X}"
    tensor = Vector(label, [l, c, I], latex=latex, hypercharge=Fraction("2/3"))
    return tensor

## VY1 and VY5 are in the 6* colour rep
def VY1(l, X, i) -> Vector:
    label = "Granada" + "VY1"
    latex = r"\mathcal{Y}_{1}"
    tensor = Vector(label, [l, X, i], latex=latex, hypercharge=Fraction("1/6"))
    return tensor

def VY5(l, X, i) -> Vector:
    label = "Granada" + "VY5"
    latex = r"\mathcal{Y}_{5}"
    tensor = Vector(label, [l, X, i], latex=latex, hypercharge=Fraction("-5/6"))
    return tensor

### SCALARS

# kappaS
kappaS_term = (
    Coupling("kappaS", [], is_complex=False, latex="\\kappa_{\\mathcal{S}}")
    * S()
    * H("i0").C
    * H("i0")
)
TERMS.append(kappaS_term)

# lambdaS
lambdaS_term = (
    Coupling("lambdaS", [], is_complex=False, latex="\\lambda_{\\mathcal{S}}")
    * S()
    * S()
    * H("i0").C
    * H("i0")
)
TERMS.append(lambdaS_term)

# kappaS3
kappaS3_term = (
    Coupling("kappaS3", [], is_complex=False, latex="\\kappa_{\\mathcal{S}3}")
    * S()
    * S()
    * S()
)
TERMS.append(kappaS3_term)

# yS1
yS1_term = (
    Coupling("yS1", "-g0 -g1", is_complex=True, latex="[y_{\\mathcal{S}_1}]")
    * S1().C
    * L("s0", "i0", "g0").bar
    * L("s0", "i1", "g1").CC
    * eps("i0", "i1")
)
TERMS.append(yS1_term)

# yS2
yS2_term = (
    Coupling("yS2", "-g0 -g1", is_complex=True, latex="[y_{\\mathcal{S}_2}]")
    * S2().C
    * eR("s0", "g0").bar
    * eR("s0", "g1").CC
)
TERMS.append(yS2_term)

# yvarphie
yvarphie_term = (
    Coupling("yvarphie", "-g0 -g1", is_complex=True, latex="[y_{\\varphi e}]")
    * varphi("i0").C
    * eR("s0", "g0").bar
    * L("s0", "i0", "g1")
)
TERMS.append(yvarphie_term)

# yvarphid
yvarphid_term = (
    Coupling("yvarphid", "-g0 -g1", is_complex=True, latex="[y_{\\varphi d}]")
    * varphi("i0").C
    * dR("s0", "c0", "g0").bar
    * Q("s0", "c0", "i0", "g1")
)
TERMS.append(yvarphid_term)

# yvarphiu
yvarphiu_term = (
    Coupling("yvarphiu", "-g0 -g1", is_complex=True, latex="[y_{\\varphi u}]")
    * varphi("i0").C
    * Q("s0", "c0", "i1", "g0").bar
    * uR("s0", "c0", "g1")
    * eps("i0", "i1")
)
TERMS.append(yvarphiu_term)

# lambdavarphi
lambdavarphi_term = (
    Coupling("lambdavarphi", [], is_complex=True, latex="\\lambda_{\\varphi}")
    * varphi("i0").C
    * H("i0")
    * H("i1").C
    * H("i1")
)
TERMS.append(lambdavarphi_term)

# kappaXi
kappaXi_term = (
    Coupling("kappaXi", [], is_complex=False, latex="\\kappa_{\\Xi}")
    * H("i0").C
    * Xi("-I0")
    * sigma("I0", "i0", "-i1")
    * H("i1")
)
TERMS.append(kappaXi_term)

# lambdaXi
lambdaXi_term = (
    Coupling("lambdaXi", [], is_complex=False, latex="\\lambda_{\\Xi}")
    * Xi("-I0")
    * Xi("I0")
    * H("i0").C
    * H("i0")
)
TERMS.append(lambdaXi_term)

# lambdaXi1
lambdaXi1_term = (
    Coupling(
        "lambdaXi1",
        [],
        is_complex=False,
        factor=Rational("1/4"),
        latex="\\lambda_{\\Xi_1}",
    )
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
    Coupling(
        "lambdaXi1P",
        [],
        is_complex=False,
        factor=I / (2 * sqrt(2)),
        latex="{\\lambda_{\\Xi_1}^\\prime}",
    )
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
    Coupling("yXi1", "-g0 -g1", is_complex=True, latex="[y_{\\Xi_1}]")
    * Xi1("-I0").C
    * L("s0", "i0", "g0").bar
    * L("s0", "i2", "g1").CC
    * sigma("I0", "i0", "-i1")
    * eps("i1", "i2")
)
TERMS.append(yXi1_term)

# kappaXi1
kappaXi1_term = (
    Coupling("kappaXi1", [], is_complex=True, latex="\\kappa_{\\Xi_1}")
    * Xi1("-I0").C
    * H("i0")
    * eps("-i0", "-i1")
    * sigma("I0", "i1", "-i2")
    * H("i2")
)
TERMS.append(kappaXi1_term)

# lambdaTheta1
lambdaTheta1_term = (
    Coupling("lambdaTheta1", [], is_complex=True, latex="\\lambda_{\\Theta_1}")
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
    Coupling("lambdaTheta3", [], is_complex=True, latex="\\lambda_{\\Theta_3}")
    * H("i0").C
    * H("i1").C
    * eps("i1", "i4")
    * H("i2").C
    * eps("i2", "i3")
    * c2224("-Q0", "i0", "-i4", "-i3")
    * Theta3("Q0")
)
TERMS.append(lambdaTheta3_term)

# yqlomega1
yqlomega1_term = (
    Coupling(
        "yqlomega1", ["-g0", "-g1"], is_complex=True, latex="[y_{q\\ell \\Omega_1}]"
    )
    * omega1("c0").C
    * Q("s0", "c0", "i0", "g0").CC.bar
    * L("s0", "i1", "g1")
    * eps("-i0", "-i1")
)
TERMS.append(yqlomega1_term)

# yqqomega1
yqqomega1_term = (
    Coupling("yqqomega1", ["-g0", "-g1"], is_complex=True, latex="[y_{qq \\Omega_1}]")
    * omega1("c0").C
    * Q("s0", "c1", "i0", "g0").bar
    * Q("s0", "c2", "i1", "g1").CC
    * eps("i0", "i1")
    * eps("c0", "c1", "c2")
)
TERMS.append(yqqomega1_term)

# yeuomega1
yeuomega1_term = (
    Coupling("yeuomega1", ["-g0", "-g1"], is_complex=True, latex="[y_{e u \\Omega_1}]")
    * omega1("c0").C
    * eR("s0", "g0").CC.bar
    * uR("s0", "c0", "g1")
)
TERMS.append(yeuomega1_term)

# yduomega1
yduomega1_term = (
    Coupling("yduomega1", ["-g0", "-g1"], is_complex=True, latex="[y_{d u \\Omega_1}]")
    * omega1("c0").C
    * dR("s0", "c1", "g0").bar
    * uR("s0", "c2", "g1").CC
    * eps("c0", "c1", "c2")
)
TERMS.append(yduomega1_term)

# yomega2
yomega2_term = (
    Coupling("yomega2", ["-g0", "-g1"], is_complex=True, latex="[y_{\\Omega_2}]")
    * omega2("c0").C
    * dR("s0", "c1", "g0").bar
    * dR("s0", "c2", "g1").CC
    * eps("c0", "c1", "c2")
)
TERMS.append(yomega2_term)

# yedomega4
yedomega4_term = (
    Coupling("yedomega4", ["-g0", "-g1"], is_complex=True, latex="[y_{e d \\Omega_4}]")
    * omega4("c0").C
    * eR("s0", "g0").CC.bar
    * dR("s0", "c0", "g1")
)
TERMS.append(yedomega4_term)

# yuuomega4
yuuomega4_term = (
    Coupling("yuuomega4", ["-g0", "-g1"], is_complex=True, latex="[y_{u u \\Omega_4}]")
    * omega4("c0").C
    * uR("s0", "c1", "g0").bar
    * uR("s0", "c2", "g1").CC
    * eps("c0", "c1", "c2")
)
TERMS.append(yuuomega4_term)

# yPi1
yPi1_term = (
    Coupling("yPi1", ["-g0", "-g1"], is_complex=True, latex="[y_{\\Pi_1}]")
    * Pi1("c0", "i0").C
    * eps("i0", "i1")
    * L("s0", "i1", "g0").bar
    * dR("s0", "c0", "g1")
)
TERMS.append(yPi1_term)

# yluPi7
yluPi7_term = (
    Coupling("yluPi7", ["-g0", "-g1"], is_complex=True, latex="[y_{\\ell u \\Pi_7}]")
    * Pi7("c0", "i0").C
    * eps("i0", "i1")
    * L("s0", "i1", "g0").bar
    * uR("s0", "c0", "g1")
)
TERMS.append(yluPi7_term)

# yeqPi7
yeqPi7_term = (
    Coupling("yeqPi7", ["-g0", "-g1"], is_complex=True, latex="[y_{e q \\Pi_7}]")
    * Pi7("c0", "i0").C
    * eR("s0", "g0").bar
    * Q("s0", "c0", "i0", "g1")
)
TERMS.append(yeqPi7_term)

# yqlzeta
yqlzeta_term = (
    Coupling("yqlzeta", ["-g0", "-g1"], is_complex=True, latex="[y_{q\\ell \\zeta}]")
    * zeta("c0", "-I0").C
    * Q("s0", "c0", "i0", "g0").CC.bar
    * L("s0", "i1", "g1")
    * eps("-i0", "-i2")
    * sigma("I0", "i2", "-i1")
)
TERMS.append(yqlzeta_term)

# yqqzeta
yqqzeta_term = (
    Coupling("yqqzeta", ["-g0", "-g1"], is_complex=True, latex="[y_{qq \\zeta}]")
    * zeta("c0", "-I0").C
    * Q("s0", "c1", "i0", "g0").bar
    * Q("s0", "c2", "i1", "g1").CC
    * sigma("I0", "i0", "-i2")
    * eps("i2", "i1")
    * eps("c0", "c1", "c2")
)
TERMS.append(yqqzeta_term)

# yudOmega1
yudOmega1_term = (
    Coupling("yudOmega1", ["-g0", "-g1"], is_complex=True, latex="[y_{u d \\Omega_1}]")
    * Omega1("-X0").C
    * K("X0", "-c0", "-c1")
    * uR("s0", "c0", "g0").CC.bar
    * dR("s0", "c1", "g1")
)
TERMS.append(yudOmega1_term)


# yqqOmega1
yqqOmega1_term = (
    Coupling("yqqOmega1", ["-g0", "-g1"], is_complex=True, latex="[y_{q q \\Omega_1}]")
    * Omega1("-X0").C
    * K("X0", "-c0", "-c1")
    * Q("s0", "c0", "i0", "g0").CC.bar
    * Q("s0", "c1", "i1", "g1")
    * eps("-i0", "-i1")
)
TERMS.append(yqqOmega1_term)

# yOmega2
yOmega2_term = (
    Coupling("yOmega2", ["-g0", "-g1"], is_complex=True, latex="[y_{\\Omega_2}]")
    * Omega2("-X0").C
    * K("X0", "-c0", "-c1")
    * dR("s0", "c0", "g0").CC.bar
    * dR("s0", "c1", "g1")
)
TERMS.append(yOmega2_term)

# yOmega4
yOmega4_term = (
    Coupling("yOmega4", ["-g0", "-g1"], is_complex=True, latex="[y_{\\Omega_4}]")
    * Omega4("-X0").C
    * K("X0", "-c0", "-c1")
    * uR("s0", "c0", "g0").CC.bar
    * uR("s0", "c1", "g1")
)
TERMS.append(yOmega4_term)

# yUpsilon
yUpsilon_term = (
    Coupling("yUpsilon", ["-g0", "-g1"], is_complex=True, latex="[y_{\\Upsilon}]")
    * Upsilon("-X0", "-I0").C
    * Q("s0", "c0", "i0", "g0").CC.bar
    * Q("s0", "c1", "i1", "g1")
    * eps("-i0", "-i2")
    * sigma("I0", "i2", "-i1")
    * K("X0", "-c0", "-c1")
)
TERMS.append(yUpsilon_term)

# yquPhi
yquPhi_term = (
    # Introduce factor of 1/2 since in paper T_A is used instead of Gell-mann
    # matrices
    Coupling(
        "yquPhi",
        ["-g0", "-g1"],
        is_complex=True,
        factor=Rational("1/2"),
        latex="[y_{q u \\Phi}]",
    )
    * Phi("-C0", "i0").C
    * Q("s0", "c0", "i1", "g0").bar
    * uR("s0", "c1", "g1")
    * eps("i0", "i1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(yquPhi_term)

# yqdPhi
ydqPhi_term = (
    # Introduce factor of 1/2 since in paper T_A is used instead of Gell-mann
    # matrices
    Coupling(
        "ydqPhi",
        ["-g0", "-g1"],
        is_complex=True,
        factor=Rational("1/2"),
        latex="[y_{q d \\Phi}]",
    )
    * Phi("-C0", "i0").C
    * dR("s0", "c0", "g0").bar
    * Q("s0", "c1", "i0", "g1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(ydqPhi_term)

### FERMIONS

## LEPTONS

# lambdaN
lambdaN_term = (
    Coupling("lambdaN", ["-g0"], is_complex=True, latex="\\lambda_N")
    * N("s0").right.bar
    * L("s0", "i0", "g0")
    * eps("-i0", "-i1")
    * H("i1")
)
TERMS.append(lambdaN_term)

# lambdaE
lambdaE_term = (
    Coupling("lambdaE", ["-g0"], is_complex=True, latex="\\lambda_E")
    * E("s0").right.bar
    * L("s0", "i0", "g0")
    * H("i0").C
)
TERMS.append(lambdaE_term)

# lambdaDelta1
lambdaDelta1_term = (
    Coupling("lambdaDelta1", ["-g0"], is_complex=True, latex="\\lambda_{\\Delta_1}")
    * Delta1("s0", "i0").left.bar
    * eR("s0", "g0")
    * H("i0")
)
TERMS.append(lambdaDelta1_term)

# lambdaDelta3
lambdaDelta3_term = (
    Coupling("lambdaDelta3", ["-g0"], is_complex=True, latex="\\lambda_{\\Delta_3}")
    * Delta3("s0", "i0").left.bar
    * eR("s0", "g0")
    * H("i1").C
    * eps("i0", "i1")
)
TERMS.append(lambdaDelta3_term)

# lambdaSigma
lambdaSigma_term = (
    Coupling(
        "lambdaSigma",
        ["-g0"],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\lambda_{\\Sigma}",
    )
    * Sigma("s0", "-I0").right.bar
    * L("s0", "i4", "g0")
    * sigma("I0", "i2", "-i4")
    * H("i3")
    * eps("-i3", "-i2")
)
TERMS.append(lambdaSigma_term)

# lambdaSigma
lambdaSigma1_term = (
    Coupling(
        "lambdaSigma1",
        ["-g0"],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\lambda_{\\Sigma_1}",
    )
    * Sigma1("s0", "-I0").right.bar
    * L("s0", "i4", "g0")
    * sigma("I0", "i3", "-i4")
    * H("i3").C
)
TERMS.append(lambdaSigma1_term)

## QUARKS

# lambdaU
lambdaU_term = (
    Coupling("lambdaU", ["-g0"], is_complex=True, latex="\\lambda_U")
    * U("s0", "c0").right.bar
    * Q("s0", "c0", "i0", "g0")
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaU_term)

# lambdaD
lambdaD_term = (
    Coupling("lambdaD", ["-g0"], is_complex=True, latex="\\lambda_D")
    * D("s0", "c0").right.bar
    * Q("s0", "c0", "i0", "g0")
    * H("i0").C
)
TERMS.append(lambdaD_term)

# lambdauQ1
lambdauQ1_term = (
    Coupling("lambdauQ1", ["-g0"], is_complex=True, latex="\\lambda_{u Q_1}")
    * Q1("s0", "c0", "i0").left.bar
    * uR("s0", "c0", "g0")
    * H("i1").C
    * eps("i0", "i1")
)
TERMS.append(lambdauQ1_term)

# lambdadQ1
lambdadQ1_term = (
    Coupling("lambdadQ1", ["-g0"], is_complex=True, latex="\\lambda_{d Q_1}")
    * Q1("s0", "c0", "i0").left.bar
    * dR("s0", "c0", "g0")
    * H("i0")
)
TERMS.append(lambdadQ1_term)

# lambdaQ5
lambdaQ5_term = (
    Coupling("lambdaQ5", ["-g0"], is_complex=True, latex="\\lambda_{Q_5}")
    * Q5("s0", "c0", "i0").left.bar
    * dR("s0", "c0", "g0")
    * H("i1").C
    * eps("i0", "i1")
)
TERMS.append(lambdaQ5_term)

# lambdaQ7
lambdaQ7_term = (
    Coupling("lambdaQ7", ["-g0"], is_complex=True, latex="\\lambda_{Q_7}")
    * Q7("s0", "c0", "i0").left.bar
    * uR("s0", "c0", "g0")
    * H("i0")
)
TERMS.append(lambdaQ7_term)

# lambdaT1
lambdaT1_term = (
    Coupling(
        "lambdaT1",
        ["-g0"],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\lambda_{T_1}",
    )
    * T1("s0", "c0", "-I0").right.bar
    * Q("s0", "c0", "i0", "g0")
    * H("i1").C
    * sigma("I0", "i1", "-i0")
)
TERMS.append(lambdaT1_term)

# lambdaT2
lambdaT2_term = (
    Coupling(
        "lambdaT2",
        ["-g0"],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\lambda_{T_2}",
    )
    * T2("s0", "c0", "-I0").right.bar
    * Q("s0", "c0", "i0", "g0")
    * H("i1")
    * eps("-i1", "-i2")
    * sigma("I0", "i2", "-i0")
)
TERMS.append(lambdaT2_term)


## Additional terms in the scalar potential (hatted in the paper)

# lambda_hat_S1
lambda_hat_S1_term = (
    Coupling(
        "lambdaHatS1", [], is_complex=False, latex="\\hat{\\lambda}_{\\mathcal{S}_1}"
    )
    * H("i0").C
    * H("i0")
    * S1().C
    * S1()
)
TERMS.append(lambda_hat_S1_term)

# lambda_hat_S2
lambda_hat_S2_term = (
    Coupling(
        "lambdaHatS2", [], is_complex=False, latex="\\hat{\\lambda}_{\\mathcal{S}_2}"
    )
    * H("i0").C
    * H("i0")
    * S2().C
    * S2()
)
TERMS.append(lambda_hat_S2_term)

# lambda_hat_varphi
lambda_hat_varphi_term = (
    Coupling(
        "lambdaHatvarphi", [], is_complex=False, latex="\\hat{\\lambda}_{\\varphi}"
    )
    * H("i0").C
    * H("i0")
    * varphi("i1").C
    * varphi("i1")
)
TERMS.append(lambda_hat_varphi_term)

# lambda_hat_Theta1
lambda_hat_Theta1_term = (
    Coupling(
        "lambdaHatTheta1", [], is_complex=False, latex="\\hat{\\lambda}_{\\Theta_1}"
    )
    * H("i0").C
    * H("i0")
    * Theta1("-Q0").C
    * Theta1("Q0")
)
TERMS.append(lambda_hat_Theta1_term)

# lambda_hat_Theta3
lambda_hat_Theta3_term = (
    Coupling(
        "lambdaHatTheta3", [], is_complex=False, latex="\\hat{\\lambda}_{\\Theta_3}"
    )
    * H("i0").C
    * H("i0")
    * Theta3("-Q0").C
    * Theta3("Q0")
)
TERMS.append(lambda_hat_Theta3_term)

# lambda_hat_omega1
lambda_hat_omega1_term = (
    Coupling(
        "lambdaHatomega1", [], is_complex=False, latex="\\hat{\\lambda}_{\\omega_1}"
    )
    * H("i0").C
    * H("i0")
    * omega1("c0").C
    * omega1("c0")
)
TERMS.append(lambda_hat_omega1_term)

# lambda_hat_omega2
lambda_hat_omega2_term = (
    Coupling(
        "lambdaHatomega2", [], is_complex=False, latex="\\hat{\\lambda}_{\\omega_2}"
    )
    * H("i0").C
    * H("i0")
    * omega2("c0").C
    * omega2("c0")
)
TERMS.append(lambda_hat_omega2_term)

# lambda_hat_omega4
lambda_hat_omega4_term = (
    Coupling(
        "lambdaHatomega4", [], is_complex=False, latex="\\hat{\\lambda}_{\\omega_4}"
    )
    * H("i0").C
    * H("i0")
    * omega4("c0").C
    * omega4("c0")
)
TERMS.append(lambda_hat_omega4_term)


# lambda_hat_Pi1
lambda_hat_Pi1_term = (
    Coupling("lambdaHatPi1", [], is_complex=False, latex="\\hat{\\lambda}_{\\Pi_1}")
    * H("i0").C
    * H("i0")
    * Pi1("c0", "i1").C
    * Pi1("c0", "i1")
)
TERMS.append(lambda_hat_Pi1_term)

# lambda_hat_Pi7
lambda_hat_Pi7_term = (
    Coupling("lambdaHatPi7", [], is_complex=False, latex="\\hat{\\lambda}_{\\Pi_7}")
    * H("i0").C
    * H("i0")
    * Pi7("c0", "i1").C
    * Pi7("c0", "i1")
)
TERMS.append(lambda_hat_Pi7_term)

# lambda_hat_zeta
lambda_hat_zeta_term = (
    Coupling("lambdaHatzeta", [], is_complex=False, latex="\\hat{\\lambda}_{\\zeta}")
    * H("i0").C
    * H("i0")
    * zeta("c0", "-I0").C
    * zeta("c0", "I0")
)
TERMS.append(lambda_hat_zeta_term)

# lambda_hat_Omega1
lambda_hat_Omega1_term = (
    Coupling(
        "lambdaHatOmega1", [], is_complex=False, latex="\\hat{\\lambda}_{\\Omega_1}"
    )
    * H("i0").C
    * H("i0")
    * Omega1("-X0").C
    * Omega1("X0")
)
TERMS.append(lambda_hat_Omega1_term)

# lambda_hat_Omega2
lambda_hat_Omega2_term = (
    Coupling(
        "lambdaHatOmega2", [], is_complex=False, latex="\\hat{\\lambda}_{\\Omega_2}"
    )
    * H("i0").C
    * H("i0")
    * Omega2("-X0").C
    * Omega2("X0")
)
TERMS.append(lambda_hat_Omega2_term)

# lambda_hat_Omega4
lambda_hat_Omega4_term = (
    Coupling(
        "lambdaHatOmega4", [], is_complex=False, latex="\\hat{\\lambda}_{\\Omega_4}"
    )
    * H("i0").C
    * H("i0")
    * Omega4("-X0").C
    * Omega4("X0")
)
TERMS.append(lambda_hat_Omega4_term)

# lambda_hat_Upsilon
lambda_hat_Upsilon_term = (
    Coupling(
        "lambdaHatUpsilon", [], is_complex=False, latex="\\hat{\\lambda}_{\\Upsilon}"
    )
    * H("i0").C
    * H("i0")
    * Upsilon("-X0", "-I0").C
    * Upsilon("X0", "I0")
)
TERMS.append(lambda_hat_Upsilon_term)

# lambda_hat_Phi
lambda_hat_Phi_term = (
    Coupling("lambdaHatPhi", [], is_complex=False, latex="\\hat{\\lambda}_{\\Phi}")
    * H("i0").C
    * H("i0")
    * Phi("-C0", "i1").C
    * Phi("C0", "i1")
)
TERMS.append(lambda_hat_Phi_term)


# lambda_hat_prime_varphi
lambda_hat_prime_varphi_term = (
    Coupling(
        "lambdaHatPrimevarphi",
        [],
        is_complex=False,
        latex="\\hat{\\lambda}^{\\prime}_{\\varphi}",
    )
    * H("i0").C
    * varphi("i0")
    * varphi("i1").C
    * H("i1")
)
TERMS.append(lambda_hat_prime_varphi_term)


# lambda_hat_prime_Theta1
lambda_hat_prime_Theta1_term = (
    Coupling(
        "lambdaHatPrimeTheta1",
        [],
        is_complex=False,
        latex="\\hat{\\lambda}^{\\prime}_{\\Theta_1}",
    )
    * Theta1("-Q0").C
    * c344("-I0", "Q0", "-Q1")
    * Theta1("Q1")
    * H("i1").C
    * sigma("I0", "i1", "-i2")
    * H("i2")
)
TERMS.append(lambda_hat_prime_Theta1_term)


# lambda_hat_prime_Theta3
lambda_hat_prime_Theta3_term = (
    Coupling(
        "lambdaHatPrimeTheta3",
        [],
        is_complex=False,
        latex="\\hat{\\lambda}^{\\prime}_{\\Theta_3}",
    )
    * Theta3("-Q0").C
    * c344("-I0", "Q0", "-Q1")
    * Theta3("Q1")
    * H("i1").C
    * sigma("I0", "i1", "-i2")
    * H("i2")
)
TERMS.append(lambda_hat_prime_Theta3_term)

# lambda_hat_prime_Pi1
lambda_hat_prime_Pi1_term = (
    Coupling(
        "lambdaHatPrimePi1",
        [],
        is_complex=False,
        latex="\\hat{\\lambda}^{\\prime}_{\\Pi_1}",
    )
    * Pi1("c0", "i0").C
    * H("i0")
    * H("i1").C
    * Pi1("c0", "i1")
)
TERMS.append(lambda_hat_prime_Pi1_term)

# lambda_hat_prime_Pi7
lambda_hat_prime_Pi7_term = (
    Coupling(
        "lambdaHatPrimePi7",
        [],
        is_complex=False,
        latex="\\hat{\\lambda}^{\\prime}_{\\Pi_7}",
    )
    * Pi7("c0", "i0").C
    * H("i0")
    * H("i1").C
    * Pi7("c0", "i1")
)
TERMS.append(lambda_hat_prime_Pi7_term)

# lambda_hat_prime_Phi
lambda_hat_prime_Phi_term = (
    Coupling(
        "lambdaHatPrimePhi",
        [],
        factor=Rational("1/4"),
        is_complex=False,
        latex="\\hat{\\lambda}^{\\prime}_{\\Phi}",
    )
    * Phi("-C0", "i0").C
    * H("i0")
    * H("i1").C
    * Phi("-C1", "i1")
    * lambda_("C0", "c0", "-c1")
    * lambda_("C1", "c1", "-c0")
)
TERMS.append(lambda_hat_prime_Phi_term)


# lambda_hat_prime_zeta
lambda_hat_prime_zeta_term = (
    Coupling(
        "lambdaHatPrimezeta",
        [],
        is_complex=False,
        factor=I / (sqrt(2)),
        latex="\\hat{\\lambda}^{\\prime}_{\\zeta}",
    )
    * zeta("c0", "I0").C
    * zeta("c0", "I1")
    * H("i0").C
    * H("i1")
    * sigma("I2", "i0", "-i1")
    * eps("-I0", "-I1", "-I2")
)
TERMS.append(lambda_hat_prime_zeta_term)

# lambda_hat_prime_Upsilon
lambda_hat_prime_Upsilon_term = (
    Coupling(
        "lambdaHatPrimeUpsilon",
        [],
        is_complex=False,
        factor=I / (sqrt(2)),
        latex="\\hat{\\lambda}^{\\prime}_{\\Upsilon}",
    )
    * Upsilon("-X0", "I0").C
    * Upsilon("X0", "I1")
    * H("i0").C
    * H("i1")
    * sigma("I2", "i0", "-i1")
    * eps("-I0", "-I1", "-I2")
)
TERMS.append(lambda_hat_prime_Upsilon_term)


# lambda_hat_prime_prime_Theta1
# lambda_hat_prime_prime_Theta1_term = (
#     Coupling("lambdaHatPrimePrimeTheta1", [], is_complex=True, latex="\\hat{\\lambda}^{\\prime\\prime}_{\\Theta_1}")
#     * Theta1("Q0")
#     * Theta1("Q2")
#     * H("i0").C
#     * H("i1").C
#     * eps("i2", "i1")
#     * eps4("-Q0", "-Q1")
#     * c344("-I0", "Q1", "-Q2")
#     * sigma("I0", "i0", "-i2")
# )
# TERMS.append(lambda_hat_prime_prime_Theta1_term)

lambda_hat_prime_prime_Theta1_term = (
    Coupling(
        "lambdaHatPrimePrimeTheta1",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}^{\\prime\\prime}_{\\Theta_1}",
    )
    * t2244("i0", "i1", "-Q0", "-Q1")
    * Theta1("Q0")
    * Theta1("Q1")
    * H("i0").C
    * H("i1").C
)
TERMS.append(lambda_hat_prime_prime_Theta1_term)

# lambda_hat_prime_prime_Phi
lambda_hat_prime_prime_Phi_term = (
    Coupling(
        "lambdaHatPrimePrimePhi",
        [],
        factor=Rational("1/4"),
        is_complex=True,
        latex="\\hat{\\lambda}^{\\prime\\prime}_{\\Phi}",
    )
    * H("i0").C
    * Phi("-C0", "i0")
    * H("i1").C
    * Phi("-C1", "i1")
    * lambda_("C0", "c0", "-c1")
    * lambda_("C1", "c1", "-c0")
)
TERMS.append(lambda_hat_prime_prime_Phi_term)


### Tree-level terms for the Lorentz vectors
###

# g_l_VB
g_l_VB_term = (
    Coupling(
        "glVB",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{B}}^{l}]",
    )
    * VB("-l0")
    * L("s0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * L("s1", "i0", "g1")
)
TERMS.append(g_l_VB_term)

# g_q_VB
g_q_VB_term = (
    Coupling(
        "gqVB",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{B}}^{q}]",
    )
    * VB("-l0")
    * Q("s0", "c0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c0", "i0", "g1")
)
TERMS.append(g_q_VB_term)

# g_e_VB
g_e_VB_term = (
    Coupling(
        "geVB",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{B}}^{e}]",
    )
    * VB("-l0")
    * eR("s0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * eR("s1", "g1")
)
TERMS.append(g_e_VB_term)

# g_u_VB
g_u_VB_term = (
    Coupling(
        "guVB",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{B}}^{u}]",
    )
    * VB("-l0")
    * uR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * uR("s1", "c0", "g1")
)
TERMS.append(g_u_VB_term)

# g_d_VB
g_d_VB_term = (
    Coupling(
        "gdVB",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{B}}^{d}]",
    )
    * VB("-l0")
    * dR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * dR("s1", "c0", "g1")
)
TERMS.append(g_d_VB_term)

# g_phi_VB
g_phi_VB_term = (
    Coupling(
        "gphiVB",
        [],
        is_complex=True,
        latex="[g_{\\mathcal{B}}^{\\phi}]",
    )
    * VB("-l0")
    * H("i0").C
    * DH("l0", "i0")
)
TERMS.append(g_phi_VB_term)

# g_du_VB1
g_du_VB1_term = (
    Coupling(
        "gduVB1",
        "-g0 -g1",
        is_complex=True,
        latex="[g^{du}_{\\mathcal{B}_{1}}]",
    )
    * VB1("-l0").C
    * dR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * uR("s1", "c0", "g1")
)
TERMS.append(g_du_VB1_term)

# g_phi_VB1
g_phi_VB1_term = (
    Coupling(
        "gphiVB1",
        [],
        is_complex=True,
        latex="[g^{\\phi}_{\\mathcal{B}_{1}}]",
    )
    * VB1("-l0").C
    * DH("l0", "i0")
    * H("i1")
    * eps("-i0", "-i1")
)
TERMS.append(g_phi_VB1_term)

# g_l_VW
g_l_VW_term = (
    Coupling(
        "glVW",
        "-g0 -g1",
        is_complex=False,
        factor=Rational("1/2"),
        latex="[g_{\\mathcal{W}}^{l}]",
    )
    * VW("-l0", "-I0")
    * L("s0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * L("s1", "i1", "g1")
    * sigma("I0", "i0", "-i1")
)
TERMS.append(g_l_VW_term)

# g_q_VW
g_q_VW_term = (
    Coupling(
        "gqVW",
        "-g0 -g1",
        is_complex=False,
        factor=Rational("1/2"),
        latex="[g_{\\mathcal{W}}^{q}]",
    )
    * VW("-l0", "-I0")
    * Q("s0", "c0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c0", "i1", "g1")
    * sigma("I0", "i0", "-i1")
)
TERMS.append(g_q_VW_term)

# g_phi_VW
g_phi_VW_term = (
    Coupling(
        "gphiVW",
        [],
        is_complex=True,
        factor=Rational("1/2"),
        latex="[g_{\\mathcal{W}}^{\\phi}]",
    )
    * VW("-l0", "-I0")
    * H("i0").C
    * DH("l0", "i1")
    * sigma("I0", "i0", "-i1")
)
TERMS.append(g_phi_VW_term)

# g_phi_VW1
g_phi_VW1_term = (
    Coupling(
        "gphiVW1",
        [],
        is_complex=True,
        factor=Rational("1/2"),
        latex="[g_{\\mathcal{W_{1}}}^{\\phi}]",
    )
    * VW1("-l0", "-I0").C
    * DH("l0", "i0")
    * H("i2")
    * eps("-i0", "-i1")
    * sigma("I0", "i1", "-i2")
)
TERMS.append(g_phi_VW1_term)

# g_q_VG
g_q_VG_term = (
    Coupling(
        "gqVG",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{G}}^{q}]",
    )
    * VG("-l0", "-C0")
    * Q("s0", "c0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c1", "i0", "g1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(g_q_VG_term)

# g_u_VG
g_u_VG_term = (
    Coupling(
        "guVG",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{G}}^{u}]",
    )
    * VG("-l0", "-C0")
    * uR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * uR("s1", "c1", "g1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(g_u_VG_term)

# g_d_VG
g_d_VG_term = (
    Coupling(
        "gdVG",
        "-g0 -g1",
        is_complex=False,
        latex="[g_{\\mathcal{G}}^{d}]",
    )
    * VG("-l0", "-C0")
    * dR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * dR("s1", "c1", "g1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(g_d_VG_term)

# g_VG1
g_VG1_term = (
    Coupling(
        "gVG1",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{G}_{1}}]",
    )
    * VG1("-l0", "-C0").C
    * dR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * uR("s1", "c1", "g1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(g_VG1_term)

# g_q_VH : (1/2) g_H  H^{μ a A}  \bar q_L σ^a γ_μ T_A q_L
g_q_VH_term = (
    Coupling(
        "gqVH",
        "-g0 -g1",
        factor=Rational("1/2"),
        is_complex=False,
        latex="[g_{\\mathcal{H}}]",
    )
    * VH("-l0", "-C0", "-I0")
    * Q("s0", "c0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c1", "i1", "g1")
    * sigma("I0", "i0", "-i1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(g_q_VH_term)

# γ_{L1}  :  γ_L1  L1_μ^† D^μ φ  + h.c.
gamma_VL1_term = (
    Coupling(
        "gammaVL1",
        [],
        is_complex=True,
        latex="[\\gamma_{\\mathcal{L}_1}]",
    )
    * VL1("-l0", "i0").C
    * DH("l0", "i0")
)
TERMS.append(gamma_VL1_term)

# i g^B_{L1}  L1_μ^† L1_ν B^{μν}
gB_VL1_term = (
    Coupling(
        "gBVL1",
        [],
        is_complex=False,
        latex="[g^{B}_{\\mathcal{L}_1}]",
        factor=I,
    )
    * VL1("-l0", "i0").C
    * VL1("-l1", "i0")
    * FS("B", "l0", "l1")
)
TERMS.append(gB_VL1_term)

# i g^W_{L1}  L1_{i μ}^† σ^a_{ij} L1_{j ν} W^{a μν}
gW_VL1_term = (
    Coupling(
        "gWVL1",
        [],
        is_complex=False,
        latex="[g^{W}_{\\mathcal{L}_1}]",
        factor=I,
    )
    * VL1("-l0", "i0").C
    * VL1("-l1", "i1")
    * sigma("I0", "i0", "-i1")
    * FS("Wi", "l0", "l1", "-I0")
)
TERMS.append(gW_VL1_term)

# i g^{~B}_{L1}  L1_μ^† L1_ν  \tilde{B}^{μν}
#   \tilde{F}^{μν} = (1/2) ε^{μνρσ} F_{ρσ}.
gBt_VL1_term = (
    Coupling(
        "gBtildeVL1",
        [],
        is_complex=False,
        latex="[g^{\\tilde{B}}_{\\mathcal{L}_1}]",
        factor=I * Rational("1/2"), # From dual definition
    )
    * VL1("l0", "i0").C
    * VL1("l1", "i0")
    * FS("B", "l2", "l3")
    * eps("-l0", "-l1", "-l2", "-l3")
)
TERMS.append(gBt_VL1_term)

# i g^{~W}_{L1}  L1_{i μ}^† σ^a_{ij} L1_{j ν}  \tilde{W}^{a μν}
gWt_VL1_term = (
    Coupling(
        "gWtildeVL1",
        [],
        is_complex=False,
        latex="[g^{\\tilde{W}}_{\\mathcal{L}_1}]",
        factor=I * Rational("1/2"), # From dual definition
    )
    * VL1("l0", "i0").C
    * VL1("l1", "i1")
    * sigma("I0", "i0", "-i1")
    * FS("Wi", "l2", "l3", "-I0")
    * eps("-l0", "-l1", "-l2", "-l3")
)
TERMS.append(gWt_VL1_term)

# h^{(1)}_{L1}  (L1_μ^† L1^μ) (φ^† φ)
h1_VL1_term = (
    Coupling(
        "h1VL1",
        [],
        is_complex=False,
        latex="[h^{(1)}_{\\mathcal{L}_1}]",
    )
    * VL1("-l0", "i0").C
    * VL1("l0", "i0")
    * H("i1").C
    * H("i1")
)
TERMS.append(h1_VL1_term)

# h^{(2)}_{L1}  (L1_μ^† φ) (φ^† L1^μ)
h2_VL1_term = (
    Coupling(
        "h2VL1",
        [],
        is_complex=False,
        latex="[h^{(2)}_{\\mathcal{L}_1}]",
    )
    * VL1("-l0", "i0").C
    * H("i0")
    * H("i1").C
    * VL1("l0", "i1")
)
TERMS.append(h2_VL1_term)

# h^{(3)}_{L1}  (L1_μ^† φ) (L1^μ^† φ)
h3_VL1_term = (
    Coupling(
        "h3VL1",
        [],
        is_complex=True,
        latex="[h^{(3)}_{\\mathcal{L}_1}]",
    )
    * VL1("-l0", "i0").C
    * H("i0")
    * VL1("l0", "i1").C
    * H("i1")
)
TERMS.append(h3_VL1_term)

# g_VL3 : (g_{L3}) L3^{μ†} \bar{e}_R^c γ_μ l_L + h.c.
g_VL3_term = (
    Coupling(
        "gVL3",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{L}_3}]",
    )
    * VL3("-l0", "i0").C
    * eR("s0", "g0").CC.bar
    * Ga("l0", "s0", "-s1")
    * L("s1", "i0", "g1")
)
TERMS.append(g_VL3_term)

# (g^{ed}_{U2}) U2^{μ†} \bar e_R γ_μ d_R + h.c.
g_ed_VU2_term = (
    Coupling(
        "gedVU2",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{U}_2}^{ed}]",
    )
    * VU2("-l0", "c0").C
    * eR("s0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * dR("s1", "c0", "g1")
)
TERMS.append(g_ed_VU2_term)

# (g^{lq}_{U2}) U2^{μ†} \bar l_L γ_μ q_L + h.c.
g_lq_VU2_term = (
    Coupling(
        "glqVU2",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{U}_2}^{lq}]",
    )
    * VU2("-l0", "c0").C
    * L("s0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c0", "i0", "g1")
)
TERMS.append(g_lq_VU2_term)

# (g_{U5}) U5^{μ†} \bar e_R γ_μ u_R + h.c.
g_VU5_term = (
    Coupling(
        "gVU5",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{U}_5}]",
    )
    * VU5("-l0", "c0").C
    * eR("s0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * uR("s1", "c0", "g1")
)
TERMS.append(g_VU5_term)


# (g^{ul}_{Q1}) Q1^{μ†} \bar u_R^c γ_μ l_L + h.c.
g_ul_VQ1_term = (
    Coupling(
        "gulVQ1",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{Q}_1}^{ul}]",
    )
    * VQ1("-l0", "c0", "i0").C
    * uR("s0", "c0", "g0").CC.bar
    * Ga("l0", "s0", "-s1")
    * L("s1", "i0", "g1")
)
TERMS.append(g_ul_VQ1_term)

# (g^{dq}_{Q1}) Q1^{μ†}_A ε_{ABC} \bar d_R^B γ_μ (iσ2 q_L^c)^C + h.c.
g_dq_VQ1_term = (
    Coupling(
        "gdqVQ1",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{Q}_1}^{dq}]",
    )
    * VQ1("-l0", "c0", "i0").C
    * dR("s0", "c1", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c2", "i1", "g1").CC
    * eps("c0", "c1", "c2")
    * eps("i0", "i1")
)
TERMS.append(g_dq_VQ1_term)

# (g^{dl}_{Q5}) Q5^{μ†} \bar d_R^c γ_μ l_L + h.c.
g_dl_VQ5_term = (
    Coupling(
        "gdlVQ5",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{Q}_5}^{dl}]",
    )
    * VQ5("-l0", "c0", "i0").C
    * dR("s0", "c0", "g0").CC.bar
    * Ga("l0", "s0", "-s1")
    * L("s1", "i0", "g1")
)
TERMS.append(g_dl_VQ5_term)

# (g^{eq}_{Q5}) Q5^{μ†} \bar e_R^c γ_μ q_L + h.c.
g_eq_VQ5_term = (
    Coupling(
        "geqVQ5",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{Q}_5}^{eq}]",
    )
    * VQ5("-l0", "c0", "i0").C
    * eR("s0", "g0").CC.bar
    * Ga("l0", "s0", "-s1") # should the first spinor index be lowered here?
    * Q("s1", "c0", "i0", "g1")
)
TERMS.append(g_eq_VQ5_term)

# (g^{uq}_{Q5}) Q5^{μ†}_A ε_{ABC} \bar u_R^B γ_μ q_L^{c\,C} + h.c.
g_uq_VQ5_term = (
    Coupling(
        "guqVQ5",
        "-g0 -g1",
        is_complex=True,
        latex="[g_{\\mathcal{Q}_5}^{uq}]",
    )
    * VQ5("-l0", "c0", "i0").C
    * uR("s0", "c1", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c2", "i1", "g1").CC
    * eps("c0", "c1", "c2")
    * eps("i0", "i1")
)
TERMS.append(g_uq_VQ5_term)

# (1/2) g_X  X^{a μ†}  \bar l_L σ^a γ_μ q_L + h.c.
g_VX_term = (
    Coupling(
        "gVX",
        "-g0 -g1",
        factor=Rational("1/2"),
        is_complex=True,
        latex="[g_{\\mathcal{X}}]",
    )
    * VX("-l0", "c0", "-I0").C
    * L("s0", "i0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c0", "i1", "g1")
    * sigma("I0", "i0", "-i1")
)
TERMS.append(g_VX_term)

# (1/2) g_{Y1}  Y1^{AB μ†}  \bar d_R^{(A|} γ_μ (iσ2 q_L^c)^{|B)}  + h.c.
g_VY1_term = (
    Coupling(
        "gVY1",
        "-g0 -g1",
        factor=Rational("1/2"),
        is_complex=True,
        latex="[g_{\\mathcal{Y}_1}]",
    )
    * VY1("-l0", "X0", "i0").C
    * K("-X0", "c0", "c1")
    * dR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c1", "i1", "g1").CC
    * eps("i0", "i1")
)
TERMS.append(g_VY1_term)

# (1/2) g_{Y5}  Y5^{AB μ†}  \bar u_R^{(A|} γ_μ (iσ2 q_L^c)^{|B)}  + h.c.
g_VY5_term = (
    Coupling(
        "gVY5",
        "-g0 -g1",
        factor=Rational("1/2"),
        is_complex=True,
        latex="[g_{\\mathcal{Y}_5}]",
    )
    * VY5("-l0", "X0", "i0").C
    * K("-X0", "c0", "c1")
    * uR("s0", "c0", "g0").bar
    * Ga("l0", "s0", "-s1")
    * Q("s1", "c1", "i1", "g1").CC
    * eps("i0", "i1")
)
TERMS.append(g_VY5_term)
