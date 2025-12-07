"""Dictionaries are mutable. This means that change their content without changing their identity.
For example, add, remove, or modify key-value pairs in a dictionary without creating a new dictionary object.
Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
Dictionaries are unordered collections, meaning that the order of key-value pairs is not guaranteed.
Dictionaries will have unique keys.
They are commonly used to store and retrieve data based on unique keys.
Dictionaries are ordered as of Python 3.7, meaning that they maintain the insertion order of key-value pairs.
"""
# Creation of a dictionary.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Original dictionary:", my_dict)
# Accessing values using keys.
print("Name:", my_dict['name'])
# Modifying a value.
my_dict['age'] = 31
print("Modified dictionary:", my_dict)
# Adding a new key-value pair.
my_dict['job'] = 'Engineer'
print("Dictionary after adding a new key-value pair:", my_dict)
# Removing a key-value pair.
del my_dict['city']
print("Dictionary after removing a key-value pair:", my_dict)
# Iterating through a dictionary.
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Checking if a key exists.
if 'name' in my_dict:
    print("Key 'name' exists in the dictionary.")
# Getting the number of key-value pairs.
print("Number of key-value pairs:", len(my_dict))
# Clearing all key-value pairs.
my_dict.clear()
print("Dictionary after clearing all key-value pairs:", my_dict)
# Demonstrating that the dictionary is mutable by checking its identity.
my_dict = {'name': 'Alice', 'age': 30}
print("New dictionary:", my_dict)
print("Dictionary ID before modification:", id(my_dict))
my_dict['age'] = 31
print("Dictionary after modification:", my_dict)
print("Dictionary ID after modification:", id(my_dict))
# The ID remains the same, showing that the dictionary is mutable.
my_dict1 = dict(a=1, b=2)
print(my_dict1.get('a'))
print(my_dict1['b'])
print("Dictionary created using dict():", my_dict1)
my_dict2 = {}
my_dict2['x'] = 10
print("Dictionary created using empty braces and adding key-value pair:", my_dict2)