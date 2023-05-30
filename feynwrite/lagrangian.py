#!/usr/bin/env python3

import itertools
from alive_progress import alive_bar
from pprint import pprint
from sympy import Rational
from neutrinomass.completions.core import VectorLikeDiracFermion, ComplexScalar, RealScalar, MajoranaFermion
from neutrinomass.tensormethod.core import decompose_product
from neutrinomass.tensormethod.contract import construct_operators
from neutrinomass.tensormethod.sm import H, L, Q, ub, db, eb
from neutrinomass.tensormethod.lagrangian import contains, npoint_terms, remove_equivalent, prod_mass_dim

SM_MATTER = [H("i0"), Q("u0 c0 i0"), ub("u0 -c0"), db("u0 -c0"), L("u0 i0"), eb("u0")]
SM_MATTER_LABELS = [f.label for f in SM_MATTER]

def contains_exotic(fields):
    """Returns True if any of the fields are exotic. That is, if any are a
    RealScalar, a ComplexScalar, a MajoranaFermion or a VectorLikeDiracFermion.

    """
    for f in fields:
        if f.label not in SM_MATTER_LABELS:
            return True
    return False

def npoint_fieldstrings(n, fields=(L, eb, Q, db, ub, H), derivs=False, func=None):
    """Returns all possible n-point fieldstrings with the given fields."""

    conjs = tuple([f.conj for f in fields])
    if derivs:
        T = Field("D", "11000", charges={"y": 0})
        fields += (T,)

    combos = list(itertools.combinations_with_replacement(fields + conjs, n))
    terms = []
    with alive_bar(len(combos)) as bar:
        while combos:
            combo = combos.pop(0)

            if func is not None:
                if not func(combo):
                    bar()
                    continue

            prods = decompose_product(*combo)
            singlets = [i for i in prods if i.is_singlet]
            if singlets:
                terms += [singlets[0]]
            bar()

    return terms

def four_point_scalar_terms(exotic_fields):
    """Returns all possible 4-point terms with the given fields that satisfy the
    conditions of Table 2 in https://arxiv.org/pdf/2103.11593.pdf.

    """

    conjs = [f.conj for f in exotic_fields]

    combos = list(itertools.combinations_with_replacement(exotic_fields + conjs, 2))
    higgs_combos = [(H, H), (H.conj, H.conj), (H, H.conj)]
    terms = []
    while combos:
        combo = combos.pop(0)
        f1, f2 = combo

        if abs(f1.charges["y"] + f2.charges["y"]) != 1:
            continue

        for irrep in f1.field * f2.field:
            if irrep.colour_irrep == (0, 0) and irrep.isospin_irrep in {(0,), (2,)}:
                for higgs_combo in higgs_combos:
                    prods = decompose_product(f1.field, f2.field, *higgs_combo)
                    singlets = [i for i in prods if i.is_singlet]
                    if singlets:
                        terms += singlets

    return terms

def generate_uv_terms(fields: set):
    all_fields = SM_MATTER + [f.field for f in fields]
    cubic_terms = npoint_fieldstrings(n=3, fields=tuple(all_fields), func=contains_exotic)
    quartic_terms = npoint_fieldstrings(n=4, fields=tuple(all_fields), func=contains_exotic)

    # Only keep terms that contain exotic fields
    # return [i for i in out if i != 0 and contains(i, [f.field for f in fields])]
    return [t for t in cubic_terms + quartic_terms if prod_mass_dim(t.walked()) <= 4]

    # ignore = ["c"]
    # cubic_terms = npoint_terms(3, all_fields, ignore=ignore)
    # quartic_terms = npoint_terms(4, all_fields, ignore=ignore)

    # out = []
    # for term in [*cubic_terms, *quartic_terms]:
    #     if term.mass_dim <= 4:
    #         out.append(term)

    # eq = lambda x, y: x.safe_simplify() == y.safe_simplify()
    # remove_equivalent(out, eq_func=eq)
    # # Only keep terms that contain exotic fields
    # return [i for i in out if i != 0 and contains(i, [f.field for f in fields])]


S = RealScalar('S', "", charges={"y": 0})
S1 = ComplexScalar('S1', "", charges={"y": 1})
S2 = ComplexScalar('S2', "", charges={"y": 2})
varphi = ComplexScalar('varphi', "i0", charges={"y": Rational("1/2")})
Xi = RealScalar('Xi', "i0 i1", charges={"y": 0})
Xi1 = ComplexScalar('Xi1', "i0 i1", charges={"y": 1})
Theta1 = ComplexScalar('Theta1', "i0 i1 i3", charges={"y": Rational("1/2")})
Theta3 = ComplexScalar('Theta3', "i0 i1 i3", charges={"y": Rational("3/2")})

