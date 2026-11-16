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
