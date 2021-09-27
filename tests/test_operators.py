import pytest

from calculate.operators import Operators


@pytest.mark.parametrize("calculation, result",
    [("5.5 + 10", 15.5), ("2 + 2 + 10", 14), ("4.8 + 5", 9.8)])
def test_should_make_addition(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.addition(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 - 10", None), ("2 + 2 * 10", None)])
def test_addition_should_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.addition(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 - 10", -4.5), ("10 - 3 - 2", 5), ("5 - 5", 0)])
def test_should_make_substraction(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.substraction(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 + 10", None), ("2 - 2 * 10", None)])
def test_substraction_should_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.substraction(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 * 10", 55), ("100 * 2 * 4", 800), ("4.8 * 5", 24)])
def test_should_make_multiplication(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.multiplication(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 + 10", None), ("2 * 2 / 10", None)])
def test_multiplication_should_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.multiplication(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 / 10", 0.55), ("100 / 2 / 10", 5), ("5 / 5", 1)])
def test_should_make_division(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.division(operation) == expected_value

@pytest.mark.parametrize("calculation, result",
    [("5.5 + 10", None), ("2 / 2 + 10", None)])
def test_division_should_return_none_with_wrong_operator(calculation, result):
    sut = Operators()
    operation = calculation
    expected_value = result
    assert sut.division(operation) == expected_value