omega1 = ComplexScalar('omega1', "c0", charges={"y": Rational("-1/3")})
omega2 = ComplexScalar('omega2', "c0", charges={"y": Rational("2/3")})
omega4 = ComplexScalar('omega4', "c0", charges={"y": Rational("-4/3")})
Pi1 = ComplexScalar('Pi1', "c0 i0", charges={"y": Rational("1/6")})
Pi7 = ComplexScalar('Pi7', "c0 i0", charges={"y": Rational("7/6")})
zeta = ComplexScalar('zeta', "c0 i0 i1", charges={"y": Rational("-1/3")})

Omega1 = ComplexScalar('Omega1', "c0 c1", charges={"y": Rational("1/3")})
Omega2 = ComplexScalar('Omega2', "c0 c1", charges={"y": Rational("-2/3")})
Omega4 = ComplexScalar('Omega4', "c0 c1", charges={"y": Rational("4/3")})
Upsilon = ComplexScalar('Upsilon', "c0 c1 i0 i1", charges={"y": Rational("1/3")})
Phi = ComplexScalar('Phi', "c0 -c1 i0", charges={"y": Rational("1/2")})

GRANADA_SCALARS = {S2, S1, S, varphi, Xi, Xi1, Theta1, Theta3, omega1, omega2, omega4, Pi1, Pi7, zeta, Omega1, Omega2, Omega4, Upsilon, Phi}

E = VectorLikeDiracFermion('E', "u0", charges={"y": Rational(1)})
Delta1 = VectorLikeDiracFermion('Delta1', "u0 i0", charges={"y": Rational("-1/2")})
Delta3 = VectorLikeDiracFermion('Delta3', "u0 i0", charges={"y": Rational("-3/2")})

GRANADA_FERMIONS = {E, Delta1, Delta3}

GRANADA_FIELDS = {*GRANADA_SCALARS, *GRANADA_FERMIONS}

# This is for pairs of fields
def one_loop_scalar_terms(fields: set):
    """Returns all possible one-loop terms with the given fields."""

    # Add Dirac partners
    fields = {
        *fields,
        *[f.dirac_partner() for f in fields if isinstance(f, VectorLikeDiracFermion)]
    }

    # Add conjugates
    fields = {
        *fields,
        *[f.conj for f in fields]
    }

    combos = list(itertools.combinations_with_replacement(fields, 2))
    quartic_coupling, cubic_coupling = [], []
    models_that_need_work = set()
    while combos:
        combo = combos.pop(0)
        f1, f2 = combo

        # Apply criteria from https://arxiv.org/pdf/2103.11593.pdf
        # For cubic coupling
        if abs(f1.charges["y"] + f2.charges["y"]) == Rational("1/2"):
            for irrep in f1.field * f2.field:
                if irrep.colour_irrep == (0, 0) and irrep.isospin_irrep == (1,):
                    cubic_coupling.append(combo)
                    models_that_need_work.add(f"{f1.field.label} {f2.field.label}")

        # For quartic coupling
        if abs(f1.charges["y"] + f2.charges["y"]) == 1:
            for irrep in f1.field * f2.field:
                if irrep.colour_irrep == (0, 0) and irrep.isospin_irrep in {(0,), (2,)}:
                    quartic_coupling.append(combo)
                    models_that_need_work.add(f"{f1.field.label} {f2.field.label}")

    print(len(models_that_need_work))
    print(len(quartic_coupling), len(cubic_coupling))
    print(len(quartic_coupling) + len(cubic_coupling))

    return models_that_need_work, cubic_coupling, quartic_coupling


# for pair in itertools.combinations(GRANADA_FIELDS, 2):
#     print(pair)
#     a, b = pair
#     pair_list = [a, b]
#     if a in GRANADA_FERMIONS:
#         pair_list.append(a.dirac_partner())
#     if b in GRANADA_FERMIONS:
#         pair_list.append(b.dirac_partner())

#     for term in set(generate_uv_terms(pair_list)):
#         latex_terms = []
#         for subterm in construct_operators(term.walked(), ignore=[]):
#             latex_terms.append(tuple([f.get_latex() for f in subterm.fields]))
#             print(set(latex_terms))
#     print()



def one_loop_scalar_terms():
    cubic_terms = []
    for f1,f2 in itertools.combinations(GRANADA_SCALARS, 2):
        if abs(f1.charges["y"] + f2.charges["y"]) == Rational("1/2") or abs(f1.charges["y"] - f2.charges["y"]) == Rational("1/2"):
            for irrep in f1.field * f2.field:
                if irrep.colour_irrep == (0, 0) and irrep.isospin_irrep == (1,):
                    print(f1, f2)

def quad_scalar_terms():
    quad_terms = []
    for f1,f2 in itertools.combinations(GRANADA_SCALARS, 2):
        if abs(f1.charges["y"] + f2.charges["y"]) == Rational("1/2") or abs(f1.charges["y"] - f2.charges["y"]) == Rational("1/2"):
            for irrep in f1.field * f2.field:
                if irrep.colour_irrep == (0, 0) and irrep.isospin_irrep == (1,):
                    print(f1, f2)
