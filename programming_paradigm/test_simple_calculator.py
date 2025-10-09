import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        """General addition test (required by checker)."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """General subtraction test."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """General multiplication test."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    # --- Division Tests ---
    def test_division(self):
        """General division test."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        """Division by zero should return None."""
        self.assertIsNone(self.calc.divide(5, 0))


if __name__ == '__main__':
    unittest.main()