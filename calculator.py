import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid logarithmic arguments")
    return math.log(a, b)


def exp(a, b):
    return a ** b


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of negative number")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError):
        raise ValueError("Invalid hypotenuse arguments")




