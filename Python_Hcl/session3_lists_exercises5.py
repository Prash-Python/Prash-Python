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
# Shallow Copy
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