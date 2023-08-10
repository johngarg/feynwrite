#!/usr/bin/env python3

"""Defines the multiplets in the Granada dictionary and the terms in the Lagrangian necessary for single-field one-loop graphs."""

# Depends on: tensor.py, sm.py

from fractions import Fraction
from sympy import sqrt, I, Rational
from feynwrite.tensor import (
    Coupling,
    Scalar,
    Fermion,
    eps,
    delta,
    sigma,
    c2224,
    c344,
    t2244,
    K,
    lambda_,
)
from feynwrite.sm import L, Q, H, eR, dR, uR

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
    * Theta1("Q0").C
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
    * Theta3("Q0").C
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
