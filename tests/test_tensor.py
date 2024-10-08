#!/usr/bin/env python3

import pytest
from feynwrite.tensor import Tensor, TensorProduct, Field, Scalar


def test_tensor_indices():
    A = Tensor("A", ["i", "j"])
    B = Tensor("A", ["k", "-j"])
    prod = A * B

    assert isinstance(A, Tensor)
    assert isinstance(prod, TensorProduct)
    assert prod.free_indices == ["i", "k"]

    assert A.label == A.latex
    assert A.is_field

    with pytest.raises(AssertionError):
        (A * A).free_indices


def test_conj():
    A = Tensor("A", ["i", "j"])
    assert A.C.indices == ["-i", "-j"]

    F = Scalar("B", [], hypercharge=0, is_self_conj=True)
    assert F.is_self_conj
    assert F == F.C
    assert not F.C.is_conj

    Adj = Field("C", ["I0"], hypercharge=1, is_self_conj=False)
    assert Adj.C.indices == ["I0"]

    AdjP = Field("CP", ["-I0"], hypercharge=1, is_self_conj=False)
    assert AdjP.C.indices == ["-I0"]
