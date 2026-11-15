import math

def add(a,b):
    return a+b

def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
def logarithmic(a,b):
    if a <= 0 or a == 1 or b<=0:
        raise ValueError("Invalid logarithmic arguments")
    return math.log(a,b)
def exponent(a,b):
    return a**b
