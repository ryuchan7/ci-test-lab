import pytest
from calculator import multiply

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(0, 5) == 0
    assert multiply(7, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6