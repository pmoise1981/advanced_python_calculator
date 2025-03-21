import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.evaluate("2 + 3") == 5

def test_subtraction(calculator):
    assert calculator.evaluate("5 - 3") == 2

def test_multiplication(calculator):
    assert calculator.evaluate("3 * 4") == 12

def test_division(calculator):
    assert calculator.evaluate("8 / 4") == 2

def test_invalid_expression(calculator):
    with pytest.raises(ValueError):
        calculator.evaluate("2 / 0")

