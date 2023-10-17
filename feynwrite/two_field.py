#!/usr/bin/env python3

"""Defines the terms in the Lagrangian necessary for two-field one-loop graphs of exotic fermions."""

# Depends on: tensor.py, sm.py, granada.py

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
from feynwrite.granada import (
    N,
    ND,
    E,
    Delta1,
    Delta3,
    Sigma,
    SigmaD,
    Sigma1,
    U,
    D,
    Q1,
    Q5,
    Q7,
    T1,
    T2,
)

TWO_FIELD_TERMS = []

# lambdaNDelta1: Typo in 1711.10391?
lambdaNDelta1_term = (
    Coupling("lambdaNDelta1", [], is_complex=True, latex="\\lambda_{N \\Delta_1}")
    * N("s0").CC.bar
    * Delta1("s0", "i0").right
    * H("i1")
    * eps("-i1", "-i0")
)
TWO_FIELD_TERMS.append(lambdaNDelta1_term)

# lambdaEDelta1
lambdaEDelta1_term = (
    Coupling("lambdaEDelta1", [], is_complex=True, latex="\\lambda_{E \\Delta_1}")
    * E("s0").left.bar
    * Delta1("s0", "i0").right
    * H("i0").C
)
TWO_FIELD_TERMS.append(lambdaEDelta1_term)

# lambdaEDelta3
lambdaEDelta3_term = (
    Coupling("lambdaEDelta3", [], is_complex=True, latex="\\lambda_{E \\Delta_3}")
    * E("s0").left.bar
    * Delta3("s0", "i0").right
    * H("i1")
    * eps("-i1", "-i0")
)
TWO_FIELD_TERMS.append(lambdaEDelta3_term)

# lambdaSigmaDelta1
lambdaSigmaDelta1_term = (
    Coupling(
        "lambdaSigmaDelta1",
        [],
        is_complex=True,
        factor=Rational("1/2"),
        latex="{\\lambda_{\\Sigma \\Delta_1}}",
    )
    * Sigma("s0", "-I0").CC.bar
    * Delta1("s0", "i0").right
    * sigma("I0", "i1", "-i0")
    * H("i2")
    * eps("-i2", "-i1")
)
TWO_FIELD_TERMS.append(lambdaSigmaDelta1_term)

# lambdaSigma1Delta1
lambdaSigma1Delta1_term = (
    Coupling(
        "lambdaSigma1Delta1",
        [],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\lambda_{\\Sigma_1 \\Delta_1}",
    )
    * Sigma1("s0", "-I0").left.bar
    * Delta1("s0", "i0").right
    * sigma("I0", "i1", "-i0")
    * H("i1").C
)
TWO_FIELD_TERMS.append(lambdaSigma1Delta1_term)

# lambdaSigma1Delta3
lambdaSigma1Delta3_term = (
    Coupling(
        "lambdaSigma1Delta3",
        [],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\lambda_{\\Sigma_1 \\Delta_1}",
    )
    * Sigma1("s0", "-I0").left.bar
    * Delta3("s0", "i0").right
    * sigma("I0", "i1", "-i0")
    * H("i2")
    * eps("-i2", "-i1")
)
TWO_FIELD_TERMS.append(lambdaSigma1Delta3_term)

### QUARKS

# lambdaUQ1
lambdaUQ1_term = (
    Coupling("lambdaUQ1", [], is_complex=True, latex="\\lambda_{U Q_1}")
    * U("s0", "c0").left.bar
    * Q1("s0", "c0", "i0").right
    * H("i1")
    * eps("-i1", "-i0")
)
TWO_FIELD_TERMS.append(lambdaUQ1_term)

# # lambdaUQ1Prime
# lambdaUQ1Prime_term = (
#     Coupling("lambdaUQ1Prime", [], is_complex=True, latex="{\\lambda_{U Q_1}^\\prime}")
#     * U("s0", "c0").right.bar
#     * Q1("s0", "c0", "i0").left
#     * H("i1")
#     * eps("-i1", "-i0")
# )
# TWO_FIELD_TERMS.append(lambdaUQ1Prime_term)


## FIXME: Did you not finish this?

#### Additional terms necessary for two-field extensions for just the fermions
#### Leptons

# lambda_hat_N_Delta1
lambda_hat_N_Delta1_term = (
    Coupling(
        "lambdaHatNDelta1", [], is_complex=True, latex="\\hat{\\lambda}_{N \\Delta_1}"
    )
    * N("s0").right.bar
    * Delta1("s0", "i0").left
    * H("i1")
    * eps("-i0", "-i1")
)
TWO_FIELD_TERMS.append(lambda_hat_N_Delta1_term)

# lambda_hat_E_Delta1
lambda_hat_E_Delta1_term = (
    Coupling(
        "lambdaHatEDelta1", [], is_complex=True, latex="\\hat{\\lambda}_{E \\Delta_1}",
    )
    * E("s0").right.bar
    * Delta1("s0", "i0").left
    * H("i0").C
)
TWO_FIELD_TERMS.append(lambda_hat_E_Delta1_term)

# lambda_hat_E_Delta3
lambda_hat_E_Delta3_term = (
    Coupling(
        "lambdaHatEDelta3", [], is_complex=True, latex="\\hat{\\lambda}_{E \\Delta_3}",
    )
    * E("s0").right.bar
    * Delta3("s0", "i1").left
    * H("i0")
    * eps("-i0", "-i1")
)
TWO_FIELD_TERMS.append(lambda_hat_E_Delta3_term)

