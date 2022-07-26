#!/usr/bin/env python3

import pytest
from feynwrite.tensor import Tensor, TensorProduct


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
