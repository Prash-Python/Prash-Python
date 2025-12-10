import re
import math
from re import split

given_string = "Computer Science 12345 python 78901 java 98765 !@$87642"

# search.
m = re.search("Science", given_string)
print(m.start())
print(m.end())
print(type(m))
print(m)

# Find all.
p = re.compile(r'\d+')
digits = re.findall(p, given_string)
print(digits)

# Compile.
p = re.compile(r'[a-e]')
print(p.findall(given_string))

p = re.compile('[aeiouAEIOU]')
print(p.findall(given_string))
print(len(p.findall(given_string)))

# Single character.
p = re.compile(r'\w')
print(p.findall(given_string))

# Single word.
p = re.compile(r'\w+')
print(p.findall(given_string))

# Single non-word character.
p = re.compile(r'\W')
print(p.findall(given_string))

# Can be zero or more b.
given_string = "abaababbbaba"
p = re.compile('ab*')
print(p.findall(given_string))

# Can be one or more b.
p = re.compile('ab+')
print(p.findall(given_string))

# split function.
print(split(r'\w+', 'Words words Words'))
print(split(r'\W', 'Words words Words'))
print(split(r'\W+', 'Words words Words'))
print(split(r'\d+', 'Words 12 18 words 9 5 Words'))

# re.sub() function.
print(re.sub('ab|AB','**', 'abcdeABpr', re.IGNORECASE))

# Starts with -
p = r'^Hello'
t = "Hello Python World"
match = re.search(p, t)
print(match)
# Ends with $
p = r'World$'
match = re.search(p,t)
print(match)


# Question 1: "Contact us at support@example.com or sales@shop.com"
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




