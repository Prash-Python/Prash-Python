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
# Using fromkeys() to create a dictionary with default values.
keys = ['name', 'age', 'city']
default_value = None
my_dict3 = dict.fromkeys(keys, default_value)
print("Dictionary created using fromkeys():", my_dict3)
# Using setdefault() to add a key-value pair if the key does not exist.
my_dict3.setdefault('country', 'USA')
print("Dictionary after using setdefault():", my_dict3)
# Using pop() to remove a key-value pair and return the value.
age = my_dict3.pop('age', 'Not Found')
print("Value popped for key 'age':", age)
print("Dictionary after using pop():", my_dict3)
# Using popitem() to remove and return the last key-value pair.
last_item = my_dict3.popitem()
print("Last item popped using popitem():", last_item)
print("Dictionary after using popitem():", my_dict3)
# Using update() to add multiple key-value pairs.
my_dict3.update({'age': 25, 'city': 'Los Angeles'})
print("Dictionary after using update():", my_dict3)
# Using copy() to create a shallow copy of the dictionary.
my_dict4 = my_dict3.copy()
print("Shallow copy of the dictionary:", my_dict4)
print("Original dictionary ID:", id(my_dict3))
print("Shallow copy dictionary ID:", id(my_dict4))
# The IDs are different, showing that a new dictionary object was created.
# Using nested dictionaries.
nested_dict = { 'person1': {'name': 'Bob', 'age': 28},
                'person2': {'name': 'Carol', 'age': 32}}
print("Nested dictionary:", nested_dict)
print("Accessing nested dictionary value:", nested_dict['person1']['name'])
# Using dictionary comprehension to create a dictionary.
squared_dict = {x: x**2 for x in range(5)}
print("Dictionary created using dictionary comprehension:", squared_dict)
# Using the keys(), values(), and items() methods.
print("Keys:", list(squared_dict.keys()))
print("Values:", list(squared_dict.values()))
print("Items:", list(squared_dict.items()))
# Merging two dictionaries using the | operator (Python 3.9+).
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
merged_dict = dict_a | dict_b
print("Merged dictionary using | operator:", merged_dict)
# Create a dictionary with mixed data types.
mixed_dict = {'integer': 1, 'float': 1.5, 'string': 'hello', 'list': [1, 2, 3], 'tuple': (4, 5), 'dict': {'key': 'value'}, 'boolean': True}
print("Dictionary with mixed data types:", mixed_dict)
# Accessing and modifying nested dictionary values.
mixed_dict['dict']['key'] = 'new_value'
print("Dictionary after modifying nested dictionary value:", mixed_dict)
# Using the get() method with a default value.
print("Accessing a non-existent key with get():", mixed_dict.get('non_existent', 'default_value'))