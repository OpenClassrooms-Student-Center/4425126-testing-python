import unittest
import pytest

from calculate.operators import Operators


class TestAdditionOperator(unittest.TestCase):
    def test_should_make_addition(self):
        sut = Operators()
        operation = "5.5 + 10"
        expected_value = 15.5
        self.assertEqual(sut.addition(operation), expected_value)

    def test_should_make_multiple_addition(self):
        sut = Operators()
        operation = "5.5 + 10 + 30 + 13.7"
        expected_value = 59.2
        self.assertEqual(sut.addition(operation), expected_value)

    def test_addition_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "5.5 * 10"
        expected_value = None
        self.assertEqual(sut.addition(operation), expected_value)

    def test_addition_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "5.5 + 10 - 10"
        expected_value = None
        self.assertEqual(sut.addition(operation), expected_value)

    def test_addition_should_return_none_with_non_digit_symbol(self):
        sut = Operators()
        operation = "5.5 + 10 + A"
        expected_value = None
        self.assertEqual(sut.addition(operation), expected_value)


class TestSubstractionOperator(unittest.TestCase):
    def test_should_make_substraction(self):
        sut = Operators()
        operation = "5.5 - 10"
        expected_value = -4.5
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_should_make_multiple_substraction(self):
        sut = Operators()
        operation = "5.5 - 10 - 30 - 13.7"
        expected_value = -48.2
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_substraction_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "5.5 * 10"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_substraction_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "5.5 + 10 - 10"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_substraction_should_return_none_with_non_digit_symbol(self):
        sut = Operators()
        operation = "5.5 - 10 - A"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)


class TestMultiplicationOperator(unittest.TestCase):
    def test_should_make_multiplication(self):
        sut = Operators()
        operation = "5.5 * 10"
        expected_value = 55.0
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_should_make_multiple_multiplication(self):
        sut = Operators()
        operation = "5.5 * 10 * 30 * 13.7"
        expected_value = 22605.0
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_multiplication_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "5.5 / 10"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_multiplication_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "5.5 * 10 - 10"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_multiplication_should_return_none_with_non_digit_symbol(self):
        sut = Operators()
        operation = "5.5 * 10 * A"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)


class TestDivisionOperator(unittest.TestCase):
    def test_should_make_division(self):
        sut = Operators()
        operation = "5.5 / 10"
        expected_value = 0.55
        self.assertEqual(sut.division(operation), pytest.approx(expected_value))

    def test_should_make_multiple_division(self):
        sut = Operators()
        operation = "5.5 / 10 / 10"
        expected_value = 0.055
        self.assertEqual(sut.division(operation), pytest.approx(expected_value))

    def test_division_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "5.5 * 10"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)

    def test_division_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "5.5 / 10 - 10"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)

    def test_division_should_return_none_with_zero_division(self):
        sut = Operators()
        operation = "5.5 / 0"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)


if __name__ == "__main__":
    unittest.main()
