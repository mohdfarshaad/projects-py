import unittest
from app.config import (
    add,
    subtract,
    multiply,
    divide,
    sine,
    cosine,
    tangent,
    log,
    square_root,
    power,
    factorial,
)


class TestCalculatorFunctions(unittest.TestCase):

    # Test basic arithmetic functions
    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(3, 0), "Error")  # Division by zero

    # Test scientific functions
    def test_sine(self):
        self.assertAlmostEqual(sine(30), 0.5, places=4)
        self.assertAlmostEqual(sine(90), 1.0, places=4)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(60), 0.5, places=4)
        self.assertAlmostEqual(cosine(0), 1.0, places=4)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(45), 1.0, places=4)
        self.assertEqual(tangent(90), "Error")  # Undefined at 90 degrees

    def test_log(self):
        self.assertAlmostEqual(log(10), 2.302585, places=6)
        self.assertEqual(log(-1), "Error")  # Logarithm of negative number

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(-1), "Error")  # Square root of negative number

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 0), 1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-1), "Error")  # Factorial of negative number


if __name__ == "__main__":
    unittest.main()