# lambda_hat_Sigma_Delta1
lambda_hat_Sigma_Delta1_term = (
    Coupling(
        "lambdaHatSigmaDelta1",
        [],
        is_complex=True,
        factor=Rational("1/2"),
        latex="\\hat{\\lambda}_{\\Sigma \\Delta_1}",
    )
    * Sigma("s0", "-I0").right.bar
    * Delta1("s0", "i4").left
    * sigma("I0", "i2", "-i4")
    * H("i3")
    * eps("-i3", "-i2")
)
TWO_FIELD_TERMS.append(lambda_hat_Sigma_Delta1_term)

# lambda_hat_Sigma1_Delta1
lambda_hat_Sigma1_Delta1_term = (
    Coupling(
        "lambdaHatSigma1Delta1",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}_{\\Sigma_1 \\Delta_1}",
        factor=Rational("1/2"),
    )
    * Sigma1("s0", "-I0").right.bar
    * Delta1("s0", "i0").left
    * sigma("I0", "i3", "-i0")
    * H("i3").C
)
TWO_FIELD_TERMS.append(lambda_hat_Sigma1_Delta1_term)

# lambda_hat_Sigma1_Delta3
lambda_hat_Sigma1_Delta3_term = (
    Coupling(
        "lambdaHatSigma1Delta3",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}_{\\Sigma_1 \\Delta_3}",
        factor=Rational("1/2"),
    )
    * Sigma1("s0", "-I0").right.bar
    * Delta3("s0", "i4").left
    * sigma("I0", "i2", "-i4")
    * H("i3")
    * eps("-i3", "-i2")
)
TWO_FIELD_TERMS.append(lambda_hat_Sigma1_Delta3_term)


#### Quarks

# lambda_hat_U_Q1
lambda_hat_U_Q1_term = (
    Coupling("lambdaHatUQ1", [], is_complex=True, latex="\\hat{\\lambda}_{U Q_1}",)
    * U("s0", "c0").right.bar
    * Q1("s0", "c0", "i1").left
    * H("i0")
    * eps("-i0", "-i1")
)
TWO_FIELD_TERMS.append(lambda_hat_U_Q1_term)

# lambda_hat_U_Q7
lambda_hat_U_Q7_term = (
    Coupling("lambdaHatUQ7", [], is_complex=True, latex="\\hat{\\lambda}_{U Q_7}",)
    * U("s0", "c0").right.bar
    * Q7("s0", "c0", "i0").left
    * H("i0").C
)
TWO_FIELD_TERMS.append(lambda_hat_U_Q7_term)

# lambda_hat_D_Q1
lambda_hat_D_Q1_term = (
    Coupling("lambdaHatDQ1", [], is_complex=True, latex="\\hat{\\lambda}_{D Q_1}",)
    * D("s0", "c0").right.bar
    * Q1("s0", "c0", "i0").left
    * H("i0").C
)
TWO_FIELD_TERMS.append(lambda_hat_D_Q1_term)

# lambda_hat_D_Q5
lambda_hat_D_Q5_term = (
    Coupling("lambdaHatDQ5", [], is_complex=True, latex="\\hat{\\lambda}_{D Q_5}",)
    * D("s0", "c0").right.bar
    * Q5("s0", "c0", "i1").left
    * H("i0")
    * eps("-i0", "-i1")
)
TWO_FIELD_TERMS.append(lambda_hat_D_Q5_term)

# lambda_hat_T1_Q1
lambda_hat_T1_Q1_term = (
    Coupling(
        "lambdaHatT1Q1",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}_{T_1 Q_1}",
        factor=Rational("1/2"),
    )
    * T1("s0", "c0", "-I0").right.bar
    * Q1("s0", "c0", "i0").left
    * sigma("I0", "i3", "-i0")
    * H("i3").C
)
TWO_FIELD_TERMS.append(lambda_hat_T1_Q1_term)

# lambda_hat_T1_Q5
lambda_hat_T1_Q5_term = (
    Coupling(
        "lambdaHatT1Q5",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}_{T_1 Q_5}",
        factor=Rational("1/2"),
    )
    * T1("s0", "c0", "-I0").right.bar
    * Q5("s0", "c0", "i4").left
    * sigma("I0", "i2", "-i4")
    * H("i3")
    * eps("-i3", "-i2")
)
TWO_FIELD_TERMS.append(lambda_hat_T1_Q5_term)

# lambda_hat_T2_Q1
lambda_hat_T2_Q1_term = (
    Coupling(
        "lambdaHatT2Q1",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}_{T_2 Q_1}",
        factor=Rational("1/2"),
    )
    * T2("s0", "c0", "-I0").right.bar
    * Q1("s0", "c0", "i4").left
    * sigma("I0", "i2", "-i4")
    * H("i3")
    * eps("-i3", "-i2")
)
TWO_FIELD_TERMS.append(lambda_hat_T1_Q5_term)

# lambda_hat_T2_Q7
lambda_hat_T2_Q7_term = (
    Coupling(
        "lambdaHatT2Q7",
        [],
        is_complex=True,
        latex="\\hat{\\lambda}_{T_2 Q_7}",
        factor=Rational("1/2"),
    )
    * T2("s0", "c0", "-I0").right.bar
    * Q7("s0", "c0", "i0").left
    * sigma("I0", "i3", "-i0")
    * H("i3").C
)
TWO_FIELD_TERMS.append(lambda_hat_T2_Q7_term)
