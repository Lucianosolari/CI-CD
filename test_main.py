import pytest
from main import suma, resta, multiplica, divide, cubeNumber


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0.3, 0.7) == 1


def test_resta():
    assert resta(5, 2) == 3
    assert resta(1, 1) == 0


def test_multiplica():
    assert multiplica(3, 4) == 12
    assert multiplica(-1, 5) == -5


def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 1) == 3
    with pytest.raises(ValueError):
        divide(5, 0)

def test_cubeNumber():
    assert cube(3) == 27
    assert cube(2) == 8