"""
There are two ways to have the modules in our functions. Using:
import module_name => It brings entire module.
from modele_name import function_name => It brings only the one called module here.
"""

# Simple function for calculator operations.
def calculator(a, b):
    add = a + b
    diff = a - b
    prod = a * b
    div = a / b
    mod = a % b
    return add, diff, prod, div, mod

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    a, b, c, d, e = calculator(x, y)
    print("Addition: ", a)
    print("Difference: ", b)
    print("Product: ", c)
    print("Division: ", d)
    print("Modulo: ", e)
main()

# Nested Functions.
def outer():
    print("In Outer function...")
    def inner():
        print("In Inner function...")
    inner()
outer()