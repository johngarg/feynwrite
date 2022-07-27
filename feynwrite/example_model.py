#!/usr/bin/env python3

from feynwrite.sm import L
from feynwrite.tensor import Coupling, Scalar, eps
from feynwrite.model import Model
from feynwrite.granada import TERMS

# # kappaS S phi^dagger phi
# yS1 = Coupling("yS1", "-g0 -g1", is_complex=True)
# S1 = Scalar("S1", [], hypercharge=1)
# term = yS1 * S1.C * L("s0", "i0", "g0").bar * L("s0", "i1", "g1").CC * eps("i0", "i1")
# model = Model(name="S1", terms=[term])

# print(model.export())

# S_terms = []
# for term in TERMS:
#     field_labels = set(f.label for f in term.fields)
#     if "S" in field_labels:
#         S_terms.append(term)

# print(Model("S", terms=S_terms).export())

varphi_terms = []
for term in TERMS:
    field_labels = set(f.label for f in term.fields)
    if "varphi" in field_labels:
        varphi_terms.append(term)

print(Model("varphi", terms=varphi_terms).export())
