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

# Different types of functional arguments.
"""
1.) Positional arguments.
"""
def foo(name,message):
    print(f"Hello {name}, {message}")
foo("Bob", "Write python codes")

"""
2.) Keyword or named arguments.
"""
def foo(name, age):
    print(f"Hi {name}, your age is {age}")
foo(name="Bob", age=15)
foo(age=15, name="Bob")

"""
3.) Default Arguments.
"""
def foo(name="xyz"):
    print(f"My name is {name}")
foo()
foo("abc")

"""
4.) Indeterminate arguments.
"""
def foo(*args):
    total = 0
    for num in args:
        total += num
    print(f"The total sum is {total}")
foo()
foo(10)
foo(10,20)
foo(10,20,30)