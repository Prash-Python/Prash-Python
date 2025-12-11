# Exercise 1. Print the initials for any name given.
def print_initials(name):
    words = name.split(" ")
    initial_name = ""
    if len(words) <= 1:
        print(words)
    else:
        for i in range(len(words)-1):
            initial_name += (words[i][0]).upper() + '.'
            print(initial_name)
        initial_name += words[-1].capitalize()
        print("Initials is: ", initial_name)
print_initials(input("Enter full name: "))

""" 
------------------------------------------------------------------------------------------------------------------------------
Decorators in python.
"""

# The greet() function comes here as parameter. Decorator using the wrapper will execute it and then return back to caller.
# This is step 3. This essentially will go in executed manner as wrapper back to step 1, where it was firstly called.
def decorator(func):
    def wrapper():
        print("Before calling greet function...")
        func()
        print("After calling greet function...")
    return wrapper

# The moment greet() is called, it will come up as parameter to decorator due to annotation @decorator here below. This is step 2.
@decorator
def greet():
    print("Hello Java from Python To Kotlin...")
# The call initialisation happens at the below step. This is step 1.
greet()

"""
Multiple Function Decorators Example.
"""

def decorator(func):
    def wrapper():
        print("Greet before actual function call...")
        func()
        print("Greet after actual function call...")
    return wrapper

@decorator
def greet_java():
    print("Greetings from Java world...")

@decorator
def greet_python():
    print("Greetings from python world...")

@decorator
def greet_kotlin():
    print("Greetings from kotlin world...")

print()
print()
greet_java()
print()
print()
greet_kotlin()
print()
print()
greet_python()
print()
print()

# -----------------------------------------------------------------------------------------------------------------------------
"""
Decorators for functions that can have its own parameters/arguments.
"""
def my_summation_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before addition action...")
        result = func(*args, **kwargs)
        print("After addition action...")
        return result
    return wrapper

@my_summation_decorator
def add_numbers(a,b):
    return a + b
result = add_numbers(5,6)
print(result)
print()
print()

"""
Decorators chaining.
"""

# Decorator 1
# Decorator 2

def decorator1(func):
    def wrapper():
        print("In Decorator 1...")
        x = func()
        return x * x
    return wrapper

def decorator2(func):
    def wrapper():
        print("In Decorator 2...")
        y = func()
        return 2 * y
    return wrapper

@decorator1
@decorator2
def num():
    return 10
print(num())


