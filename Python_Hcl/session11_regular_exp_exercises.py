import re

# "Contact us at support@example.com or sales@shop.com"
def extract_email_with_re(given_text):
    pattern = re.compile(r'[a-z]+@[a-z]+.[a-z]')
    match = re.findall(pattern, given_text)
    print(match)
    for m in match:
        if m is not None:
            print(m)
extract_email_with_re("Contact us at support@example.com or sales@shop.com")

# Check if a string is a valid phone number of the format 123-456-7890
def is_valid_phone(number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    print(bool(re.match(pattern, number)))
is_valid_phone("123-456-7890")
is_valid_phone("1234-567-890")
is_valid_phone("123-4567-890")
is_valid_phone("123_456_7890")

# Given a string with extra spaces, replace the extra spaces with a single space.
def replace_extra_space(given_text):
    new_text = re.sub("  ", " ", given_text)
    print(new_text)
replace_extra_space("Python  Programming World  With Java")

""" Write a function that:
Takes a list of values.
Converts them to integers.
If a value is not convertible, handle ValueError.
If the index is out of range, handle IndexError.
Try calling the function with [10, "abc", 30, None]
"""
def convert_list_vals_into_int(my_list):
    try:
        for item in my_list:
            item = int(item)
    except ValueError as ve:
        print(f"Cannot convert the value to integer. Value error {ve}")
    except IndexError as ie:
        print(f"Index out of bounds exception with the error {ie}")
    else:
        for item in my_list:
            print(item)
    finally:
        print("Code execution completed...")
convert_list_vals_into_int([10, "abc", 30, None])

"""
Write a program that:
Asks for two numbers.
Divides them.
Use else to print "Division successful" only if no exception occurred.
Use finally to print "Operation completed" no matter what.
"""
def handle_division_by_zero(a,b):
    try:
        c = a/b
        print(c)
    except ZeroDivisionError as ze:
        print(f"Denominator cannot be Zero. There is error {ze}")
    else:
        print("Division successful...")
    finally:
        print("Operation completed...")

x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
handle_division_by_zero(x,y)

"""
Define a custom exception InvalidAgeError
"""
class InvalidAgeError(Exception):
    print("This is the error handling")
    pass
