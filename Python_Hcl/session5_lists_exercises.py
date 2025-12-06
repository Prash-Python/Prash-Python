import copy
# #  There are following types of creation of lists in python:
# # 1. Using square brackets []
# # 2. Using list() constructor
# # 3. Using list conversion from tuple.
# # 4. Using range() function
# list1 = [1, 2, 3, 4, 5]
# list2 = list((6, 7, 8, 9, 10))
# list3 = list(range(11, 16))
# list4 = []
# list5 = [x for x in range(16, 21)]
# list6 = list(list1)
# # All above lists are created using different methods and are valid lists in python.
# # By defaulyt, lists can store heterogeneous data types.
# list7 = [1, "two", 3.0, [4, 5], (6, 7), {8: "eight"}]
# print(list7[3][1])  # Accessing element '5' from the nested list [4, 5]
# print(list7[4][0])  # Accessing element '6' from the nested tuple (6, 7)
# print(list7[5][8])  # Accessing value 'eight' from the nested dictionary {8: "eight"}
# # Take input from user to create a list of integers
# user_input = list(input("Enter integers: "))
# print("You entered:", user_input) # This will create a list of characters from the input string
# user_input_int = list([int(x) for x in input("Enter integers separated by space: ").split()])
# print("You entered (as integers):", user_input_int)
# # Repetetion operator * can be used to create a list with repeated elements
# repeated_list = [6] * 5
# print("Repeated list:", repeated_list)  # Output: [6, 6, 6, 6, 6]
# repeated_list = [6 * 5] * 5
# print("Repeated list with multiplied value:", repeated_list)  # Output: [30, 30, 30, 30, 30]
# # Nested lists
# nested_list = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hhh", "iii"], ("jjjj", "kkkk", ["lllll", "mmmmm"]), "n"]
# for item in nested_list:
#     print(nested_list.index(item), ":", item)
# # # Accessing elements in nested lists
# print(nested_list[0])
# print(nested_list[1])
# print(nested_list[1][0])
# print(nested_list[1][1])
# print(nested_list[1][1][0])
# print(nested_list[1][1][1])
# print(nested_list[1][2])
# print(nested_list[1][3])
# print(nested_list[2])
# print(nested_list[3])
# print(nested_list[3][0])
# print(nested_list[3][1])    
# print(nested_list[4])
# print(nested_list[4][0])
# print(nested_list[4][1])
# print(nested_list[4][2])
# print(nested_list[4][2][0])
# print(nested_list[4][2][1])
# print(nested_list[5])
# print(len(nested_list))
# print(len(nested_list[1]))
# print(len(nested_list[1][1]))
# print(len(nested_list[3]))
# print(len(nested_list[4]))
# print(len(nested_list[4][2]))
# Shallow Copy for string and lists. This means the address will remain same for both variables.
# a = 10
# print(a, id(a))
# b = a
# print(b, id(b))
# # Both a and b point to the same integer object 10
# list1 = [1, 2, 3, 4, 5]
# print("Original list1:", list1, id(list1))
# list2 = list1
# print("list2 assigned from list1:", list2, id(list2))
# list1[1] = 5
# print("Original list1 updated:", list1, id(list1))
# print("list2 after modifying list1:", list2, id(list2))
# list1.append(6)
# print("Original list1 after append:", list1, id(list1))
# print("list2 after appending to list1:", list2, id(list2))
# Deep Copy for lists using copy() method or list() constructor or slicing. This means the address will be different for both variables.
# original_list = [1, 2, 3, 4, 5]
# print("Original list:", original_list, id(original_list))
# deep_copied_list = copy.deepcopy(original_list)
# print("Deep copied list using copy.deepcopy():", deep_copied_list, id(deep_copied_list))
# list = [1, 2, 3, 4, 5]
# print(max(list))  # Output: 5
# print(min(list))  # Output: 1 max will work for same data types only in list.
# list_mixed = [1, "two", 3.0, 4, "five"]
# # print(max(list_mixed))  # This will raise TypeError
# # Performing various list operations and printing the list after each operation.
# my_list = []
# my_list.append(10)
# print("After appending 10:", my_list)
# my_list.append(20)
# print("After appending 20:", my_list)
# my_list.append(30)
# print("After appending 30:", my_list)
# my_list.extend([40, 50, 60])
# print("After extending with [40, 50, 60]:", my_list)
# my_list.insert(6, 70)
# print("After inserting 70 at index 6:", my_list)
# my_list.remove(70)
# print("After removing 70:", my_list)
# popped_element = my_list.pop()
# print("After popping element:", my_list)
# print("Popped element:", popped_element)
# my_list.sort()
# print("After sorting the list:", my_list)
# my_list.reverse()
# print("After reversing the list:", my_list)
# my_list.sort(reverse=True)
# print("After sorting the list in descending order:", my_list)
# my_list.sort(reverse=False)
# print("After sorting the list in ascending order:", my_list)
# my_list.clear()
# print("After clearing the list:", my_list)
# Example of list comprehension to create a list of squares of even numbers from 1 to 5.
# squares_of_even = [x**2 for x in range(1, 6) if x % 2 == 0]
# print("Squares of even numbers from 1 to 5:", squares_of_even)  # Output: [4, 16]
# # Some more examples of list comprehensions
# cubes = [x**3 for x in range(1, 6)]
# print("Cubes of numbers from 1 to 5:", cubes)  # Output: [1, 8, 27, 64, 125]
# even_numbers = [x for x in range(1, 11) if x % 2 == 0]
# print("Even numbers from 1 to 10:", even_numbers)  # Output: [2, 4, 6, 8, 10]
# odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
# print("Odd numbers from 1 to 10:", odd_numbers)  # Output: [1, 3, 5, 7, 9]
# multiples_of_three = [x for x in range(1, 21) if x % 3 == 0]
# print("Multiples of three from 1 to 20:", multiples_of_three)  # Output: [3, 6, 9, 12, 15, 18]
# Square numbers that are even  from 1 to 10
# squares_of_even = [x ** 2 for x in range(1,11) if x % 2 ==0]
# print("Squares of even numbers from 1 to 10:", squares_of_even)  # Output: [4, 16, 36, 64, 100]
# # Square numbers that are odd from 1 to 10
# squares_of_odd = [x ** 2 for x in range(1,11) if x % 2 !=0]
# print("Squares of odd numbers from 1 to 10:", squares_of_odd)  # Output: [1, 9, 25, 49, 81]
# Example to read nested list using list comprehension.
nested_list = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flat_list)  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# Example to create a list of tuples using list comprehension.
tuples_list = [(x, x**2) for x in range(1, 6)]
print("List of tuples (number, square):", tuples_list)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# Example to filter and create a list of prime numbers using list comprehension.
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# prime_numbers = [x for x in range(1, 21) if is_prime(x)]
# print("Prime numbers from 1 to 20:", prime_numbers)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
# Capitalize using list comprehension.
# words = ["hello", "world", "python", "programming"]
# capitalized_words = [word.capitalize() for word in words]
# print("Capitalized words:", capitalized_words)  # Output: ['Hello', 'World', 'Python', 'Programming']
# Another example of list comprehension.
fruits = ["apple", "banana", "cherry", "date", "orange"]
fruits_name_starts_with_a = [fruit for fruit in fruits if fruit.startswith('a')]
print("Fruits starting with 'a':", fruits_name_starts_with_a)  # Output: ['apple']
fruits_name_ends_with_e = [fruit for fruit in fruits if fruit.endswith('e')]
print("Fruits ending with 'e':", fruits_name_ends_with_e)  # Output: ['apple', 'date', 'orange']
fruits_name_whose_length_is_5 = [fruit for fruit in fruits if len(fruit) == 5]
print("Fruits with length 5:", fruits_name_whose_length_is_5)  # Output: ['apple']
fruits_name_guava = [fruit for fruit in fruits if fruit == 'guava']
print("Fruits with name 'guava':", fruits_name_guava)  # Output: []
fruits_name_not_banana = [fruit for fruit in fruits if fruit != 'banana']
print("Fruits not named 'banana':", fruits_name_not_banana)  # Output: ['apple', 'cherry', 'date', 'orange']
veg_name = ["carrot", "broccoli", "spinach", "potato", "onion"]
