# Exercise 1. Print the initials for any name given.
# def print_initials(name):
#     words = name.split(" ")
#     initial_name = ""
#     if len(words) <= 1:
#         print(words)
#     else:
#         for i in range(len(words)-1):
#             initial_name += (words[i][0]).upper() + '.'
#             print(initial_name)
#         initial_name += words[-1].capitalize()
#         print("Initials is: ", initial_name)
# print_initials(input("Enter full name: "))

""" 
------------------------------------------------------------------------------------------------------------------------------
Decorators in python.
"""

def decorator(func):
    def wrapper():
        print("Before calling greet function...")
        func()
        print("After calling greet function...")
    return wrapper

@decorator
def greet():
    print("Hello Java from Python To Kotlin...")
greet()
