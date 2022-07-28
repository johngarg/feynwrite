#!/usr/bin/env python3

from feynwrite.granada import TERMS


def test_indices():
    for term in TERMS:
        assert not term.free_indices
        assert term.sum_hypercharges() == 0
