#!/usr/bin/env python3

## Just a place to keep these contributions for now

# lambdaNDelta1: Typo in 1711.10391?
lambdaNDelta1_term = (
    Coupling("lambdaNDelta1", [], is_complex=True, latex="\\lambda_{N \\Delta_1}")
    * N("s0").right.CC.bar
    * Delta1("s0", "i0").right
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaNDelta1_term)

# lambdaNDelta1Prime
lambdaNDelta1Prime_term = (
    Coupling("lambdaNDelta1Prime", [], is_complex=True, latex="{\\lambda_{N \\Delta_1}^\\prime}")
    * N("s0").right.bar
    * Delta1("s0", "i0").left
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaNDelta1Prime_term)

# lambdaEDelta1
lambdaEDelta1_term = (
    Coupling("lambdaEDelta1", [], is_complex=True, latex="\\lambda_{E \\Delta_1}")
    * E("s0").left.bar
    * Delta1("s0", "i0").right
    * H("i0").C
)
TERMS.append(lambdaEDelta1_term)

# lambdaEDelta1Prime
lambdaEDelta1Prime_term = (
    Coupling("lambdaEDelta1Prime", [], is_complex=True, latex="{\\lambda_{E \\Delta_1}^\\prime}")
    * E("s0").right.bar
    * Delta1("s0", "i0").left
    * H("i0").C
)
TERMS.append(lambdaEDelta1Prime_term)

# lambdaEDelta3
lambdaEDelta3_term = (
    Coupling("lambdaEDelta3", [], is_complex=True, latex="\\lambda_{E \\Delta_3}")
    * E("s0").left.bar
    * Delta3("s0", "i0").right
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaEDelta3_term)

# lambdaEDelta3Prime
lambdaEDelta3Prime_term = (
    Coupling("lambdaEDelta3Prime", [], is_complex=True, latex="{\\lambda_{E \\Delta_3}^\\prime}")
    * E("s0").right.bar
    * Delta3("s0", "i0").left
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaEDelta3Prime_term)

# lambdaSigmaDelta1
lambdaSigmaDelta1_term = (
    Coupling("lambdaSigmaDelta1", [], is_complex=True, factor=Rational("1/2"), latex="{\\lambda_{\\Sigma \\Delta_1}}")
    * Sigma("s0", "-I0").right.CC.bar
    * Delta1("s0", "i0").right
    * sigma("I0", "i1", "-i0")
    * H("i2")
    * eps("-i2", "-i1")
)
TERMS.append(lambdaSigmaDelta1_term)

# lambdaSigmaDelta1Prime
lambdaSigmaDelta1Prime_term = (
    Coupling("lambdaSigmaDelta1Prime", [], is_complex=True, factor=Rational("1/2"), latex="{\\lambda_{\\Sigma \\Delta_1}^{\\prime}}")
    * Sigma("s0", "-I0").right.bar
    * Delta1("s0", "i0").left
    * sigma("I0", "i1", "-i0")
    * H("i2")
    * eps("-i2", "-i1")
)
TERMS.append(lambdaSigmaDelta1Prime_term)

# lambdaSigma1Delta1
lambdaSigma1Delta1_term = (
    Coupling("lambdaSigma1Delta1", [], is_complex=True, factor=Rational("1/2"), latex="\\lambda_{\\Sigma_1 \\Delta_1}")
    * Sigma1("s0", "-I0").left.bar
    * Delta1("s0", "i0").right
    * sigma("I0", "i1", "-i0")
    * H("i1").C
)
TERMS.append(lambdaSigma1Delta1_term)

# lambdaSigma1Delta1Prime
lambdaSigma1Delta1Prime_term = (
    Coupling("lambdaSigma1Delta1Prime", [], is_complex=True, factor=Rational("1/2"), latex="{\\lambda_{\\Sigma_1 \\Delta_1}^{\\prime}}")
    * Sigma1("s0", "-I0").right.bar
    * Delta1("s0", "i0").left
    * sigma("I0", "i1", "-i0")
    * H("i1").C
)
TERMS.append(lambdaSigma1Delta1Prime_term)

# lambdaSigma1Delta3
lambdaSigma1Delta3_term = (
    Coupling("lambdaSigma1Delta3", [], is_complex=True, factor=Rational("1/2"), latex="\\lambda_{\\Sigma_1 \\Delta_1}")
    * Sigma1("s0", "-I0").left.bar
    * Delta3("s0", "i0").right
    * sigma("I0", "i1", "-i0")
    * H("i2")
    * eps("-i2", "-i1")
)
TERMS.append(lambdaSigma1Delta3_term)

# lambdaSigma1Delta3Prime
lambdaSigma1Delta3Prime_term = (
    Coupling("lambdaSigma1Delta3Prime", [], is_complex=True, factor=Rational("1/2"), latex="{\\lambda_{\\Sigma_1 \\Delta_1}^{\\prime}}")
    * Sigma1("s0", "-I0").right.bar
    * Delta3("s0", "i0").left
    * sigma("I0", "i1", "-i0")
    * H("i2")
    * eps("-i2", "-i1")
)
TERMS.append(lambdaSigma1Delta3Prime_term)


# lambdaUQ1
lambdaUQ1_term = (
    Coupling("lambdaUQ1", [], is_complex=True, latex="\\lambda_{U Q_1}")
    * U("s0", "c0").left.bar
    * Q1("s0", "c0", "i0").right
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaUQ1_term)

# lambdaUQ1Prime
lambdaUQ1Prime_term = (
    Coupling("lambdaUQ1Prime", [], is_complex=True, latex="{\\lambda_{U Q_1}^\\prime}")
    * U("s0", "c0").right.bar
    * Q1("s0", "c0", "i0").left
    * H("i1")
    * eps("-i1", "-i0")
)
TERMS.append(lambdaUQ1Prime_term)
