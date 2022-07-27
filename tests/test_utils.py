#!/usr/bin/env python3


import pytest
from feynwrite.utils import wolfram_index_map


def test_wolfram_index_map():
    assert wolfram_index_map("i0") == "Index[SU2D]"
    assert wolfram_index_map("I11") == "Index[SU2W]"
    assert wolfram_index_map("-c9") == "Index[Colour]"
    assert wolfram_index_map("g") == "Index[Generation]"
