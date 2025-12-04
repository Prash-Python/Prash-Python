# Create empty list
my_list1 = []
my_list2 = list()
print("Empty Lists:", my_list1, my_list2)
print("Type of my_list1:", type(my_list1))
print("Type of my_list2:", type(my_list2))
# Create empty tuple
my_tuple1 = ()
my_tuple2 = tuple()
print("Empty Tuples:", my_tuple1, my_tuple2)
print("Type of my_tuple1:", type(my_tuple1))
print("Type of my_tuple2:", type(my_tuple2))
# Create empty dictionary
my_dict1 = {}
my_dict2 = dict()
print("Empty Dictionaries:", my_dict1, my_dict2)
print("Type of my_dict1:", type(my_dict1))
print("Type of my_dict2:", type(my_dict2))
# Create empty set and sets are mutable with unique elements.
my_set1 = set()
print("Empty Set:", my_set1)
print("Type of my_set1:", type(my_set1))
my_set1 = {1, 2, 3, 4, 5}
print("Non-empty Set:", my_set1)
print("Type of my_set1:", type(my_set1))
my_set1.add(6)
print("Set after adding an element:", my_set1)
my_set1.remove(2)
print("Set after removing an element:", my_set1)
my_set1.update([7, 8, 9])
print("Set after updating with multiple elements:", my_set1)
# Both Sets and Dictionaries are unordered collections.
# However, Dictionaries store data in key-value pairs.
# Both Sets and Dictionaries use curly braces {} for their declaration. If the Curly braces are empty, it creates an empty dictionary, not a set.
# To create an empty set, we must use the set() function or {}.
my_dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Dictionary:", my_dict1)
print("Type of my_dict1:", type(my_dict1))
print("Accessing value for key 'name':", my_dict1['city'])

