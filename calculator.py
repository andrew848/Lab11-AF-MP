import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def log(a,b):
    if a <= 0 or a == 1 or b<=0:
        raise ValueError("Invalid logarithmic arguments")
    return math.log(a,b)

def exp(a,b):
    return a**b

def square_root(a):
    try:
        return math.sqrt(a)
    except ZeroDivisionError:
        raise ValueError("Cannot take square root of negative number")

def hypotneuse(a,b):
    try:
        return math.hypot(a,b)
    except (TypeError, ValueError):
        return ValueError("Invalid hypotneuse arguments")


def test_multiply(self):
    self.assertEqual(calculator.multiply(3, 4), 12)
    self.assertEqual(calculator.multiply(-2, 5), -10)


def test_divide(self):
    self.assertAlmostEqual(calculator.divide(2, 10), 5)
    self.assertAlmostEqual(calculator.divide(4, 9), 2.25)


def test_log_invalid_argument(self):
    self.assertRaises(ValueError, calculator.logarithm, 2, -10)
    self.assertRaises(ValueError, calculator.logarithm, 2, 0)


def test_hypotenuse(self):
    self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
    self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)


def test_sqrt(self):
    self.assertAlmostEqual(calculator.square_root(16), 4)
    self.assertRaises(ValueError, calculator.square_root, -9)