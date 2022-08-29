#!/usr/bin/env python3

"""Defines dictionary of multiplets in Granada dictionary."""

# Depends on: tensor.py, sm.py

from fractions import Fraction
from feynwrite.tensor import (
    Coupling,
    Scalar,
    Fermion,
    eps,
    delta,
    sigma,
    c2224,
    K,
    lambda_,
)
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


def omega1(c) -> Scalar:
    label = "omega1"
    latex = r"\omega_{1}"
    tensor = Scalar(label, [c], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def omega2(c) -> Scalar:
    label = "omega2"
    latex = r"\omega_{2}"
    tensor = Scalar(label, [c], latex=latex, hypercharge=Fraction("2/3"))
    return tensor


def omega4(c) -> Scalar:
    label = "omega4"
    latex = r"\omega_{4}"
    tensor = Scalar(label, [c], latex=latex, hypercharge=Fraction("-4/3"))
    return tensor


def Pi1(c, i) -> Scalar:
    label = "Pi1"
    latex = r"\Pi_{1}"
    tensor = Scalar(label, [c, i], latex=latex, hypercharge=Fraction("1/6"))
    return tensor


def Pi7(c, i) -> Scalar:
    label = "Pi7"
    latex = r"\Pi_{7}"
    tensor = Scalar(label, [c, i], latex=latex, hypercharge=Fraction("7/6"))
    return tensor


def zeta(c, I) -> Scalar:
    label = "zeta"
    latex = r"\zeta"
    tensor = Scalar(label, [c, I], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def Omega1(X) -> Scalar:
    label = "Omega1"
    latex = r"\Omega_{1}"
    tensor = Scalar(label, [X], latex=latex, hypercharge=Fraction("1/3"))
    return tensor


def Omega2(X) -> Scalar:
    label = "Omega2"
    latex = r"\Omega_{2}"
    tensor = Scalar(label, [X], latex=latex, hypercharge=Fraction("-2/3"))
    return tensor


def Omega4(X) -> Scalar:
    label = "Omega4"
    latex = r"\Omega_{4}"
    tensor = Scalar(label, [X], latex=latex, hypercharge=Fraction("4/3"))
    return tensor


def Upsilon(X, I) -> Scalar:
    label = "Upsilon"
    latex = r"\Upsilon"
    tensor = Scalar(label, [X, I], latex=latex, hypercharge=Fraction("1/3"))
    return tensor


def Phi(C, i) -> Scalar:
    label = "Phi2"  # Use different name here since Phi used for Higgs in SM model file
    latex = r"\Phi"
    tensor = Scalar(label, [C, i], latex=latex, hypercharge=Fraction("1/2"))
    return tensor


def N(s) -> Fermion:
    label = "NR"
    latex = "N"
    tensor = Fermion(label, [s], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor


def E(s) -> Fermion:
    label = "ER"
    latex = "E"
    tensor = Fermion(label, [s], latex=latex, hypercharge=-1)
    return tensor


def Delta1(s, i) -> Fermion:
    label = "Delta1"
    latex = r"\Delta_{1}"
    tensor = Fermion(label, [s, i], latex=latex, hypercharge=Fraction("-1/2"))
    return tensor


def Delta3(s, i) -> Fermion:
    label = "Delta3"
    latex = r"\Delta_{3}"
    tensor = Fermion(label, [s, i], latex=latex, hypercharge=Fraction("-3/2"))
    return tensor


def Sigma(s, I) -> Fermion:
    label = "Sigma"
    latex = r"\Sigma"
    tensor = Fermion(label, [s, I], latex=latex, hypercharge=0, is_self_conj=True)
    return tensor


def Sigma1(s, I) -> Fermion:
    label = "Sigma1"
    latex = r"\Sigma_{1}"
    tensor = Fermion(label, [s, I], latex=latex, hypercharge=-1)
    return tensor


def U(s, a) -> Fermion:
    label = "U"
    latex = r"U"
    tensor = Fermion(label, [s, a], latex=latex, hypercharge=Fraction("2/3"))
    return tensor


def D(s, a) -> Fermion:
    label = "D"
    latex = r"D"
    tensor = Fermion(label, [s, a], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def Q1(s, a, i) -> Fermion:
    label = "Q1"
    latex = r"Q_{1}"
    tensor = Fermion(label, [s, a, i], latex=latex, hypercharge=Fraction("1/6"))
    return tensor


def Q5(s, a, i) -> Fermion:
    label = "Q5"
    latex = r"Q_{5}"
    tensor = Fermion(label, [s, a, i], latex=latex, hypercharge=Fraction("-5/6"))
    return tensor


def Q7(s, a, i) -> Fermion:
    label = "Q7"
    latex = r"Q_{7}"
    tensor = Fermion(label, [s, a, i], latex=latex, hypercharge=Fraction("7/6"))
    return tensor


def T1(s, a, I) -> Fermion:
    label = "T1"
    latex = r"T_{1}"
    tensor = Fermion(label, [s, a, I], latex=latex, hypercharge=Fraction("-1/3"))
    return tensor


def T2(s, a, I) -> Fermion:
    label = "T2"
    latex = r"T_{2}"
    tensor = Fermion(label, [s, a, I], latex=latex, hypercharge=Fraction("2/3"))
    return tensor


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

# yqlomega1
yqlomega1_term = (
    Coupling("yqlomega1", ["-g0", "-g1"], is_complex=True)
    * omega1("c0").C
    * Q("s0", "c0", "i0", "g0").CC.bar
    * L("s0", "i1", "g1")
    * eps("-i0", "-i1")
)
TERMS.append(yqlomega1_term)

# yqqomega1
yqqomega1_term = (
    Coupling("yqqomega1", ["-g0", "-g1"], is_complex=True)
    * omega1("c0").C
    * Q("s0", "c1", "i0", "g0").bar
    * Q("s0", "c2", "i1", "g1").CC
    * eps("i0", "i1")
    * eps("c0", "c1", "c2")
)
TERMS.append(yqqomega1_term)

# yeuomega1
yeuomega1_term = (
    Coupling("yeuomega1", ["-g0", "-g1"], is_complex=True)
    * omega1("c0").C
    * eR("s0", "g0").CC.bar
    * uR("s0", "c0", "g1")
)
TERMS.append(yeuomega1_term)

# yduomega1
yduomega1_term = (
    Coupling("yduomega1", ["-g0", "-g1"], is_complex=True)
    * omega1("c0").C
    * dR("s0", "c1", "g0").bar
    * uR("s0", "c2", "g1").CC
    * eps("c0", "c1", "c2")
)
TERMS.append(yduomega1_term)

# yomega2
yomega2_term = (
    Coupling("yomega2", ["-g0", "-g1"], is_complex=True)
    * omega2("c0").C
    * dR("s0", "c1", "g0").bar
    * dR("s0", "c2", "g1").CC
    * eps("c0", "c1", "c2")
)
TERMS.append(yomega2_term)

# yedomega4
yedomega4_term = (
    Coupling("yedomega4", ["-g0", "-g1"], is_complex=True)
    * omega4("c0").C
    * eR("s0", "g0").CC.bar
    * dR("s0", "c0", "g1")
)
TERMS.append(yedomega4_term)

# yuuomega4
yuuomega4_term = (
    Coupling("yuuomega4", ["-g0", "-g1"], is_complex=True)
    * omega4("c0").C
    * uR("s0", "c1", "g0").bar
    * uR("s0", "c2", "g1").CC
    * eps("c0", "c1", "c2")
)
TERMS.append(yuuomega4_term)

# yPi1
yPi1_term = (
    Coupling("yPi1", ["-g0", "-g1"], is_complex=True)
    * Pi1("c0", "i0").C
    * eps("i0", "i1")
    * L("s0", "i1", "g0").bar
    * dR("s0", "c0", "g1")
)
TERMS.append(yPi1_term)

# yluPi7
yluPi7_term = (
    Coupling("yluPi7", ["-g0", "-g1"], is_complex=True)
    * Pi7("c0", "i0").C
    * eps("i0", "i1")
    * L("s0", "i1", "g0").bar
    * uR("s0", "c0", "g1")
)
TERMS.append(yluPi7_term)

# yeqPi7
yeqPi7_term = (
    Coupling("yeqPi7", ["-g0", "-g1"], is_complex=True)
    * Pi7("c0", "i0").C
    * eR("s0", "g0").bar
    * Q("s0", "c0", "i0", "g1")
)
TERMS.append(yeqPi7_term)

# yqlzeta
yqlzeta_term = (
    Coupling("yqlzeta", ["-g0", "-g1"], is_complex=True)
    * zeta("c0", "-I0").C
    * Q("s0", "c0", "i0", "g0").CC.bar
    * L("s0", "i1", "g1")
    * eps("-i0", "-i2")
    * sigma("I0", "i2", "-i1")
)
TERMS.append(yqlzeta_term)

# yqqzeta
yqqzeta_term = (
    Coupling("yqqzeta", ["-g0", "-g1"], is_complex=True)
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
    Coupling("yudOmega1", ["-g0", "-g1"], is_complex=True)
    * Omega1("-X0").C
    * K("X0", "-c0", "-c1")
    * uR("s0", "c0", "g0").CC.bar
    * dR("s0", "c1", "g1")
)
TERMS.append(yudOmega1_term)


# yqqOmega1
yqqOmega1_term = (
    Coupling("yqqOmega1", ["-g0", "-g1"], is_complex=True)
    * Omega1("-X0").C
    * K("X0", "-c0", "-c1")
    * Q("s0", "c0", "i0", "g0").CC.bar
    * Q("s0", "c1", "i1", "g1")
    * eps("-i0", "-i1")
)
TERMS.append(yqqOmega1_term)

# yOmega2
yOmega2_term = (
    Coupling("yOmega2", ["-g0", "-g1"], is_complex=True)
    * Omega2("-X0").C
    * K("X0", "-c0", "-c1")
    * dR("s0", "c0", "g0").CC.bar
    * dR("s0", "c1", "g1")
)
TERMS.append(yOmega2_term)

# yUpsilon
yUpsilon_term = (
    Coupling("yUpsilon", ["-g0", "-g1"], is_complex=True)
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
    Coupling("yquPhi", ["-g0", "-g1"], is_complex=True, factor="1/2")
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
    Coupling("ydqPhi", ["-g0", "-g1"], is_complex=True, factor="1/2")
    * Phi("-C0", "i0").C
    * dR("s0", "c0", "g0").bar
    * Q("s0", "c1", "i0", "g1")
    * lambda_("C0", "c0", "-c1")
)
TERMS.append(ydqPhi_term)

# lambdaN
lambdaN_term = (
    Coupling("lambdaN", ["-g0"], is_complex=True)
    * N("s0").right.bar
    * L("s0", "i0", "g0")
    * eps("-i0", "-i1")
    * H("i1")
)
TERMS.append(lambdaN_term)

# lambdaE
lambdaE_term = (
    Coupling("lambdaE", ["-g0"], is_complex=True)
    * E("s0").right.bar
    * L("s0", "i0", "g0")
    * H("i0").C
)
TERMS.append(lambdaE_term)

# lambdaDelta1
lambdaDelta1_term = (
    Coupling("lambdaDelta1", ["-g0"], is_complex=True)
    * Delta1("s0", "i0").left.bar
    * eR("s0", "g0")
    * H("i0")
)
TERMS.append(lambdaDelta1_term)

# lambdaDelta3
lambdaDelta3_term = (
    Coupling("lambdaDelta3", ["-g0"], is_complex=True)
    * Delta3("s0", "i0").left.bar
    * eR("s0", "g0")
    * H("i1").C
    * eps("i0", "i1")
)
TERMS.append(lambdaDelta3_term)

# lambdaSigma
lambdaSigma_term = (
    Coupling("lambdaSigma", ["-g0"], is_complex=True, factor="1/2")
    * Sigma("s0", "-I0").right.bar
    * L("s0", "i4", "g0")
    * sigma("I0", "i2", "-i4")
    * H("i3")
    * eps("-i3", "-i2")
)
TERMS.append(lambdaSigma_term)

# lambdaSigma
lambdaSigma1_term = (
    Coupling("lambdaSigma1", ["-g0"], is_complex=True, factor="1/2")
    * Sigma1("s0", "-I0").right.bar
    * L("s0", "i4", "g0")
    * sigma("I0", "i3", "-i4")
    * H("i3").C
)
TERMS.append(lambdaSigma1_term)

# lambdaNDelta1
lambdaNDelta1_term = (
    Coupling("lambdaNDelta1", [], is_complex=True)
    * N("s0").right.CC.bar
    * Delta1("s0", "i0").right
    * H("i1")
    * eps("-i0", "-i1")
)
TERMS.append(lambdaNDelta1_term)

# lambdaEDelta1
lambdaEDelta1_term = (
    Coupling("lambdaEDelta1", [], is_complex=True)
    * E("s0").left.bar
    * Delta1("s0", "i0").right
    * H("i0").C
)
TERMS.append(lambdaEDelta1_term)
