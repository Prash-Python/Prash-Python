"""Dictionaries are mutable. This means that change their content without changing their identity.
For example, add, remove, or modify key-value pairs in a dictionary without creating a new dictionary object.
Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
Dictionaries are unordered collections, meaning that the order of key-value pairs is not guaranteed.
Dictionaries will have unique keys.
They are commonly used to store and retrieve data based on unique keys.
Dictionaries are ordered as of Python 3.7, meaning that they maintain the insertion order of key-value pairs.
"""
import copy
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
# Dictionary with tuple keys.
tuple_key_dict = {('a', 1): 'value1', (3, 2): 'value2'}
print("Dictionary with tuple keys:", tuple_key_dict)
# Accessing values using tuple keys.
print("Accessing value with tuple key ('a', 1):", tuple_key_dict[('a', 1)])
print("Accessing value with tuple key (3, 2):", tuple_key_dict[(3, 2)])
# Iteration through dictionary.
dict_iter = {'x': 10, 'y': 20, 'z': 30}
for key in dict_iter:
    print(f"Key: {key}, Value: {dict_iter[key]}")
for key in dict_iter.keys():
    print(f"Key from keys(): {key}")
for value in dict_iter.values():
    print(f"Value from values(): {value}")
for key, value in dict_iter.items():
    print(f"Key from items(): {key}, Value from items(): {value}")
# Creating a set and list from dictionary keys.
my_set = set()
my_list = []
my_new_dict = { 'a': 1, 'b': 2, 'c': 3 }
for k,v in my_new_dict.items():
    my_set.add(k)
    my_list.append(v)
print("Set created from dictionary keys:", my_set)
print("List created from dictionary values:", my_list)
# Creating a dictionary with set and list as key and value.
set_keys = {'p', 'q', 'r'}
list_values = [1, 2, 3]
dict_with_set_list = {k:v for (k,v) in zip(set_keys, list_values)}
print("Dictionary with set as key and list as value:", dict_with_set_list)
# Demonstration of shallow and deep copy further.
original_dict = {'a': 1, 'b': {'c': 2, 'd': 3}}
shallow_copied_dict = copy.copy(original_dict)
deep_copied_dict = copy.deepcopy(original_dict)
print("Original dictionary:", original_dict)
print("Shallow copied dictionary:", shallow_copied_dict)
print("Deep copied dictionary:", deep_copied_dict)
print(original_dict, id(original_dict))
print(shallow_copied_dict, id(shallow_copied_dict))
print(deep_copied_dict, id(deep_copied_dict))
original_dict['b']['c'] = 20
print("After modifying the nested dictionary in the original dictionary:")
print("Original dictionary:", original_dict)
print("Shallow copied dictionary:", shallow_copied_dict)
print("Deep copied dictionary:", deep_copied_dict)
shallow_copied_dict['b']['d'] = 30
print("After modifying the nested dictionary in the shallow copied dictionary:")
print("Original dictionary:", original_dict)
print("Shallow copied dictionary:", shallow_copied_dict)
print("Deep copied dictionary:", deep_copied_dict)
deep_copied_dict['b']['c'] = 200
print("After modifying the nested dictionary in the deep copied dictionary:")
print("Original dictionary:", original_dict)
print("Shallow copied dictionary:", shallow_copied_dict)
print("Deep copied dictionary:", deep_copied_dict)
# Create dictionary using fromKeys with different data types as keys.
keys_list = ['key1', 'key2', 'key3']
default_value = 0
dict_fromkeys = dict.fromkeys(keys_list, default_value)
print("Dictionary created using fromkeys():", dict_fromkeys)
# Using setdefault() to add a key-value pair if the key does not exist.
dict_fromkeys.setdefault('key4', 4)
print("Dictionary after using setdefault():", dict_fromkeys)
# Create dictionary using comprehension with conditional logic.
conditional_dict_even = {x: x**2 for x in range(10) if x % 2 == 0}
print("Dictionary created using comprehension with conditional logic:", conditional_dict_even)
conditional_dict_odd = {x: x**2 for x in range(10) if x % 2 != 0}
print("Dictionary created using comprehension with conditional logic (odd):", conditional_dict_odd)
conditional_dict_squares = {x: x*x for x in range(1, 11) if x*x > 20}
print("Dictionary of squares greater than 20:", conditional_dict_squares)
conditional_dict_cubes = {x: x**3 for x in range(1, 11) if x**3 < 1000}
print("Dictionary of cubes less than 1000:", conditional_dict_cubes)
conditional_dict_prime = {x: 'prime' for x in range(2, 21) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
print("Dictionary of prime numbers:", conditional_dict_prime)
# Merging two dictionaries using the update() method.
dict_one = {'x': 1, 'y': 2}
dict_two = {'y': 3, 'z': 4}
dict_one.update(dict_two)
print("Dictionary after merging using update():", dict_one)
