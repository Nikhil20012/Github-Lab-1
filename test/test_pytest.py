import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import pytest
from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(5, 0) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2


def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(5, 0) == 5
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(-1, -1) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5, 0) == 0
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1

def test_add_three():
    assert calculator.add_three(2, 3, 5) == 10
    assert calculator.add_three(5, 0, -1) == 4
    assert calculator.add_three(-1, -1, -1) == -3
    assert calculator.add_three(-1, -1, 100) == 98

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 3) == 3
    assert calculator.divide(-10, 2) == -5
    assert calculator.divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 2) == 25
    assert calculator.power(10, 0) == 1
    assert calculator.power(2, -1) == 0.5

def test_square_root():
    assert calculator.square_root(16) == 4
    assert calculator.square_root(25) == 5
    assert calculator.square_root(0) == 0
    assert calculator.square_root(2) == pytest.approx(1.414, rel=0.01)

def test_square_root_negative():
    with pytest.raises(ValueError):
        calculator.square_root(-1)
    