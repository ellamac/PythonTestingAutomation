# code.py has the functions for add, multiply and power
from sample_code import add, multiply, power
import pytest


def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1
    with pytest.raises(TypeError) as excinfo:
        add("1", 2)


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-3, 4) == -12
    with pytest.raises(TypeError) as excinfo:
        multiply("1", 2)
    assert str(excinfo.value) == "must be and integer!"


def test_power():
    assert power(2, 0) == 1
    assert power(-2, 8) == 256
    with pytest.raises(TypeError) as excinfo:
        power("1", 2)
