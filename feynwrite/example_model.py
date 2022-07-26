#!/usr/bin/env python3

from sm import L
from tensor import Coupling, Scalar, eps
from feynrules import Model

# kappaS S phi^dagger phi
yS1 = Coupling("yS1", "-g0 -g1", is_complex=True)
S1 = Scalar("S1", [], hypercharge=1)
term = yS1 * S1.C * L("s0", "i0", "g0").bar * L("s0", "i1", "g1").CC * eps("i0", "i1")

model = Model(name="S1", terms=[term])

print(model.export())
