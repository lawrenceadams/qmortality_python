import pytest
from qmortality import qmortality_female

def test_qmortality_female():
    female_1 = qmortality_female(
    75,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    40,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    2)

    assert female_1 == 1.605573