import unittest
from calculator import *


class TestCalculator(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(50, 60), 110)

    def test_subtract(self):
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(5, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 2), 1)
        self.assertAlmostEqual(logarithm(27, 3), 3)
        self.assertAlmostEqual(logarithm(4, 2), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, -1)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 9), 2.25)
        self.assertAlmostEqual(div(-2, 10), -5)

    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm, 0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(25), 5)
        self.assertRaises(ValueError, square_root, -9)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
