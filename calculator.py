import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a,b):
    if a <= 0 or b == 1 or b <= 0:
        raise ValueError("Invalid logarithmic arguments")
    return math.log(a,b)

def exp(a,b):
    return a**b

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of negative number")

def hypoteneuse(a,b):
    try:
        return math.hypot(a,b)
    except (TypeError, ValueError):
        return ValueError("Invalid hypoteneuse arguments")

