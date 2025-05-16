from csv import Error
import math


# Basic arithmetic functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error"
    return x / y


# Scientific functions
def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    if x % 180 == 90:
        return "Error"
    return math.tan(math.radians(x))


def log(x):
    if x <= 0:
        return "Error"
    return math.log(x)


def square_root(x):
    if x < 0:
        return "Error"
    return math.sqrt(x)


def power(x, y):
    return math.pow(x, y)


def factorial(x):
    if x < 0 or not x.is_integer():
        return "Error"
    return math.factorial(int(x))


# Additional functions like trigonometric, logarithmic etc. can be added as needed.
