import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import unittest
from src import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(5, 0), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(5, 0), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, 0), 0)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_add_three(self):
        self.assertEqual(calculator.add_three(2, 3, 5), 10)
        self.assertEqual(calculator.add_three(5, 0, -1), 4)
        self.assertEqual(calculator.add_three(-1, -1, -1), -3)
        self.assertEqual(calculator.add_three(-1, -1, 100), 98)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(-10, 2), -5)
        self.assertEqual(calculator.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 2), 25)
        self.assertEqual(calculator.power(10, 0), 1)
        self.assertEqual(calculator.power(2, -1), 0.5)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)
        self.assertEqual(calculator.square_root(25), 5)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertAlmostEqual(calculator.square_root(2), 1.414, places=2)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == '__main__':
    unittest.main()