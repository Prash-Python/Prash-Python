from functools import reduce
"""
map() used with lambda in Python.
"""
my_list = [1,2,3,4,5,6]
# Perform the squares of each number in above list.
my_squared_list = list(map(lambda x : x * x, my_list)) # This can return multiple values like list.
print(my_squared_list)

"""
filter() used with lambda in Python.
"""
my_list = [1,2,3,4,5,6]
# Perform filter to return the even numbers from given list.
even_numbers_list = list(filter(lambda x : x % 2 == 0, my_list))
print(even_numbers_list) # This can return multiple values like list.

"""
reduce() function with lambda in python. It will always return a single value.
"""
my_list = [1,2,3,4,5,6]
# Returns sum of each number in the given list.
summation_value = reduce(lambda x,y : x + y, my_list)
print(summation_value) # Returns a single value.